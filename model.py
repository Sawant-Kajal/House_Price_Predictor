# Import necessary libraries
import pandas as pd                              # For handling data in tables (DataFrames)
from sklearn.model_selection import train_test_split  # To split the data into training and test sets
from sklearn.linear_model import LinearRegression     # Linear Regression model from scikit-learn
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score  # For model evaluation
import numpy as np                                 # For numeric calculations (square root)
import joblib                                      # For saving/loading ML models easily

# Load the dataset
df = pd.read_csv("kc_house_data.csv") 

# Extract unique zipcodes
zipcodes = df['zipcode'].astype(str).unique().tolist()  # Ensure they are strings

# Select features (inputs) and target (output)
features = ['bedrooms', 'bathrooms', 'sqft_living', 'floors', 'grade', 'zipcode']
X = df[features]     
y = df['price']      # Target variable 

# Convert 'zipcode' from numeric to categorical into a separate column using one-hot encoding
X = pd.get_dummies(X, columns=['zipcode'], drop_first=True)

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)  # Fit the model on training data

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model using standard regression metrics
mae = mean_absolute_error(y_test, y_pred)                  # How far off our predictions are on average
rmse = np.sqrt(mean_squared_error(y_test, y_pred))         # Square root of average squared error
r2 = r2_score(y_test, y_pred)                              # R² score: how well the model explains the variance

# Print evaluation results to understand model performance
print("Model Evaluation:")
print(f"Mean Absolute Error (MAE): ${mae:,.2f}")
print(f"Root Mean Squared Error (RMSE): ${rmse:,.2f}")
print(f"R² Score: {r2:.4f}")

# Display one example prediction for demonstration
print("\nExample prediction:")
print(f"Actual Price: ${y_test.iloc[0]:,.2f}")
print(f"Predicted Price: ${model.predict(X_test.iloc[[0]])[0]:,.2f}")

# Save the trained model AND the column names to a file
joblib.dump((model, X.columns, zipcodes), 'house_price_model.pkl')
print("Model saved successfully!!!")
