from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import numpy as np
import pandas as pd
from typing import List
import re
# Easier to work with HTML file
from fastapi.responses import HTMLResponse

# Initialize FastAPI app
app = FastAPI(
    title="Spam Email Detector API",
    description="API for detecting spam emails using XGBoost",
    version="1.0.0"
)

# Add CORS middleware to allow browser requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Load the trained model, vectorizer, and clustering model
try:
    model = joblib.load("optimized_spam_detector_xgb_model.joblib")
    vectorizer = joblib.load("tfidf_vectorizer.joblib")

    # Try to load cluster model
    try:
        cluster_model = joblib.load("cluster_model.joblib")
        print(f"✓ Cluster model loaded")
    except:
        cluster_model = None
        print(f"⚠ Cluster model not found - using default cluster 0")

    print(f"✓ Models loaded successfully")
    print(f"✓ Model expects {model.n_features_in_} features")
except Exception as e:
    print(f"Error loading models: {e}")
    model = None
    vectorizer = None
    cluster_model = None


# Feature engineering functions
def extract_email_features(text):
    """
    Extract numerical features from email text to match training data
    """
    features = {}

    # Count exclamation marks
    features['exclamation_marks'] = text.count('!')

    # Count question marks
    features['question_marks'] = text.count('?')

    # Count flagged spam words (common spam indicators)
    spam_words = [
        'free', 'winner', 'cash', 'prize', 'click', 'urgent', 'limited',
        'offer', 'buy', 'sale', 'discount', 'guaranteed', 'money', 'credit',
        'viagra', 'lottery', 'congratulations', 'act now', 'call now'
    ]
    text_lower = text.lower()
    features['flagged_words'] = sum(1 for word in spam_words if word in text_lower)

    # Email length feature
    features['email_length'] = len(text)

    # Placeholder cluster - we'll need to load the actual cluster model
    # For now, set to 0 (you'll need to add proper clustering)
    features['cluster'] = 0

    return features


def prepare_features(text, num_clusters=2):
    """
    Combine features in the EXACT order as training:
    basic (3) + cluster_dummies (2) + TF-IDF (1000) = 1005
    """
    # Get TF-IDF features (1000 features)
    tfidf_features = vectorizer.transform([text])
    tfidf_dense = tfidf_features.toarray()

    # Get basic features (3 features)
    email_features = extract_email_features(text)
    basic_features = np.array([[
        email_features['exclamation_marks'],
        email_features['question_marks'],
        email_features['flagged_words']
    ]])

    # Get cluster assignment
    if cluster_model is not None:
        # Use actual cluster model to predict cluster
        cluster_id = cluster_model.predict(tfidf_features)[0]
    else:
        # Default to cluster 0 if no model
        cluster_id = 0

    # Create cluster dummy variables (2 features)
    cluster_dummies = np.zeros((1, num_clusters))
    if cluster_id < num_clusters:
        cluster_dummies[0, cluster_id] = 1

    # Combine in correct order: basic + cluster_dummies + TF-IDF
    combined_features = np.hstack([basic_features, cluster_dummies, tfidf_dense])

    return combined_features


# Request/Response models
class EmailRequest(BaseModel):
    text: str = Field(..., description="Email text to classify", min_length=1)


class EmailBatchRequest(BaseModel):
    emails: List[str] = Field(..., description="List of email texts to classify")


class PredictionResponse(BaseModel):
    text: str
    is_spam: bool
    spam_probability: float
    confidence: float
    features: dict = None


class BatchPredictionResponse(BaseModel):
    predictions: List[PredictionResponse]


# Health check endpoint
@app.get("/")
def read_root():
    return {
        "message": "Spam Email Detector API is running",
        "status": "healthy" if model and vectorizer else "error",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    if model is None or vectorizer is None:
        raise HTTPException(status_code=503, detail="Models not loaded")
    return {"status": "healthy", "models_loaded": True}


# Single email prediction
@app.post("/predict", response_model=PredictionResponse)
def predict_email(request: EmailRequest):
    """
    Classify a single email as spam or not spam
    """
    if model is None or vectorizer is None:
        raise HTTPException(status_code=503, detail="Models not loaded")

    try:
        # Prepare features (TF-IDF + engineered)
        email_features_combined = prepare_features(request.text)

        # Get prediction and probability
        prediction = model.predict(email_features_combined)[0]
        probabilities = model.predict_proba(email_features_combined)[0]

        # Extract spam probability
        spam_prob = float(probabilities[1])
        confidence = float(max(probabilities))

        # Get feature values for debugging
        feature_dict = extract_email_features(request.text)

        return PredictionResponse(
            text=request.text[:100] + "..." if len(request.text) > 100 else request.text,
            is_spam=bool(prediction),
            spam_probability=spam_prob,
            confidence=confidence,
            features=feature_dict
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


# Batch prediction
@app.post("/predict/batch", response_model=BatchPredictionResponse)
def predict_batch(request: EmailBatchRequest):
    """
    Classify multiple emails at once
    """
    if model is None or vectorizer is None:
        raise HTTPException(status_code=503, detail="Models not loaded")

    if len(request.emails) > 100:
        raise HTTPException(status_code=400, detail="Maximum 100 emails per batch")

    try:
        results = []

        for email in request.emails:
            # Prepare features for each email
            email_features_combined = prepare_features(email)

            # Get prediction and probability
            prediction = model.predict(email_features_combined)[0]
            probabilities = model.predict_proba(email_features_combined)[0]

            spam_prob = float(probabilities[1])
            confidence = float(max(probabilities))

            results.append(PredictionResponse(
                text=email[:100] + "..." if len(email) > 100 else email,
                is_spam=bool(prediction),
                spam_probability=spam_prob,
                confidence=confidence
            ))

        return BatchPredictionResponse(predictions=results)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Batch prediction error: {str(e)}")


# Model info endpoint
@app.get("/model/info")
def get_model_info():
    """
    Get information about the loaded model
    """
    if model is None or vectorizer is None:
        raise HTTPException(status_code=503, detail="Models not loaded")

    info = {
        "model_type": type(model).__name__,
        "vectorizer_type": type(vectorizer).__name__,
        "expected_features": model.n_features_in_,
        "tfidf_features": len(vectorizer.vocabulary_) if hasattr(vectorizer, 'vocabulary_') else None,
        "engineered_features": ["exclamation_marks", "question_marks", "flagged_words", "email_length", "cluster"]
    }

    if hasattr(model, 'feature_names_in_'):
        info["feature_names"] = model.feature_names_in_.tolist()

    return info

# Adding before univorn block
@app.get("/", response_class=HTMLResponse)
async def read_index():
    try:
        with open("spam_checker.html", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "<h1>Error: spam_checker.html not found.</h1>"

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
