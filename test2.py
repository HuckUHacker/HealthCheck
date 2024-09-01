import argparse
import requests

def health_check(api_url):
    """Perform a health check on the given API URL."""
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad status codes
        print(f"Health check successful! Status code: {response.status_code}")
        print(f"Response: {response.json()}")  # Assuming the response is in JSON format
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")

def main():
    parser = argparse.ArgumentParser(description="API Health Check Script")
    parser.add_argument('url', type=str, help="The URL of the API health check endpoint")
    
    args = parser.parse_args()
    health_check(args.url)

if __name__ == '__main__':
    main()
