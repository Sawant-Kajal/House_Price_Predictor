# Import required libraries
from flask import Flask, request, render_template  # For web form handling
import pandas as pd                                # For working with data
import joblib                                      # To load the saved model

# Initialize Flask app
app = Flask(__name__)

# Load trained model and saved column names + zipcodes
model, model_columns, zipcodes = joblib.load('house_price_model.pkl')

# Load original dataset to fetch actual prices
df = pd.read_csv('kc_house_data.csv')

# Home page route
@app.route('/')
def home():
    return render_template('index.html', zipcodes=zipcodes)  # Send zipcodes to dropdown

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input values from user form
        user_input = {
            'bedrooms': float(request.form['bedrooms']),
            'bathrooms': float(request.form['bathrooms']),
            'sqft_living': float(request.form['sqft_living']),
            'floors': float(request.form['floors']),
            'grade': float(request.form['grade']),
            'zipcode': request.form['zipcode']
        }

        # Convert to DataFrame
        input_df = pd.DataFrame([user_input])

        # One-hot encode zipcode to match training model format
        input_df = pd.get_dummies(input_df, columns=['zipcode'])

        # Match column structure of model (fill missing zipcodes with 0)
        input_df = input_df.reindex(columns=model_columns, fill_value=0)

        # Check if the zipcode is valid
        if user_input['zipcode'] not in zipcodes:
            return render_template('index.html', prediction_text="Error: Invalid Zipcode", actual_price_text="")

        # Make prediction
        predicted_price = model.predict(input_df)[0]

        # Fetch similar homes from dataset for actual price comparison
        similar_homes = df[
            (df['zipcode'].astype(str) == user_input['zipcode']) &
            (df['bedrooms'] == user_input['bedrooms']) &
            (abs(df['bathrooms'] - user_input['bathrooms']) <= 1)
        ]

        # Calculate average actual price (if similar homes found)
        if not similar_homes.empty:
            actual_avg_price = similar_homes['price'].mean()
            actual_price_text = f"Average Actual Price: ${actual_avg_price:,.2f}"
        else:
            actual_price_text = "No similar homes found in dataset."

        # Show both predicted and actual average price
        return render_template(
            'index.html',
            prediction_text=f"Predicted Price: ${predicted_price:,.2f}",
            actual_price_text=actual_price_text,
            zipcodes=zipcodes
        )

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}", actual_price_text="", zipcodes=zipcodes)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
