#!/bin/bash

# Test script for the phishing email classification API
# Tests 2 duplicate entries and 3 different entries

echo "\n===== Testing API Endpoint with 5 Requests =====\n"

# First unique email
echo "\n----- Request 1 (First unique email) -----"
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "todays floor meeting you may get a few pointed questions about today article about lays potential severance of $ 80 mm"
}'

# Second unique email
echo "\n\n----- Request 2 (Second unique email) -----"
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "urgent action required: your account has been compromised, click here to reset your password immediately"
}'

# First duplicate (same as first email)
echo "\n\n----- Request 3 (Duplicate of first email - should be cached) -----"
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "todays floor meeting you may get a few pointed questions about today article about lays potential severance of $ 80 mm"
}'

# Third unique email
echo "\n\n----- Request 4 (Third unique email) -----"
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "congratulations you have won a free iphone, click here to claim your prize now before it expires"
}'

# Second duplicate (same as second email)
echo "\n\n----- Request 5 (Duplicate of second email - should be cached) -----"
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "urgent action required: your account has been compromised, click here to reset your password immediately"
}'

echo "\n\n===== Test Complete =====\n"
echo "Now run 'python check_redis.py' to verify the Redis cache entries"