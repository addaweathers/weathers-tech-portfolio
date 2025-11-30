📧 Spam E-mail Detection using XGBoost

This project implements a Spam E-mail Detection model using the XGBoost algorithm. It showcases a complete machine learning workflow, including Exploratory Data Analysis (EDA), feature engineering from unstructured text data, handling class imbalance, model training, and performance evaluation.

✨ Key Project Highlights & Skills Showcased

    Exploratory Data Analysis (EDA): Identified and characterized the dataset, including the detection of class imbalance.

    Data Preprocessing & Feature Engineering: Developed both heuristic-based and unsupervised learning-based features from raw text.

        Text Feature Engineering: Applied techniques to extract features from e-mail content (e.g., word counts, punctuation).

        Feature Extraction with K-Means Clustering: Used k-means clustering to discover non-intuitive, latent features from the text data, guided by the silhouette score for optimal cluster selection.

    Handling Class Imbalance: Justified the selection of the XGBoost model due to its general robustness and better performance on imbalanced datasets compared to standard models.

    Model Building & Optimization: Iterative model development led to a final model with 97% accuracy.

    Python Stack Proficiency: Demonstrated expertise in libraries like Pandas, Numpy, Scikit-learn, and XGBoost.

📊 Dataset Overview

The dataset contained 5,728 e-mails with the following two columns:

    email: The full text content of the e-mail.

    spam: The target variable, where 0 = Not Spam and 1 = Spam.

Class Imbalance

Initial EDA revealed a significant class imbalance:

    Total E-mails: 5,728

    Spam E-mails (1): 1,368

    Non-Spam E-mails (0): 4,360

This imbalance (≈ 24% of the data is spam) was a key factor in the choice of the XGBoost algorithm.

🛠️ Feature Engineering Strategy

The project involved a two-stage approach to feature engineering to transform the raw e-mail text into numerical features for the model.

1. Intuition/Heuristic-Based Features

Based on the hypothesis that spam e-mails often contain urgent or intrusive language, the following features were engineered:

    exclamation_marks: The count of exclamation marks (!), intended to capture a sense of urgency.

    question_marks: The count of question marks (?), intended to capture queries that ask for personal information.

    flagged_words A count of specific urgency-related keywords (e.g., "failure", "last chance").

2. K-Means Clustering for Latent Features

Recognizing that intuition-based features might be insufficient, K-Means Clustering was applied to the vectorized e-mail text (using techniques like TF-IDF or Word2Vec) to uncover underlying structures in the data.

    Optimal Cluster Selection: The silhouette score was used to determine the best number of clusters. The score indicated that 2 was the optimal number of clusters.

    Feature Integration: The cluster labels from the K-Means analysis were added to the dataset as new, non-intuitive features for the XGBoost model.

🚀 Model Development & Results

Iteration 1: Initial Model (Heuristic Features Only)

    Model: XGBoost

    Features: Only the intuition-based features (exclamation_marks, question_marks, flagged_words).

    Performance: The model only detected about 68% of the spam e-mails. This highlighted the need for more powerful features, justifying the second stage of feature engineering.

Iteration 2: Final Model (Full Feature Set)

The model was retrained using all engineered features, including the new features derived from K-Means clustering and crucially, the text data itself (following a fix to an initial coding error where the text features were unintentionally excluded).

    Model: XGBoost Classifier

    Features: Full text features + Intuition-based features + K-Means cluster labels.

    Final Performance: The comprehensive feature set and robust model resulted in a significant performance jump.
    
This final result demonstrates the power of combining heuristic and unsupervised feature engineering with a strong classification algorithm like XGBoost.
