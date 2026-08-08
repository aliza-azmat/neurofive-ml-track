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

## 📌 Task 8: Ensemble Learning with Random Forest and XGBoost

### Objective
Train and compare ensemble machine learning models using the Titanic dataset. The performance of Random Forest and XGBoost was compared with Logistic Regression as the baseline single model.

### Tasks Completed
- Installed and imported XGBoost
- Loaded and explored the Titanic dataset
- Handled missing values
- Removed unnecessary columns
- Converted categorical features into numerical values
- Split the dataset into training and testing sets
- Trained and evaluated a Logistic Regression baseline model
- Trained and evaluated a Random Forest Classifier
- Trained and evaluated an XGBoost Classifier
- Created a model performance comparison table
- Plotted feature importances for Random Forest
- Plotted feature importances for XGBoost
- Compared the most important features identified by both models
- Explained the difference between Random Forest and XGBoost

### Model Performance Comparison

| Model | Metric | Score |
|---|---|---:|
| Logistic Regression | Accuracy | 80.45% |
| Random Forest | Accuracy | 82.68% |
| XGBoost | Accuracy | 78.21% |

### Feature Importance Comparison

- **Random Forest:** Fare, Sex, and Age were the three most important features.
- **XGBoost:** Sex, Pclass, and Embarked were the three most important features.

### Key Learning

Random Forest achieved the highest accuracy of **82.68%** in this experiment. The results showed that ensemble models can provide strong predictions, but performance depends on the dataset, preprocessing method, and model settings. The feature-importance analysis also showed that different ensemble models may assign importance differently to the same input features.

## 📌 Task 9: Handling Imbalanced Data

### Objective
Analyze and handle class imbalance in the Telco Customer Churn dataset and compare model performance before and after applying a balancing technique.

### Dataset
Telco Customer Churn Dataset

The target variable was `Churn`, where:
- `0` = No Churn
- `1` = Churn

### Class Distribution

| Class | Count | Percentage |
|---|---:|---:|
| No Churn | 5,174 | 73.46% |
| Churn | 1,869 | 26.54% |

The dataset is imbalanced because the majority class is significantly larger than the minority class.

### Technique Used

`class_weight="balanced"` was applied to Logistic Regression to give greater importance to the minority class during training.

### Model Performance

| Metric | Before Balancing | After Balancing |
|---|---:|---:|
| Accuracy | 80.34% | 73.88% |
| Precision | 65.20% | 50.51% |
| Recall | 55.61% | 78.88% |
| F1-Score | 60.03% | 61.59% |

### Key Findings

After applying class weighting, Recall increased significantly from **55.61% to 78.88%**, meaning the balanced model identified a much larger proportion of customers who actually churned. The F1-score also improved from **60.03% to 61.59%**.

Although Accuracy decreased from **80.34% to 73.88%**, this does not indicate that the balanced model was necessarily worse. For imbalanced datasets, accuracy can be misleading because a model can achieve high accuracy by favoring the majority class.

### Why Accuracy Can Be Misleading

Since 73.46% of customers belong to the majority `No Churn` class, a model can achieve relatively high accuracy by mostly predicting the majority class while failing to identify many churned customers. Therefore, Precision, Recall, and F1-score are more informative metrics for evaluating performance on the minority class.

## 📌 Task 10: Deploying a Machine Learning Model

### Objective
Deploy the best-performing model from previous tasks as an interactive Streamlit web application.

### Model Used
Random Forest Classifier

The Random Forest model from Task 8 was selected for deployment because it achieved the highest accuracy among the models compared in that task.

**Random Forest Accuracy: 82.68%**

### Dataset
Titanic Survival Dataset

### Features Used
- Pclass
- Sex
- Age
- SibSp
- Parch
- Fare
- Embarked

### Application
The Streamlit application allows users to enter Titanic passenger information and receive a predicted survival outcome from the trained Random Forest model.

### Deployment
The application was deployed using Streamlit Community Cloud.

### Project Files
- `app.py` – Streamlit application
- `titanic_random_forest.pkl` – Saved Random Forest model
- `sex_encoder.pkl` – Saved Sex encoder
- `embarked_encoder.pkl` – Saved Embarked encoder
- `requirements.txt` – Required Python libraries
- `Task_10_Deploying_Titanic_RandomForest.ipynb` – Task notebook

### Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier
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
