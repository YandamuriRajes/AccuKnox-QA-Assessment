import re

# Update the log_file_path variable with the actual path to your log file
log_file_path = '/Users/anjaligopal/qa-test/problem2/logs/sample.log'

def analyze_log_file(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()
    
    error_404_count = 0
    ip_requests = {}

    for log in logs:
        if '404' in log:
            error_404_count += 1
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', log)
        if ip:
            ip = ip[0]
            if ip in ip_requests:
                ip_requests[ip] += 1
            else:
                ip_requests[ip] = 1
    
    most_requests_ip = max(ip_requests, key=ip_requests.get)

    print(f"Number of 404 errors: {error_404_count}")
    print(f"IP with the most requests: {most_requests_ip} ({ip_requests[most_requests_ip]} requests)")

if __name__ == "__main__":
    analyze_log_file(log_file_path)

