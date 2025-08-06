🌟 API Uptime Monitor 🌟

The API Uptime Monitor is a vibrant Python-based tool designed to keep tabs on the uptime and availability of your favorite API endpoints!  This tool periodically checks your APIs, logs their status, and lets you know if they're up or down with clear, colorful logs. Perfect for developers who want to ensure their APIs are always ready to shine!
✨ Features

Monitors multiple API endpoints at regular intervals (default: every 5 minutes).
Logs API status (UP/DOWN) and errors to api_uptime.log for easy tracking.
Gracefully handles network issues with timeouts and exception handling.
Easily configurable list of APIs to monitor.

📋 Prerequisites
To get started, ensure you have:

Python 3.6 or higher installed.
Required Python packages listed in requirements.txt.

🛠️ Installation
1. Clone or Download the Project
Get the project files onto your local machine:
git clone <https://github.com/AkinwandeFredrick/API-Monitor>

Or download the ZIP file from GitHub and extract it.
2. Install Dependencies
Make sure Python is installed, then install the required packages:
pip install -r requirements.txt

The requirements.txt includes:

requests==2.32.3: For making HTTP requests.
schedule==1.2.2: For scheduling periodic checks.

🚀 Usage
1. Configure APIs to Monitor
Edit api_uptime_monitor.py and update the API_LIST variable with the APIs you want to monitor. Each entry needs:

url: The API endpoint URL.
expected_status: The expected HTTP status code (e.g., 200 for OK).

Example:
API_LIST = [
    {"url": "https://jsonplaceholder.typicode.com/posts", "expected_status": 200},
    {"url": "https://dog.ceo/api/breeds/image/random", "expected_status": 200}
]

2. Run the Script
Launch the monitor using powershell or command prompt (Terminal for linux users)with:
python api_uptime_monitor.py

What happens next:

The script performs an initial check of all APIs.
It then checks every 5 minutes.
Results are logged to api_uptime.log.

3. View Logs
Open api_uptime.log to see status updates. Example entries:
2025-08-06 22:45:00,123 - INFO - Starting API monitoring cycle
2025-08-06 22:45:00,456 - INFO - API https://jsonplaceholder.typicode.com/posts is UP - Status Code: 200
2025-08-06 22:45:00,789 - WARNING - API https://example.com/status is DOWN - Status Code: 404, Expected: 200
2025-08-06 22:45:01,012 - INFO - Completed API monitoring cycle

4. Stop the Script
Hit Ctrl+C to gracefully stop the monitoring.
🌐 Included APIs
The default configuration monitors these public APIs (no authentication needed):

JSONPlaceholder: https://jsonplaceholder.typicode.com/posts (Status: 200)
REST Countries: https://restcountries.com/v3.1/all (Status: 200)
Dog CEO API: https://dog.ceo/api/breeds/image/random (Status: 200)
CoinDesk Bitcoin Price: https://api.coindesk.com/v1/bpi/currentprice.json (Status: 200)
PokeAPI: https://pokeapi.co/api/v2/pokemon/ditto (Status: 200)
Public APIs: https://api.publicapis.org/entries (Status: 200)
Random User API: https://randomuser.me/api/ (Status: 200)
GamerPower API: https://www.gamerpower.com/api/giveaways (Status: 200)
Openverse API: https://api.openverse.engineering/v1/images/ (Status: 200)


Note: Watch out for rate limits (e.g., Public APIs has a 1000 requests/day limit). Adjust the check interval in api_uptime_monitor.py (e.g., schedule.every(10).minutes) if needed.

🛠️ Troubleshooting

Connection Errors: Ensure your machine has internet access and API URLs are correct.
Rate Limits: If an API returns a 429 status code, increase the check interval in the script.
Missing Dependencies: Verify all packages are installed with pip install -r requirements.txt.

📜 License
This project is open-source and available under the MIT License. 🎉
