# 🫀💔 Heart Disease Predictive Modeling

**Project Overview**

Developed a Decision Tree classification system to predict cardiovascular pathology based on clinical patient features. This project demonstrates the end-to-end ML workflow: from exploratory data analysis (EDA) and data cleaning to model evaluation and optimization strategies.

## Technical Methodology

**Problem Space:** Binomial Classification (Presence vs. Absence of Heart Disease)

**Model Selection:** Utilized a Decision Tree architecture to capture non-linear relationships and feature dependencies common in clinical datasets, providing better performance than independence-based models like Naive Bayes.

**Data Engineering & Pre-processing:**
* Data Integrity: Performed targeted outlier and null-value handling by identifying non-standard missing values in the ca and thal features.
* Feature Selection: Conducted EDA to identify feature distributions (e.g., median age ≈55) and correlations (Resting BP vs. Serum Cholesterol).

**Pipeline Design:** Implemented a 70/30 train-test split to ensure model generalizability and prevent overfitting.

# Scalability & Future Engineering

To transition this from a prototype to a production-grade system, the following architectural improvements are proposed:

**Feature Engineering:** Programmatic creation of interaction terms (e.g., Age×MaxHeartRate) to uncover deeper signal.

**Ensemble Methods:** Implementation of Random Forests or Gradient Boosting (XGBoost) to reduce variance and improve Precision.

**Deployment:** Wrapping the final model in a FastAPI service (as seen in my other projects) for real-time clinical decision support.
