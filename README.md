# 🏠 California House Price Prediction | Machine Learning & Flask

**Portfolio case study · Regression · Feature engineering · Model serving**

## Executive Summary
This project develops a machine-learning workflow to estimate California median house values from location, housing, household and income features. It covers exploratory analysis, train/test splitting, preprocessing of numerical and categorical data, model preparation and a Flask interface for serving predictions.

The source notebook loads **20,640 housing records** and includes features such as longitude, latitude, housing median age, rooms, bedrooms, population, households, median income and ocean proximity.

## Business Problem
Property values depend on multiple interacting factors, and a manual estimate can be inconsistent. A regression model can provide a repeatable baseline estimate from known property and neighbourhood attributes. This prototype demonstrates how data preparation and a trained pipeline can be connected to an application interface.

**Intended use:** educational estimation and model demonstration. It is not a certified appraisal, financial recommendation, or a live real-estate valuation service.

## Data & Features
| Feature group | Examples | Analytical role |
|---|---|---|
| Geography | Longitude, latitude, ocean proximity | Capture location-related patterns |
| Housing stock | Median age, total rooms, total bedrooms | Describe local housing characteristics |
| Population | Population, households | Describe community scale |
| Income | Median income | Socioeconomic signal in the source dataset |
| Target | Median house value | Value the model learns to estimate |

## Workflow
1. Load and inspect the California housing dataset.
2. Explore distributions and missing values.
3. Create a reproducible train/test split; the notebook uses a seeded split and also explores income-category stratification.
4. Impute missing numerical values and scale/transform numerical fields as appropriate.
5. Encode `ocean_proximity` as categorical features.
6. Assemble preprocessing into a pipeline so training and inference use consistent transformations.
7. Train a regression model and persist the pipeline.
8. Use inference code and Flask to accept input features and return a prediction.

## Business Questions
- How do location and income relate to observed median house values?
- Which input fields contribute useful predictive signal?
- How well does the model generalise to unseen data?
- Can the same preprocessing be applied consistently in a deployed prediction flow?

## KPI & Model Evaluation Scorecard
| Metric | What it measures | Why recruiters should care |
|---|---|---|
| MAE | Mean absolute prediction error | Typical error magnitude in target units |
| RMSE | Penalises larger errors more strongly | Highlights costly large misses |
| R² | Variation explained relative to a baseline | Useful context, but not enough alone |
| Baseline comparison | Model vs simple predictor such as training-set median | Shows whether complexity adds value |
| Train/test gap | Difference in performance across splits | Helps diagnose overfitting |

The current notebook content does not provide a clearly documented, verified final MAE/RMSE/R² scorecard. Those figures should be calculated from held-out predictions before claiming a model accuracy.

## Business Interpretation
- **Location matters:** geographic features allow the model to learn spatial patterns, but model performance should be checked across locations rather than only in aggregate.
- **Income and housing characteristics provide context:** feature importance or error analysis can help explain which fields are useful, while avoiding causal claims.
- **Large prediction errors matter:** report examples and error distributions, not just a single score.
- **Deployment is part of the project:** preprocessing and inference must use the same feature order, encodings and units as training.

These are interpretation directions supported by the project design; do not describe a feature as the “most important” until the trained model's actual outputs have been evaluated.

## Tools & Technologies
Python · Pandas · NumPy · Scikit-learn · Jupyter Notebook · Flask · HTML/CSS · Pickle/model persistence

## Repository Guide
| File / folder | Purpose |
|---|---|
| `HousePrice.ipynb` | Data exploration and model development |
| `california_price.py` | Supporting model/analysis script |
| `Inference.py` | Prediction workflow |
| `app.py` | Flask application |
| `housing.csv` | Dataset |
| `pipeline.pkl` | Saved pipeline/model artifact |
| `requirements.txt` | Dependencies |
| `templates/` | HTML templates |
| `static/` | Static assets |

## Run Locally
1. Clone the repository and open the project folder.
2. Create and activate a virtual environment.
3. Install dependencies with `pip install -r requirements.txt`.
4. Confirm the dataset and saved pipeline paths expected by the scripts.
5. Start the Flask app with the entry point in `app.py` (commonly `python app.py`).
6. Open the local URL printed in the terminal and test valid input values.

## Limitations & Responsible Use
- Dataset values represent historical regional median values, not current individual property prices.
- Predictions can be biased by geography, data coverage and changes in market conditions.
- A model score should come from a held-out test set; avoid reporting training performance as generalisation.
- Do not expose pickle files from untrusted sources; serialized Python objects can be unsafe to load.
- Keep model input validation and error handling in the application.

## Next Steps
- Add a final metrics table with baseline, MAE, RMSE and R².
- Add residual plots and error breakdowns by income band and ocean proximity.
- Validate the Flask form against missing, extreme and malformed inputs.
- Pin package versions and include a small sample request/response.

## Author
**Yazdan Ahmed** · [GitHub Portfolio](https://github.com/YazdanAhmedData)
