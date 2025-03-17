# check_redis.py

import redis
import json
from tabulate import tabulate


def main():
    # Connect to Redis (ensure Redis is running on localhost:6379)
    redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

    # Retrieve all keys that start with "prediction:"
    keys = redis_client.keys("prediction:*")
    total_entries = len(keys)
    print(f"Total number of cached prediction entries: {total_entries}\n")

    table_data = []
    # Process only the first 5 entries
    for key in keys[:5]:
        # Remove the 'prediction:' prefix to get the original email text
        email_text = key.replace("prediction:", "", 1)

        # Retrieve the cached value
        value = redis_client.get(key)
        try:
            data = json.loads(value)
        except json.JSONDecodeError:
            data = {}

        prediction = data.get("prediction", "N/A")

        # Display only the first 7 words of the email text
        words = email_text.split()
        truncated_text = " ".join(words[:7]) + ("..." if len(words) > 7 else "")

        table_data.append([truncated_text, prediction])

    # Print table using tabulate (only two columns now)
    headers = ["Email Text (First 7 Words)", "Prediction"]
    print(tabulate(table_data, headers=headers, tablefmt="pretty"))


if __name__ == "__main__":
    main()
