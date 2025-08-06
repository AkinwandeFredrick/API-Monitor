
# API Uptime Monitor

This is a Python-based tool to monitor the uptime and availability of multiple API endpoints. It periodically checks specified APIs, logs their status, and reports whether they are up or down based on their HTTP status codes.
Features

Monitors multiple API endpoints at regular intervals (default: every 5 minutes).
Logs API status (UP/DOWN) and errors to a file (api_uptime.log).
Handles network issues gracefully with timeout and exception handling.
Easily configurable list of APIs to monitor.

Prerequisites

Python 3.6 or higher
Required Python packages (listed in requirements.txt)

Installation

Clone or Download the Project

Clone the repository or download the project files to your local machine.

Install Dependencies

Ensure you have Python installed.
Install the required packages by running:pip install -r requirements.txt

The requirements.txt file includes:
requests==2.32.3: For making HTTP requests.
schedule==1.2.2: For scheduling periodic checks.

Usage

Configure APIs to Monitor

Open api_uptime_monitor.py and update the API_LIST variable with the APIs you want to monitor. Each entry should include:
url: The API endpoint URL.
expected_status: The expected HTTP status code (e.g., 200 for OK).

Example:API_LIST = [
    {"url": "https://jsonplaceholder.typicode.com/posts", "expected_status": 200},
    {"url": "https://dog.ceo/api/breeds/image/random", "expected_status": 200}
]

Run the Script

Execute the script using:python api_uptime_monitor.py

The script will:
Perform an initial check of all APIs.
Check APIs every 5 minutes thereafter.
Log results to api_uptime.log.

View Logs

Check the api_uptime.log file for status updates. Example log entries:2025-08-06 22:45:00,123 - INFO - Starting API monitoring cycle
2025-08-06 22:45:00,456 - INFO - API <https://jsonplaceholder.typicode.com/posts> is UP - Status Code: 200
2025-08-06 22:45:00,789 - WARNING - API <https://example.com/status> is DOWN - Status Code: 404, Expected: 200
2025-08-06 22:45:01,012 - INFO - Completed API monitoring cycle

Stop the Script

Press Ctrl+C to stop the script.

Included APIs
The default configuration monitors the following public APIs (no authentication required):

JSONPlaceholder: <https://jsonplaceholder.typicode.com/posts> (Status: 200)
REST Countries: <https://restcountries.com/v3.1/all> (Status: 200)
Dog CEO API: <https://dog.ceo/api/breeds/image/random> (Status: 200)
CoinDesk Bitcoin Price: <https://api.coindesk.com/v1/bpi/currentprice.json> (Status: 200)
PokeAPI: <https://pokeapi.co/api/v2/pokemon/ditto> (Status: 200)
Public APIs: <https://api.publicapis.org/entries> (Status: 200)
Random User API: <https://randomuser.me/api/> (Status: 200)
GamerPower API: <https://www.gamerpower.com/api/giveaways> (Status: 200)
Openverse API: <https://api.openverse.engineering/v1/images/> (Status: 200)

Note: Be aware of rate limits for these APIs (e.g., Public APIs has a 1000 requests/day limit). Adjust the check interval in api_uptime_monitor.py (e.g., schedule.every(10).minutes) if needed.

Troubleshooting

Connection Errors: Ensure your machine has internet access and the API URLs are correct.
Rate Limits: If an API returns a 429 status code, increase the check interval in the script.
Missing Dependencies: Verify all packages are installed using pip install -r requirements.txt.

License
This project is open-source and available under the MIT License.
