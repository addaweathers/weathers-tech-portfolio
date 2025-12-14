import requests
import json

# Base URL
BASE_URL = "http://localhost:8000"


def test_health():
    """Test the health endpoint"""
    print("Testing /health endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")


def test_single_prediction():
    """Test single email prediction"""
    print("Testing /predict endpoint...")

    # Example spam email
    spam_email = {
        "text": "CONGRATULATIONS! You've won $1,000,000! Click here now to claim your prize!"
    }

    response = requests.post(f"{BASE_URL}/predict", json=spam_email)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")

    # Example legitimate email
    ham_email = {
        "text": "Hi team, let's schedule our weekly meeting for tomorrow at 2pm. Please confirm your availability."
    }

    response = requests.post(f"{BASE_URL}/predict", json=ham_email)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")


def test_batch_prediction():
    """Test batch email prediction"""
    print("Testing /predict/batch endpoint...")

    batch_request = {
        "emails": [
            "URGENT: Your account will be closed! Click here immediately!",
            "Can you review the attached document for our meeting?",
            "FREE VIAGRA! Best prices guaranteed! Order now!",
            "Your order #12345 has been shipped and will arrive tomorrow."
        ]
    }

    response = requests.post(f"{BASE_URL}/predict/batch", json=batch_request)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")


def test_model_info():
    """Test model info endpoint"""
    print("Testing /model/info endpoint...")
    response = requests.get(f"{BASE_URL}/model/info")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")


if __name__ == "__main__":
    try:
        print("=" * 60)
        print("Spam Email Detector API - Test Suite")
        print("=" * 60 + "\n")

        test_health()
        test_single_prediction()
        test_batch_prediction()
        test_model_info()

        print("=" * 60)
        print("All tests completed!")
        print("=" * 60)

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure it's running on http://localhost:8000")
    except Exception as e:
        print(f"Error: {e}")