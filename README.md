
# 🏠 California House Price Prediction

An end-to-end **Machine Learning web application** that predicts California house prices based on geographical, demographic, and housing-related features.

The project combines **Python, Pandas, NumPy, Scikit-learn, Random Forest Regression, Flask, HTML, and CSS** to build a complete workflow from data preprocessing and model training to real-time predictions through a web interface.

---

## 🚀 Project Overview

The goal of this project is to build a machine learning model capable of estimating the **median house value** of a California housing district based on multiple input features.

The project includes:

- Data exploration and preprocessing
- Missing-value handling
- Numerical feature preprocessing
- Categorical feature encoding
- Machine Learning model training
- Random Forest Regression
- Model and preprocessing pipeline serialization
- Flask backend
- Interactive web interface
- Real-time house price prediction

---

## 🧠 Machine Learning Workflow

```text
California Housing Dataset
          ↓
    Data Exploration
          ↓
    Data Preprocessing
          ↓
   Train/Test Preparation
          ↓
 Feature Transformation Pipeline
          ↓
 Random Forest Regressor
          ↓
      Model Training
          ↓
      Model Saving
          ↓
       Flask API
          ↓
    Web Application
          ↓
   House Price Prediction
```

---

## 📊 Dataset

The project uses the **California Housing Dataset**, containing information about housing districts in California.

### Features

| Feature | Description |
|---|---|
| `longitude` | Geographic longitude |
| `latitude` | Geographic latitude |
| `housing_median_age` | Median age of houses in the district |
| `total_rooms` | Total number of rooms |
| `total_bedrooms` | Total number of bedrooms |
| `population` | Population of the district |
| `households` | Number of households |
| `median_income` | Median income of households |
| `ocean_proximity` | Location relative to the ocean |

### Target Variable

```text
median_house_value
```

The model uses the above features to estimate the median house value of a district.

---

## 🤖 Machine Learning Model

The project uses a:

### Random Forest Regressor

Random Forest Regression was selected to model the relationship between the housing features and the target house value.

The preprocessing workflow uses a Scikit-learn `ColumnTransformer` pipeline that handles:

- Missing numerical values
- Numerical feature scaling
- Categorical feature encoding
- Unknown categorical values

The categorical feature:

```text
ocean_proximity
```

is transformed using One-Hot Encoding.

---

## 🌐 Web Application

The trained model is integrated into a Flask web application.

Users can enter housing information through the web interface and receive a predicted house price.

### Application Flow

```text
User enters property information
            ↓
       Flask API
            ↓
   Input preprocessing
            ↓
   Random Forest Model
            ↓
    Predicted house value
            ↓
       Web interface
```

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Random Forest Regression

### Data Processing
- Pandas
- NumPy

### Web Development
- Flask
- HTML
- CSS
- JavaScript

### Model Serialization
- Joblib

### Development Tools
- Jupyter Notebook
- VS Code
- Git & GitHub

---

## 📁 Project Structure

```text
California_House_Price_Prediction_model/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── HousePrice.ipynb
├── Inference.py
├── california_price.py
├── app.py
│
├── housing.csv
├── input.csv
├── input copy.csv
├── output.csv
│
├── pipeline.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

> `model.pkl` is intentionally excluded from the GitHub repository because the trained model file exceeds GitHub's standard 100 MB file limit.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YazdanAhmedData/California_House_Price_Prediction_model.git
```

### 2. Navigate to the project

```bash
cd California_House_Price_Prediction_model
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

#### macOS / Linux

```bash
source .venv/bin/activate
```

#### Windows

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Flask application:

```bash
python app.py
```

The application will run locally at:

```text
http://127.0.0.1:5002
```

Open the address in your browser to access the application.

---

## 🔮 Making Predictions

The Flask application accepts housing information through the `/predict` endpoint.

Example input:

```json
{
    "longitude": -122.23,
    "latitude": 37.88,
    "housing_median_age": 41,
    "total_rooms": 880,
    "total_bedrooms": 129,
    "population": 322,
    "households": 126,
    "median_income": 8.3252,
    "ocean_proximity": "NEAR BAY"
}
```

The API returns the predicted house value.

---

## 📌 Example Prediction

For a given set of housing characteristics, the application produces an estimated median house value such as:

```text
Predicted House Value: ₹4,61,79,101.95
```

> The displayed value depends on the input data and the trained model.

---

## 📚 Project Files

### `HousePrice.ipynb`
Contains the machine learning experimentation, data analysis, preprocessing, and model development workflow.

### `california_price.py`
Contains the main model training workflow.

### `Inference.py`
Used for making predictions with the trained model.

### `app.py`
Flask backend responsible for loading the model, receiving user input, preprocessing the data, and returning predictions.

### `index.html`
Frontend interface where users enter housing information.

### `style.css`
Styling for the web application.

### `pipeline.pkl`
Saved Scikit-learn preprocessing pipeline.

### `housing.csv`
California housing dataset used for the project.

---

## 🎯 Key Learning Outcomes

This project helped demonstrate an end-to-end Machine Learning workflow including:

- Data preprocessing
- Handling missing values
- Feature transformation
- Categorical encoding
- Machine Learning model training
- Random Forest Regression
- Model serialization
- Building a REST-style prediction endpoint
- Connecting a Machine Learning model with a web application
- Frontend and backend integration
- Deployable project structure
- Git and GitHub version control

---

## 🔮 Future Improvements

Possible improvements include:

- Hyperparameter tuning
- Model comparison with Gradient Boosting, XGBoost, and other regressors
- Model performance dashboard
- Prediction confidence/range
- Better visualization of California housing data
- Cloud deployment
- REST API documentation
- Model versioning
- Automated CI/CD pipeline
- Hosting the trained model separately using cloud storage or Git LFS

---

## 👨‍💻 Author

**Yazdan Ahmed**

B.Com (Accounts Hons) Student | Data Analytics & Machine Learning Enthusiast

### GitHub

[https://github.com/YazdanAhmedData](https://github.com/YazdanAhmedData)

---

## ⭐ Project

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.
