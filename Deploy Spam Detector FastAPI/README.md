# 🛡️ Spam Email Detector API

A machine learning-powered REST API that classifies emails as spam or legitimate using XGBoost, Natural Language Processing, and **Docker containerization**.

## 🎯 Project Overview

This project demonstrates the transition of a Machine Learning model from a research environment (Jupyter) to a production-ready application.
- **Model Deployment**: High-performance FastAPI backend.
- **Containerization**: Packaged with **Docker** for consistent environment behavior across any machine.
- **XGBoost Classifier**: Trained on 5,728 emails with 95%+ accuracy.
- **Enhanced NLP**: Integrates TF-IDF vectorization and K-Means clustering to improve prediction confidence.

## 🚀 Features

- **Integrated Web UI**: A user-friendly dashboard served directly at the root (`/`) path.
- **Real-time Prediction**: Instant classification with probability scores.
- **Batch Processing**: Support for analyzing up to 100 emails in a single request.
- **Advanced Feature Engineering**: Analysis of exclamation marks, question marks, flagged keywords, and text length.
- **Automatic Documentation**: Interactive Swagger UI available at `/docs`.

## 📊 Model Performance

- **Algorithm**: XGBoost Classifier
- **Total Features**: 1,005
  - 1,000 TF-IDF word importance features
  - 3 text-based engineered features
  - 2 K-Means cluster assignment features
- **Training Data**: 5,728 emails
- **Accuracy**: 95%+

## 🛠️ Technology Stack

- **Backend**: FastAPI, Python 3.12
- **ML/NLP**: scikit-learn, XGBoost, Joblib
- **Deployment**: Docker, Uvicorn
- **Frontend**: HTML5, CSS3, Vanilla JavaScript

---

## 📦 Deployment with Docker (Recommended)

This is the standard way to run the API. It handles all dependencies, including the Python version and model libraries, automatically.
```bash
docker build -t spam-detector:v1 .

1. Clone the repository:
```bash
git clone
cd FastAPI

2. Run the Container:
docker run -d -p 8000:8000 --name spam-app spam-detector:v1

3. Access the App:
Web Interface: http://localhost:8000
```

## 🛠️ Manual Installation (Local Development)
```bash
1. Clone the Repository:
git clone [https://github.com/addaweathers/weathers-tech-portfolio.git](https://github.com/addaweathers/weathers-tech-portfolio.git)
cd "Deploy Spam Detector FastAPI"

2. Create and Activate Virtual Environment:
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. Install Dependencies:
pip install -r requirements.txt

4. Run the server:
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

```text
Deploy Spam Detector FastAPI/
├── main.py                # FastAPI application & HTML routing
├── spam_checker.html      # Interactive Web Interface (HTML/JS)
├── Dockerfile             # Container build recipe
├── .dockerignore          # Optimization: Excludes unnecessary files from build
├── requirements.txt       # Python library dependencies
├── test_api.py            # Automated API test suite
├── optimized_spam_detector_xgb_model.joblib  # Trained XGBoost model
├── tfidf_vectorizer.joblib # TF-IDF NLP model
├── cluster_model.joblib    # K-Means clustering model
└── README.md              # Project documentation
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
