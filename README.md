Goal: To develop and evaluate a Decision Tree classification model using RapidMiner to predict the presence or absence of heart disease based on patient clinical features.

---

Data Source & URL: Heart Disease Dataset from Kaggle -- https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

The dataset contains 303 patient records and 14 features. 

---

Methodology: I chose a Decision Tree for the following reasons. 

	1. Decision Trees work for classification problems. The presence or absence of heart disease is a binomial classification problem. 

	2. It is not uncommon for relationships to exist within health data. A Naive Bayes model, for example, assumes no relationship between variables 		 and may not work as effectively. 

To pre-process the data, missing values were removed. 4 in the "ca" column and 0 in the "thal" column as missing, since typical values are 0-3 for "ca" and 1-3 for "thal." 

EDA revealed that the patient population was slightly older (median age ≈55), and a weak positive correlation exists between resting blood pressure and serum cholesterol. This EDA informed feature selection and the understanding of the raw data distribution.

The data was split into 70% training data and 30% testing sets. The model was scored using Classification Accuracy and a Confusion Matrix. 

---

Model and Insights: The model achieved an overall Accuracy of 93%. However, the Precision of 89% indicates a need for caution, as a higher number of False Positives means the model would incorrectly diagnose a healthy patient with heart disease.

Future steps to improve Precision would include implementing Feature Engineering (e.g., creating interaction terms like Age × Max Heart Rate) and exploring more complex ensemble methods like Random Forests or Gradient Boosting.
