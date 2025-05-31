# Import required libraries
from flask import Flask, request, render_template  # For handling web routes and form data
import pandas as pd                                # For creating input DataFrame
import joblib                                      # To load the trained ML model with column structure

# Initialize Flask application
app = Flask(__name__)

# Load the trained model and the column names 
model, model_columns = joblib.load('house_price_model.pkl')

# Home page route 
@app.route('/')
def home():
    return render_template('index.html')  # Renders HTML form

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract input values from form and convert to float
        user_input = {
            'bedrooms': float(request.form['bedrooms']),
            'bathrooms': float(request.form['bathrooms']),
            'sqft_living': float(request.form['sqft_living']),
            'floors': float(request.form['floors']),
            'grade': float(request.form['grade']),
            'zipcode': request.form['zipcode']  # keep as string for one-hot encoding
        }

        # Convert input to DataFrame
        input_df = pd.DataFrame([user_input])

        # One-hot encode the zipcode to match training data
        input_df = pd.get_dummies(input_df, columns=['zipcode'])

        # Reindex to match training column structure, fill missing zipcodes with 0
        input_df = input_df.reindex(columns=model_columns, fill_value=0)

        # Predict the house price
        prediction = model.predict(input_df)[0]

        # Return result to the user
        return render_template('index.html', prediction_text=f'Predicted House Price: ${prediction:,.2f}')

    except Exception as e:
        # Handle errors
        return render_template( 'index.html', prediction_text=f"Error: {str(e)}" )

# Run the application 
if __name__ == '__main__':
    app.run(debug=True)  
