# health_checker.py
import requests

URL = 'http://localhost:5000'

def check_application_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Application is up and running.")
        else:
            print(f"Application is down. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Application is down. Error: {e}")

if __name__ == "__main__":
    check_application_health(URL)

