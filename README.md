# California House Price Prediction | Machine Learning & Flask

An end-to-end machine-learning project that predicts California housing values from property and demographic features. The repository covers data preparation, model training, saved model artifacts, inference, and a Flask web interface.

## Objective

Build a repeatable prediction workflow that accepts housing features and returns an estimated median house value. This project demonstrates the journey from a tabular dataset to a model-backed application.

## Workflow

1. **Explore the dataset** and inspect feature types, missing values, and target distribution.
2. **Prepare the data** using preprocessing steps appropriate for numerical and categorical features.
3. **Train and compare models** using a consistent evaluation approach.
4. **Persist the fitted pipeline** so preprocessing at inference time matches training.
5. **Generate predictions** through the inference code.
6. **Serve the workflow** through a Flask application and web interface.

## Technology Stack

- Python
- Pandas and NumPy
- Scikit-learn
- Jupyter Notebook
- Flask
- HTML/CSS templates

## Repository Contents

| File or folder | Purpose |
|---|---|
| `HousePrice.ipynb` | Notebook for exploration/model development |
| `california_price.py` | Supporting model or analysis script |
| `Inference.py` | Prediction/inference workflow |
| `app.py` | Flask application |
| `housing.csv` | Housing dataset |
| `pipeline.pkl` | Serialized pipeline/model artifact |
| `requirements.txt` | Python dependencies |
| `templates/` | HTML templates |
| `static/` | Static web assets |

Check the source files for the exact division of responsibilities and expected input fields.

## Evaluation and Reporting

For a credible regression project, model performance should be reported on held-out data using metrics such as **MAE** and **RMSE**, alongside a baseline comparison. The repository’s actual evaluation outputs should be used for these values; this README does not claim a specific accuracy or error score without verified results.

## Run Locally

1. Clone the repository and enter its folder.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Confirm that the saved pipeline and dataset paths expected by the scripts are present.
5. Start the Flask application using the entry point defined in `app.py` (commonly `python app.py`).
6. Open the local address printed by Flask in your browser.

If your local setup uses a different entry point or port, follow the configuration in `app.py`.

## Important Limitations

- Predictions are estimates, not guaranteed market valuations.
- Dataset coverage and feature quality constrain model performance.
- Performance metrics should be calculated on data not used for fitting.
- The saved pipeline and inference input schema must remain consistent.

## Skills Demonstrated

Regression modelling · Data preprocessing · Feature engineering · Model evaluation · Model persistence · Inference pipelines · Flask deployment · Python

## Author

**Yazdan Ahmed**  
[GitHub Portfolio](https://github.com/YazdanAhmedData)
