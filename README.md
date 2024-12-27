# Ford Car Price Prediction App

![Streamlit](https://img.shields.io/badge/Streamlit-App-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-yellow)


## Overview
The **Ford Car Price Prediction App** is a web application built using Streamlit that predicts car prices based on various attributes like model, transmission type, fuel type, mileage, and more. The dataset used for this project is sourced from Kaggle and includes information about Ford car prices. The app leverages a machine learning model to provide accurate predictions.

## Features
- **Interactive UI**: User-friendly interface powered by Streamlit.
- **Data Visualization**: Insights into data distributions and correlations.
- **Prediction**: Real-time car price predictions based on user input.

## Dataset
- Source: [Ford Car Price Prediction Dataset](https://www.kaggle.com/datasets/adhurimquku/ford-car-price-prediction)
- Attributes:
  - Price
  - Year
  - Model
  - Mileage
  - Tax
  - MPG
  - Engine Size
  - Fuel Type
  - Transmission

## Tech Stack
- **Python**
- **Libraries**: Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib, Streamlit, Pickle

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/iiTzIsh/Ford_Car-PredictionApp.git
   cd Ford_Car-PredictionApp
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. Access the app in your browser at `http://localhost:8501`.

## Data Preprocessing
- Removed duplicates and handled missing values.
- Identified and removed outliers based on IQR.
- Performed one-hot encoding for categorical features.
- Scaled numerical features using StandardScaler.

## Machine Learning Workflow
- Model: Random Forest Regressor
- Data split into training (80%) and testing (20%) sets.
- Hyperparameter tuning using GridSearchCV.
- Performance Metrics:
  - Mean Squared Error (MSE)
  - R² Score

### Best Model Performance
- **MSE**: `Optimized MSE Value`
- **R² Score**: `Optimized R² Value`

## Visualization
- Distribution plots for numerical features.
- Heatmap for correlation analysis.
- Scatter plot for actual vs. predicted prices.

## File Structure
```
.
├── app.py               # Streamlit app code
├── car_price_model.pkl  # Trained model file
├── ford.csv             # Dataset
├── requirements.txt     # Required Python libraries
└── README.md            # Documentation
```

## How to Use
1. Open the app in your browser.
2. Input the car details (e.g., model, year, mileage).
3. Click the "Predict" button to see the car price prediction.

