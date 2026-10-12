
# 🏠 California House Price Prediction

An end-to-end **Machine Learning + Flask Web Application** that predicts California house prices based on property and demographic information.

The project covers the complete machine learning workflow — from data preprocessing and model training to model persistence, Flask API development, and a user-friendly web interface.

---

## 📌 Project Overview

This project uses the **California Housing Dataset** to predict the median house value of a property based on features such as:

- Longitude
- Latitude
- Housing median age
- Total rooms
- Total bedrooms
- Population
- Households
- Median income
- Ocean proximity

The trained machine learning model is integrated into a **Flask web application**, allowing users to enter property details and receive an estimated house price.

---

## 🎯 Project Objective

The main objective of this project is to build a complete house-price prediction system that demonstrates both **machine learning** and **deployment concepts**.

The project focuses on:

- Preparing and cleaning real-world housing data
- Creating a reliable train/test split
- Handling missing values
- Scaling numerical features
- Encoding categorical variables
- Training multiple regression models
- Comparing model performance
- Selecting a Random Forest Regressor
- Saving the trained model and preprocessing pipeline
- Building a Flask prediction API
- Connecting the ML model to a web interface
- Generating real-time house-price predictions

---

## 🔄 Project Workflow
California Housing Dataset
            ↓
     Data Preprocessing
            ↓
   Stratified Train/Test Split
            ↓
 Numerical + Categorical Features
            ↓
      Data Pipelines
            ↓
   ┌────────┬──────────┬──────────────┐
   ↓        ↓          ↓
Linear   Decision   Random Forest
Regression Tree       Regression
   ↓        ↓          ↓
        Model Evaluation
              ↓
      Random Forest Selected
              ↓
        model.pkl
              +
        pipeline.pkl
              ↓
        Flask Backend
              ↓
       HTML + CSS Frontend
              ↓
       House Price Prediction
## 📊 Dataset
The project uses the California Housing Dataset stored in:
housing.csv

The prediction target is:
median_house_value

Input Features
Feature	Description
longitude	Longitude of the property
latitude	Latitude of the property
housing_median_age	Median age of houses in the area
total_rooms	Total number of rooms
total_bedrooms	Total number of bedrooms
population	Population of the area
households	Number of households
median_income	Median income of the area
ocean_proximity	Location relative to the ocean


Target
median_house_value

## 🧹 Data Preprocessing
The project implements a preprocessing pipeline using Scikit-learn.
Stratified Sampling
Instead of performing a completely random split, the dataset is divided using a stratified sampling strategy based on median_income.
Income categories are created using:
housing["income_cat"] = pd.cut(    housing["median_income"],    bins=[0., 1.5, 3.0, 4.5, 6., np.inf],    labels=[1, 2, 3, 4, 5])


A StratifiedShuffleSplit is then used with:
Test Size: 20%
Random State: 42

This helps preserve the distribution of income categories between the training and test datasets.
⚙️ Feature Processing
The project separates the dataset into numerical and categorical features.
Numerical Features
The numerical columns are processed using:
SimpleImputer
        ↓
Median Imputation
        ↓
StandardScaler

Missing numerical values are replaced using the median.
The numerical features are then standardized using StandardScaler.
Categorical Feature
The categorical feature:
ocean_proximity

is processed using:
OneHotEncoder(handle_unknown="ignore")


This converts categorical values into numerical features that can be used by the machine learning models.
🧩 Scikit-learn Pipeline
The preprocessing steps are combined using:
ColumnTransformer


The complete pipeline contains:
Numerical Pipeline
├── SimpleImputer
└── StandardScaler

Categorical Pipeline
└── OneHotEncoder

        ↓

ColumnTransformer

The preprocessing pipeline is saved separately as:
pipeline.pkl

This ensures that the same preprocessing used during training is also used when making predictions.
🤖 Machine Learning Models
Three regression models were explored during the project.
1. Linear Regression
LinearRegression()


The model is trained on the transformed housing data and evaluated using Root Mean Squared Error.
2. Decision Tree Regressor
DecisionTreeRegressor()


The Decision Tree model is evaluated using 10-fold cross-validation with Root Mean Squared Error.
cross_val_score(    dec_reg,    housing_prepared,    housing_labels,    scoring="neg_root_mean_squared_error",    cv=10)


3. Random Forest Regressor
RandomForestRegressor(random_state=42)


The Random Forest model is ultimately selected for the deployed application.
Random Forest is trained using the processed training dataset and saved using Joblib.
📏 Model Evaluation
The project uses:
Root Mean Squared Error (RMSE)

as the primary regression evaluation metric.
RMSE measures the average magnitude of prediction errors, with larger errors receiving greater weight.
The project evaluates:
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
The Decision Tree also uses 10-fold cross-validation to evaluate its performance across multiple subsets of the training data.
🌲 Final Model
The deployed model is:
Random Forest Regressor

with:
random_state=42


The trained model is saved as:
model.pkl

The preprocessing pipeline is saved as:
pipeline.pkl

💾 Model Persistence
Joblib is used to save and load the trained machine learning objects.
joblib.dump(model, "model.pkl")joblib.dump(pipeline, "pipeline.pkl")


During inference:
model = joblib.load("model.pkl")pipeline = joblib.load("pipeline.pkl")


This allows the Flask application to use the already-trained model without retraining it for every prediction.

## 🔮 Inference Pipeline
The project also contains a separate inference workflow.
Input data can be provided through:
input.csv

The saved preprocessing pipeline transforms the input:
input.csv
     ↓
pipeline.pkl
     ↓
Transformed Data
     ↓
model.pkl
     ↓
Predictions
     ↓
output.csv

The predicted values are added to the input dataset under:
median_house_value

and saved as:
output.csv

## 🌐 Flask Web Application
The machine learning model is deployed through a Flask application.
The Flask backend:
1. Loads model.pkl
2. Loads pipeline.pkl
3. Receives property information from the frontend
4. Creates a Pandas DataFrame
5. Applies the saved preprocessing pipeline
6. Sends the transformed data to the Random Forest model
7. Generates the predicted house value
8. Returns the prediction as JSON
The prediction endpoint is:
POST /predict

## 🖥️ Web Interface
The project contains a frontend built using:
- HTML
- CSS
- JavaScript
Users can enter property information through the web interface.
The frontend sends the information to the Flask /predict endpoint and displays the predicted house price.
🏗️ Application Architecture
                 User
                  │
                  ▼
        ┌──────────────────┐
        │   HTML + CSS UI  │
        └────────┬─────────┘
                 │
                 │ JSON Request
                 ▼
        ┌──────────────────┐
        │   Flask Backend  │
        │     app.py       │
        └────────┬─────────┘
                 │
        ┌────────┴─────────┐
        ▼                  ▼
 pipeline.pkl          model.pkl
        │                  │
        ▼                  ▼
 Preprocessing       Random Forest
        │                  │
        └────────┬─────────┘
                 ▼
          Predicted Price
                 │
                 ▼
               User

## 🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
Pandas	Data manipulation
NumPy	Numerical operations
Scikit-learn	Machine learning and preprocessing
Random Forest	Final prediction model
Joblib	Model persistence
Flask	Backend/API
HTML	Web interface
CSS	Frontend styling
JavaScript	Frontend-backend communication
Jupyter Notebook	ML experimentation
Git & GitHub	Version control


## 📁 Project Structure
California_House_Price_Prediction_model/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
│
├── california_price.py
│
├── HousePrice.ipynb
│
├── Inference.py
│
├── housing.csv
│
├── input.csv
├── input copy.csv
│
├── output.csv
│
├── pipeline.pkl
├── model.pkl
│
├── requirements.txt
│
└── README.md

## 🚀 Installation & Setup
1. Clone the repository
git clone https://github.com/YazdanAhmedData/California_House_Price_Prediction_model.git

2. Navigate into the project
cd California_House_Price_Prediction_model

3. Create a virtual environment
python -m venv .venv

4. Activate the environment
macOS / Linux
source .venv/bin/activate

Windows
.venv\Scripts\activate

5. Install dependencies
pip install -r requirements.txt

🧠 Train the Model
If the trained model files are not available locally, run the training script:
python california_price.py

The script trains the Random Forest model and creates:
model.pkl
pipeline.pkl

The training process also creates the test dataset:
input.csv

▶️ Run the Flask Application
After the model and pipeline are available, start the Flask application:
python app.py

The application runs on:
http://127.0.0.1:5002

Open the address in your browser to use the prediction application.
🔮 Making Predictions
The web application accepts:
Longitude
Latitude
Housing Median Age
Total Rooms
Total Bedrooms
Population
Households
Median Income
Ocean Proximity

The information is sent to the Flask backend and processed using the saved machine learning pipeline.
The final output is an estimated:
Median House Value

## 📌 Key Machine Learning Concepts Demonstrated
This project demonstrates practical knowledge of:
- Supervised Learning
- Regression
- Train/Test Splitting
- Stratified Sampling
- Feature Engineering
- Missing Value Imputation
- Feature Scaling
- One-Hot Encoding
- Column Transformers
- Machine Learning Pipelines
- Linear Regression
- Decision Tree Regression
- Random Forest Regression
- Cross-Validation
- RMSE Evaluation
- Model Persistence
- Model Inference
- REST-style API communication
- Flask Deployment
- Frontend Integration
💡 What This Project Demonstrates
This project goes beyond simply training a machine learning model.
It demonstrates the complete transition from:
Raw Dataset
      ↓
Data Preparation
      ↓
Machine Learning
      ↓
Model Evaluation
      ↓
Model Serialization
      ↓
Backend API
      ↓
Web Interface
      ↓
Real-Time Prediction

This makes the project suitable as a practical Machine Learning / Data Analytics portfolio project.

## 🚀 Future Improvements
Possible improvements include:
- Hyperparameter tuning for Random Forest
- Comparing additional regression algorithms
- Adding model performance visualizations
- Adding prediction confidence/ranges
- Improving frontend validation
- Adding interactive charts
- Deploying the Flask application online
- Adding a database for prediction history
- Adding user authentication
- Creating an API documentation page
- Containerizing the application with Docker
- Deploying the application using a cloud platform
- 
## 👨‍💻 Author
Yazdan Ahmed
Data Analytics & Machine Learning Enthusiast
GitHub:
https://github.com/YazdanAhmedData

## ⭐ Project
If you found this project useful, consider giving the repository a ⭐ on GitHub.
       
