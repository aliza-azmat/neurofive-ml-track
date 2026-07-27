# Neurofive ML Internship

This repository contains the tasks I completed during my Machine Learning Internship at Neurofive Solutions.

## 📌 Task 1: Titanic Dataset Exploration
- Loaded and explored the Titanic dataset
- Performed Exploratory Data Analysis (EDA)
- Examined dataset structure and summary statistics

## 📌 Task 2: Data Cleaning and Visualization
- Handled missing values using appropriate techniques
- Detected outliers using a boxplot
- Created visualizations including:
  - Histogram
  - Boxplot
  - Bar Chart
  - Correlation Heatmap
- Analyzed important insights from the dataset

## 📌 Task 3: Logistic Regression
- Encoded categorical variables
- Split the dataset into training and testing sets
- Built a Logistic Regression classification model
- Predicted passenger survival
- Evaluated the model using:
  - Accuracy Score
  - Confusion Matrix

## 📌 Task 4: Linear Regression
- Used the California Housing dataset from Scikit-learn
- Selected important features for prediction
- Built a Linear Regression model
- Predicted house prices
- Evaluated model performance using:
  - RMSE (Root Mean Squared Error)
  - R² Score (Coefficient of Determination)
- Visualized Actual vs Predicted house prices using a scatter plot
- Interpreted the R² score in simple language

## 📌 Task 5: Model Evaluation and Hyperparameter Tuning

### Objective
Evaluate and improve the Logistic Regression model built on the Titanic dataset.

### Tasks Completed
- Revisited the Logistic Regression model
- Evaluated the model using Accuracy, Precision, Recall, and F1-score
- Generated a Classification Report
- Explained why accuracy alone can be misleading for imbalanced datasets
- Applied GridSearchCV for hyperparameter tuning
- Tuned the hyperparameters:
  - C = 1
  - Solver = liblinear
- Compared the original and tuned model performance

### Results
- Original Accuracy: **81.01%**
- Tuned Accuracy: **78.21%**
- Best Parameters:
- C = 1
  - Solver = liblinear

## 📌 Task 6: Customer Churn Prediction

### Objective
Predict customer churn using machine learning and compare the performance of two classification models.

### Tasks Completed
- Loaded and explored the Telco Customer Churn dataset
- Cleaned and preprocessed the data
- Encoded categorical variables
- Trained Logistic Regression and Decision Tree models
- Compared model performance using accuracy
- Identified the most important features affecting customer churn
- Summarized business insights based on the results

### Results
- Logistic Regression Accuracy: **81.83%**
- Decision Tree Accuracy: **72.89%**

### Top Important Features
- Contract
- MonthlyCharges
- customerID *(identified by the model, though it is a unique identifier and would typically be excluded in practice)*

## 📌 Task 7: Machine Learning Pipeline and Feature Engineering

### Objective
Build an end-to-end machine learning pipeline using the Titanic dataset by combining preprocessing and model training into a single workflow. Apply feature engineering and compare model performance before and after adding new features.

### Tasks Completed
- Loaded and explored the Titanic dataset
- Cleaned missing values
- Selected features and target variable
- Split the dataset into training and testing sets
- Identified numerical and categorical features
- Built a ColumnTransformer for preprocessing
- Created a Machine Learning Pipeline using Logistic Regression
- Trained and evaluated the pipeline
- Created two engineered features:
  - FamilySize
  - IsAlone
- Compared model performance before and after feature engineering
- Saved the trained pipeline using Joblib

### Results

**Original Pipeline Accuracy:** 81.01%

**Pipeline Accuracy After Feature Engineering:** 79.89%

### Key Learning

This task demonstrated how machine learning pipelines simplify preprocessing and model training into a single workflow. It also highlighted that feature engineering should always be evaluated, as newly created features may improve, maintain, or reduce model performance depending on the dataset.

### Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- ColumnTransformer
- Pipeline
- Logistic Regression
- Joblib
- Google Colab

## 🎯 Internship Skills Learned
- Data Exploration
- Data Cleaning
- Data Visualization
- Feature Selection
- Classification
- Regression
- Model Evaluation
- Machine Learning Fundamentals

Thank you to **Neurofive Solutions** for providing this valuable learning opportunity and helping me strengthen my practical Machine Learning skills.
