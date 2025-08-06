import requests
import schedule
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='api_uptime.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# List of APIs to monitor (URL and expected status code)
# Note: https://restcountries.com/v3.1/all returns 400; investigate endpoint.
# Note: https://api.coindesk.com/v1/bpi/currentprice.json and https://api.publicapis.org/entries have had DNS issues; retries added.
API_LIST = [
    {"url": "https://jsonplaceholder.typicode.com/posts", "expected_status": 200},
    {"url": "https://restcountries.com/v3.1/all", "expected_status": 200},
    {"url": "https://dog.ceo/api/breeds/image/random", "expected_status": 200},
    {"url": "https://api.coindesk.com/v1/bpi/currentprice.json", "expected_status": 200},
    {"url": "https://pokeapi.co/api/v2/pokemon/ditto", "expected_status": 200},
    {"url": "https://api.publicapis.org/entries", "expected_status": 200},
    {"url": "https://randomuser.me/api/", "expected_status": 200},
    {"url": "https://www.gamerpower.com/api/giveaways", "expected_status": 200},
    {"url": "https://api.openverse.engineering/v1/images/", "expected_status": 200}
]

def check_api(api, max_retries=2):
    """Check the status of a single API endpoint with retries for DNS issues."""
    for attempt in range(max_retries + 1):
        try:
            response = requests.get(api["url"], timeout=10)  # Increased timeout to 10 seconds
            status_code = response.status_code
            is_up = status_code == api["expected_status"]
            
            if is_up:
                logging.info(f"API {api['url']} is UP - Status Code: {status_code}")
                print(f"API {api['url']} is UP - Status Code: {status_code}")
            else:
                logging.warning(f"API {api['url']} is DOWN - Status Code: {status_code}, Expected: {api['expected_status']}")
                print(f"API {api['url']} is DOWN - Status Code: {status_code}, Expected: {api['expected_status']}")
            return is_up, status_code
        
        except requests.exceptions.RequestException as e:
            if attempt < max_retries:
                logging.warning(f"API {api['url']} attempt {attempt + 1} failed - Error: {str(e)}. Retrying in 5 seconds...")
                print(f"API {api['url']} attempt {attempt + 1} failed - Error: {str(e)}. Retrying in 5 seconds...")
                time.sleep(5)  # Wait 5 seconds before retrying
            else:
                logging.error(f"API {api['url']} failed after {max_retries + 1} attempts - Error: {str(e)}")
                print(f"API {api['url']} failed after {max_retries + 1} attempts - Error: {str(e)}")
                return False, None

def monitor_apis():
    """Check all APIs and log their status."""
    logging.info("Starting API monitoring cycle")
    print("Starting API monitoring cycle")
    for api in API_LIST:
        check_api(api)
    logging.info("Completed API monitoring cycle")
    print("Completed API monitoring cycle")

def main():
    # Schedule the monitor to run every 10 minutes
    schedule.every(10).minutes.do(monitor_apis)
    
    # Run the first check immediately
    monitor_apis()
    
    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute for scheduled tasks

if __name__ == "__main__":
    main()