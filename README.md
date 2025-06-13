# House Price Prediction Flask App

This repository contains a **Flask-based web application** for predicting house prices using a **Linear Regression** model trained on the `kc_house_data.csv` dataset.

---
![Screenshot (222)](https://github.com/user-attachments/assets/a0703a11-9a34-4245-87b6-447522f83614)

## Project Overview

* **Framework:** Flask (Python)
* **Machine Learning Model:** Linear Regression
* **Dataset:** `kc_house_data.csv`
* **Features Used:**

  * Bedrooms
  * Bathrooms
  * Living area (sqft)
  * Floors
  * Grade
  * Zipcode (one-hot encoded)

Users can input these features through a web form, and the app returns a predicted house price.

---

## Repository Structure

```
├── app.py                  # Main Flask application
├── templates/
│   └── index.html          # Frontend HTML form
├── kc_house_data.csv       # Dataset used for training
├── model.py                # Script to train and save the model
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## Setup and Installation

### 1Clone the Repository

```bash
git clone https://github.com/Sawant-Kajal/house-price-predictor.git
cd house-price-predictor-flask
```

### Create a Virtual Environment and Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run the Flask App

```bash
python app.py
```

The app will be available at:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## Using the Web App

Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

Enter the following details in the form:

* Bedrooms
* Bathrooms
* Living area (sqft)
* Floors
* Grade
* Zipcode (one-hot encoded)

Click **Predict** to get the estimated house price.

---

## Model Evaluation

The model was evaluated using the following regression metrics:

| Metric                  | Value       |
| ----------------------- | ----------- |
| Mean Absolute Error     | \~\$110,045 |
| Root Mean Squared Error | \~\$195,276 |
| R² Score                | \~0.75      |

These results indicate good performance for a basic linear regression model.

---

## Requirements

Contents of `requirements.txt`:

```
Flask
pandas
scikit-learn
numpy
```

Install dependencies using:

```bash
pip install -r requirements.txt
```
---

---

## 🔧 Suggestions for Model Improvement

Although the current model uses **Linear Regression** for simplicity and explainability, the performance can be improved by:

### 📈 Try Advanced Models
- **Random Forest Regressor**
- **Gradient Boosting Regressor (e.g., XGBoost)**
- **LightGBM**

These models can capture non-linear patterns and interactions better than linear regression.

### 🧠 Include More Features from the Dataset
- `condition`
- `waterfront`
- `year_built`
- `view`
- `sqft_basement`

Adding these features can provide the model with more predictive power.

### ⚙️ Hyperparameter Tuning
- Use **Grid Search** or **Random Search** to optimize model parameters.

### 🔄 Feature Scaling or Transformation
- Apply scaling (like StandardScaler) if using models sensitive to feature scale (e.g., SVM, KNN).

> These improvements can help the model generalize better and increase prediction accuracy.

---
