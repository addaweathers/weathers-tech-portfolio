# 🛡️ Spam Email Detector API

A machine learning-powered REST API that classifies emails as spam or legitimate using XGBoost and Natural Language Processing.

## 🎯 Project Overview

This API deployment project is built on top of my spam E-mail Detector Using XGBoost machine learning model.  It demonstrates:
- **Model Deployment** from Jupyter notebooks to production API
- **XGBoost classifier** trained on 5,728 emails with 95%+ accuracy
- **TF-IDF vectorization** for text feature extraction
- **K-Means clustering** for enhanced pattern recognition
- **FastAPI** for high-performance REST API
- **Interactive web interface** for non-technical users

## 🚀 Features

- Real-time spam detection with confidence scores
- Batch processing support for multiple emails
- Feature analysis (exclamation marks, spam keywords, etc.)
- RESTful API with automatic documentation
- User-friendly web interface
- 95%+ accuracy on test data

## 📊 Model Performance

- **Algorithm**: XGBoost Classifier
- **Features**: 1,005 total
  - 1,000 TF-IDF features
  - 3 text-based features
  - 2 cluster features
- **Training Data**: 5,728 emails
- **Accuracy**: 95%

## 🛠️ Technology Stack

- **Backend**: FastAPI, Python 3.12
- **ML Libraries**: scikit-learn, XGBoost
- **NLP**: TF-IDF Vectorization
- **Deployment**: Uvicorn ASGI server
- **Frontend**: Vanilla JavaScript, HTML5, CSS3

## 📦 Installation

1. Clone the repository:
```bash
git clone
cd FastAPI
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

## 💻 Usage

### Web Interface

1. Open `spam_checker.html` in your browser
2. Paste any email text
3. Click "Check Email" to see results

### API Documentation

Visit `http://localhost:8000/docs` for interactive API documentation (Swagger UI)

### API Endpoints

**POST /predict** - Classify a single email
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "Your email content here"}'
```

**POST /predict/batch** - Classify multiple emails
```bash
curl -X POST "http://localhost:8000/predict/batch" \
  -H "Content-Type: application/json" \
  -d '{"emails": ["Email 1", "Email 2"]}'
```

**GET /health** - Check API health
```bash
curl http://localhost:8000/health
```

### Example Response

```json
{
  "text": "CONGRATULATIONS! You won $1,000,000!",
  "is_spam": true,
  "spam_probability": 0.95,
  "confidence": 0.95,
  "features": {
    "exclamation_marks": 2,
    "question_marks": 0,
    "flagged_words": 3
  }
}
```

## 🧪 Testing

Run the test suite:
```bash
python test_api.py
```

## 📁 Project Structure

```
FastAPI/
├── main.py                                    # FastAPI application
├── spam_checker.html                          # Web interface
├── requirements.txt                           # Python dependencies
├── test_api.py                               # API tests
├── optimized_spam_detector_xgb_model.joblib  # Trained model
├── tfidf_vectorizer.joblib                   # Text vectorizer
├── cluster_model.joblib                      # Clustering model
└── README.md                                 # Documentation
```

## 🔍 Feature Engineering

The model uses the following features:

1. **TF-IDF Features (1000)**: Word importance scores
2. **Exclamation Marks**: Count of '!' in email
3. **Question Marks**: Count of '?' in email
4. **Flagged Words**: Count of spam keywords (free, winner, cash, etc.)
5. **Cluster Assignments (2)**: K-Means clustering categories

## 🚀 Deployment

This API can be deployed to:
- **Heroku**: `gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker`

## 🔒 Security Considerations
- No sensitive data stored or logged

## 📈 Future Improvements

- [ ] Add authentication/API keys
- [ ] Implement rate limiting
- [ ] Add more sophisticated features (sender reputation, links analysis)
- [ ] Deploy to cloud platform
- [ ] Add email header analysis
- [ ] Create admin dashboard for monitoring

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 👤 Author

**Adda Weathers**
- GitHub: [@addaweathers](https://github.com/addaweathers/weathers-tech-portfolio)
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/addaweathers/)

## 🙏 Acknowledgments

- Dataset: [Spam E-Mail Dataset](https://www.kaggle.com/datasets/abineshpa/spam-email-dataset)
- Inspired by real-world spam filtering systems
