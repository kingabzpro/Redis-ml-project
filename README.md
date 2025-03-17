# Phishing Email Classification App with Redis

This project demonstrates a phishing email classification application using machine learning. It includes four main components:

- **Model Training (`train.py`)**: Processes the dataset, trains a model using TF-IDF vectorization and logistic regression, and saves the trained model.
- **Model Validation (`validate.py`)**: Evaluates the saved model on a test dataset and outputs performance metrics such as accuracy, precision, and recall.
- **Model Serving (`serve.py`)**: Implements a FastAPI-based service to provide real-time phishing email predictions. Redis caching is used to optimize performance by speeding up repeated requests.
- **Redis Check (`check_redis.py`)**: A utility script to inspect the Redis database, displaying the number of cached entries and sample predictions.

---
## Application Workflow
The following diagram illustrates how the application works, including the interaction between the machine learning model, FastAPI, and Redis caching:

![Redis ML applicaiton diagram](image/redisml.svg)


---

## Project Structure

```
.
├── data/
│   └── phishing_emails.csv         # Kaggle dataset 
├── phishing_model.pkl              # Saved model file
├── train.py                        # Script for training the model
├── validate.py                     # Script for validating the model
├── serve.py                        # FastAPI app for model serving with Redis caching
└── check_redis.py                  # Script to inspect Redis cache entries
```

---

## Prerequisites

- Python 3.7+
- Pip
- Redis (see instructions below for running Redis on Windows)

Install the required Python packages with:
```bash
pip install -r requirements.txt
```

---

## Dataset

The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/subhajournal/phishingemails). Download the dataset and place it in the `data/` directory.

---

## Usage

### 1. Training the Model
Run the training script to process the dataset and generate the model file:
```bash
python train.py
```

### 2. Validating the Model
Run the validation script to evaluate the model's performance:
```bash
python validate.py
```

### 3. Serving Predictions
Ensure Redis is running (see instructions below for Windows), then start the FastAPI server:
```bash
python serve.py
```
Access the API at `http://localhost:8000` and send POST requests to the `/predict` endpoint with JSON payloads:
```json
{
  "text": "Your email content here..."
}
```

### 4. Checking Redis
Use the `check_redis.py` script to inspect the Redis cache. This script displays the number of cached entries and the first five email texts along with their predictions:
```bash
python check_redis.py
```

---

## Running Redis on Windows

1. **Enable WSL**: Follow [Microsoft's guide](https://docs.microsoft.com/en-us/windows/wsl/install) to enable WSL and install a Linux distribution (e.g., Ubuntu) from the Microsoft Store.
2. **Install Redis**: Open your WSL terminal and run:
   ```bash
   sudo apt update
   sudo apt install redis-server
   ```
3. **Start Redis**:
   ```bash
   sudo service redis-server start
   ```
4. **Access Redis from Windows**: With Redis running in WSL (default on `localhost:6379`), the Python Redis client in your FastAPI app can connect without extra configuration.

---

## API Usage

Send a POST request to `http://localhost:8000/predict` with the following JSON payload:
```bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "todays floor meeting you may get a few pointed questions about today article about lays potential severance of $ 80 mm"
}'
```

The API responds with a JSON object containing:
- **`prediction`**: The predicted class name (e.g., "Phishing Email" or "Safe Email").
- **`probability`**: The confidence score of the prediction.

Example response:
```json
{
  "prediction": "Safe Email",
  "probability": 0.7791625553383463
}
```
