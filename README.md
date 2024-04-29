# Emotional Dysregulation Project
## Machine Learning Model Optimization Project

## Project Overview
This project aims to optimize machine learning models for predicting outcomes based on the CASIS dataset. It uses various classification algorithms such as Logistic Regression, Support Vector Machines (SVM), Random Forest, and K-Nearest Neighbors (KNN) to model and predict the specified outcomes. The project applies RandomizedSearchCV to fine-tune the models' hyperparameters and improve their performance.

## Data Source
The dataset is loaded from an online CSV file, which can be accessed via this link:
[https://raw.githubusercontent.com/jserrataylor/CASIS/main/casis_datasets.csv]

## Features
The dataset includes the following features which are considered for model training:
- Difficulty Sleeping (`Tengodificultadesconelsueño`)
- Considering Harm to Others (`Consideréseriamentelastimaraotrapersona`)
- Need to Reduce Alcohol/Drug Use (`Sentílanecesidaddereducirelusodebebidasalcóholicasyodrogas`)
- Undergoing Counseling or Psychotherapy (`Asistíaconsejeríaopsicoterapiaporasuntosrelacionadosconmisalud`)
- Experiencing Panic Attacks (`Hetenidoataquesdepánicoepisodiosdeansiedadseveraqueduranalreded`)
- Concerns Related to Unhealthy Diet (`Tengopreocupacionesrelacionadasamialimentacióndietasnosaludable`)
- Sexual Contacts Without Consent (`Hetenidocontactossexualesuotrasexperienciasdeíndolesexualsindes`)

## Data Preprocessing
Data preprocessing steps include:
- Converting data to numeric values, handling non-convertible cases.
- Dropping rows with any missing values.
- Applying SMOTE for balancing the classes in the dataset.

## Model Optimization
RandomizedSearchCV is used for optimizing model parameters with the following settings:
- Iterations: 100
- Cross-validation folds: 6
- Scoring metric: Recall

## Results
Results for each model are summarized in terms of accuracy, precision, recall, and F1 score. The best parameters found for each model are also documented.

## Usage
To run the models:
1. Ensure Python 3 and necessary libraries (`pandas`, `scikit-learn`, `imblearn`, `joblib`) are installed.
2. Execute the script to train the models, perform hyperparameter tuning, and evaluate the results.

## Saving Models
The best models are saved using `joblib` into `.pkl` files for later use or deployment.

## Conclusion
This project showcases the application of different machine learning techniques to predict outcomes accurately using hyperparameter tuning to enhance model performance.

