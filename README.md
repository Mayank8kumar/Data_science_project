# 🧠 Student Score Prediction - ML Pipeline Project

This project demonstrates a structured and production-ready machine learning pipeline built using Python for predicting **students' math scores** based on demographic and academic factors. It covers everything from data ingestion to model training — all following standard MLOps practices.

---

## 🚀 Project Overview

This project is a **regression-based ML system** that simulates how machine learning is deployed in real-world production environments — not just a notebook-based prototype. It is modular, scalable, and includes logging, exception handling, pipeline saving, and model evaluation logic.

---

## 🔧 Tech Stack & Libraries

| Component         | Technology                        |
| ----------------- | --------------------------------- |
| Language          | Python 3.8+                       |
| Data Processing   | Pandas, NumPy                     |
| Model Training    | scikit-learn, XGBoost, CatBoost   |
| Pipeline Handling | Scikit-learn Pipelines            |
| Logging & Errors  | Python logging, Custom Exceptions |
| Model Persistence | Pickle (`.pkl` files)             |

---

## 🧩 Project Structure

```
Data Science/
│
├── app.py                             # Main entry point
├── artifacts/                         # Stores transformed datasets and model .pkl files
├── logs/                              # Automatically created log files
├── notebook/data/raw.csv              # Input CSV data
├── src/
│   └── Data_science/
│       ├── components/
│       │   ├── data_ingestion.py      # Reads and splits data
│       │   ├── data_transformation.py # Preprocessing pipelines
│       │   └── model_trainer.py       # Trains and selects best model
│       ├── utils.py                   # Utility functions (pickle, SQL read)
│       ├── logger.py                  # Logging logic
│       └── exceptions.py              # Custom exception handling
```

---

## 📊 Features Implemented

✅ **Data Ingestion**

* Reads `.csv` or SQL data
* Splits into train/test
* Saves raw, train, and test data in `artifacts/`

✅ **Data Transformation**

* Handles missing values with `SimpleImputer`
* Scales numerical & encodes categorical columns
* Saves preprocessing pipeline as `.pkl`

✅ **Model Training**

* Trains multiple regressors (`RandomForest`, `XGBoost`, `CatBoost`, etc.)
* Uses hyperparameter tuning for best results
* Logs model performance (R² score)
* Saves the best model as `.pkl`

✅ **Production-Ready Engineering**

* Modular code structure
* Logging for debugging
* Error handling via custom exceptions
* Configurable file paths using `dataclass`

---

## ⚙️ How to Run the Project Locally

1. **Clone the repo**

```bash
git clone <your_repo_url>
cd Data\ Science
```

2. **Create a virtual environment**

```bash
python -m venv env
env\Scripts\activate      # For Windows
```

3. **Install requirements**
   Make sure all dependencies like `pandas`, `scikit-learn`, `xgboost`, `catboost`, etc. are installed.

```bash
pip install -r requirements.txt
```

4. **Place your dataset**
   Put the `raw.csv` file inside `notebook/data/` directory.

5. **Run the pipeline**

```bash
python app.py
```

---

## 📁 Output Artifacts

* `artifacts/train.csv`, `test.csv`, `raw.csv`: Data splits
* `artifacts/preprocessor.pkl`: Preprocessing pipeline
* `artifacts/model.pkl`: Best trained model

---

## 🧠 Skills Demonstrated

* Structured ML project architecture (beyond notebooks)
* Data preprocessing using pipelines
* Hyperparameter tuning
* Logging & debugging
* Exception handling & code modularity
* Saving and loading models/pipelines

---

## 📌 To Do (Optional Enhancements)

* Add automated tests
* Add model explainability (e.g., SHAP)
* Create a Flask API for prediction
* Deploy via Docker/Render/Streamlit

---

## 🤝 Credits

Project developed as a structured ML engineering practice based on standard industry templates (e.g., used in internship projects or guided mentorships).

---

## 🪪 License

This project is for educational purposes and does not currently include a license file.
