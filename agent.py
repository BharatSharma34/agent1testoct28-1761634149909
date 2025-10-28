import requests

def main():
    """
    Main function for agent1testOct28
    This function will call an AWS Lambda function URL and return its response.
    """

    # Lambda Function URL
    lambda_url = "https://jyhtv2lzrk6vue7ovjtbmfotfi0utvxl.lambda-url.eu-north-1.on.aws/"
    app_key = "xx"
    try:
        # Optional: You can send data if your Lambda expects POST input
        payload = {"example": "test"}  
        headers = {"Content-Type": "application/json"}

        # Call Lambda function (GET or POST depending on how your Lambda is written)
        response = requests.post(lambda_url, json=payload, headers=headers, timeout=15)
        response.raise_for_status()  # raises an error if response code is not 200

        # Parse JSON returned by Lambda
        lambda_data = response.json()

        return {
            "success": True,
            "message": f"Lambda call succeeded! Response: {lambda_data}",
            "data": lambda_data
        }

    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "message": f"Lambda call failed: {e}",
            "data": {}
        }

