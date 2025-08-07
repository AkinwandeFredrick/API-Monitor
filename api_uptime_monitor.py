import requests
import time
import logging
from datetime import datetime
from colorama import init, Fore, Style
import pyautogui
import os
import matplotlib.pyplot as plt
import numpy as np

# Initialize colorama for Windows support
init()

# Configure logging
logging.basicConfig(
    filename='api_uptime.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# List of APIs to monitor (URL and expected status code)
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
            response = requests.get(api["url"], timeout=10)
            status_code = response.status_code
            is_up = status_code == api["expected_status"]
            
            if is_up:
                logging.info(f"API {api['url']} is UP - Status Code: {status_code}")
                print(f"{Fore.GREEN}API {api['url']} is UP - Status Code: {status_code}{Style.RESET_ALL}")
            else:
                logging.warning(f"API {api['url']} is DOWN - Status Code: {status_code}, Expected: {api['expected_status']}")
                print(f"{Fore.RED}API {api['url']} is DOWN - Status Code: {status_code}, Expected: {api['expected_status']}{Style.RESET_ALL}")
            return is_up, status_code
        
        except requests.exceptions.RequestException as e:
            if attempt < max_retries:
                logging.warning(f"API {api['url']} attempt {attempt + 1} failed - Error: {str(e)}. Retrying in 5 seconds...")
                print(f"{Fore.YELLOW}API {api['url']} attempt {attempt + 1} failed - Error: {str(e)}. Retrying in 5 seconds...{Style.RESET_ALL}")
                time.sleep(5)
            else:
                logging.error(f"API {api['url']} failed after {max_retries + 1} attempts - Error: {str(e)}")
                print(f"{Fore.RED}API {api['url']} failed after {max_retries + 1} attempts - Error: {str(e)}{Style.RESET_ALL}")
                return False, None

def monitor_apis():
    """Check all APIs and log their status."""
    logging.info("Starting API monitoring cycle")
    print(f"{Fore.WHITE}Starting API monitoring cycle{Style.RESET_ALL}")
    for api in API_LIST:
        check_api(api)
    logging.info("Completed API monitoring cycle")
    print(f"{Fore.WHITE}Completed API monitoring cycle{Style.RESET_ALL}")
    generate_chart_and_screenshot()

def generate_chart_and_screenshot():
    """Generate a stacked bar chart and screenshot of the console display."""
    # Parse log file
    api_status = {api["url"]: {"UP": 0, "DOWN": 0, "FAILED": 0} for api in API_LIST}
    with open('api_uptime.log', 'r') as f:
        for line in f:
            if "API" in line:
                # Extract the base URL by matching against API_LIST
                url_start = line.find("API ") + 4
                potential_url = line[url_start:].split()[0]
                matched_url = next((url for url in API_LIST if url["url"].startswith(potential_url)), None)
                if matched_url:
                    url = matched_url["url"]
                    # Count statuses
                    if " is UP" in line:
                        api_status[url]["UP"] += 1
                    elif " is DOWN" in line:
                        api_status[url]["DOWN"] += 1
                    elif " failed after" in line:
                        api_status[url]["FAILED"] += 1

    # Prepare data for stacked bar chart
    labels = [
        "jsonplaceholder.typicode.com",
        "restcountries.com",
        "dog.ceo",
        "api.coindesk.com",
        "pokeapi.co",
        "api.publicapis.org",
        "randomuser.me",
        "gamerpower.com",
        "api.openverse.engineering"
    ]
    up_counts = [api_status[api["url"]]["UP"] for api in API_LIST]
    down_counts = [api_status[api["url"]]["DOWN"] for api in API_LIST]
    failed_counts = [api_status[api["url"]]["FAILED"] for api in API_LIST]

    # Create stacked bar chart
    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(len(labels))
    ax.bar(x, up_counts, label="UP", color="#2ecc71")
    ax.bar(x, down_counts, bottom=up_counts, label="DOWN", color="#e74c3c")
    ax.bar(x, failed_counts, bottom=np.array(up_counts) + np.array(down_counts), label="FAILED", color="#7f8c8d")

    # Customize chart
    ax.set_xlabel("APIs")
    ax.set_ylabel("Status Count")
    ax.set_title("API Uptime Status Counts")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.legend()
    ax.grid(True, axis="y", linestyle="--", alpha=0.7)
    ax.set_ylim(bottom=0)

    # Save chart as PNG
    chart_path = 'api_uptime_chart.png'
    plt.savefig(chart_path, bbox_inches='tight')
    plt.close(fig)
    print(f"{Fore.WHITE}Bar chart saved as {chart_path}{Style.RESET_ALL}")

    # Capture screenshot of the console display
    time.sleep(1)  # Wait for console output to stabilize
    screenshot_path = f'console_screenshot_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)
    print(f"{Fore.WHITE}Console screenshot saved as {screenshot_path}{Style.RESET_ALL}")

def main():
    # Run the first check immediately
    monitor_apis()

if __name__ == "__main__":
    main()
