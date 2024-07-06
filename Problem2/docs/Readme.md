# QA Engineer Practical Assessment - Problem 2

## System Health Monitoring Script

1. **Description**: Monitors CPU, memory, and disk usage of the system.
2. **File**: `health_monitor.py`
3. **Usage**:
   - Install dependencies: `pip install psutil`
   - Run the script: `python3 health_monitor.py`

## Log File Analyzer

1. **Description**: Analyzes web server logs for common patterns like 404 errors and most frequent IP addresses.
2. **File**: `log_analyzer.py`
3. **Usage**:
   - Update `log_file_path` variable with the path to your log file.
   - Run the script: `python3 log_analyzer.py`

## Application Health Checker

1. **Description**: Checks the health status of an application by monitoring HTTP status codes.
2. **File**: `health_checker.py`
3. **Setup**:
   - Ensure `requests` module is installed: `pip install requests`
   - Update `URL` variable with your application's URL in `health_checker.py`.
   - Run the application health checker server: `python3 health_checker_helper.py`
   - Run the health checker script: `python3 health_checker.py`

## Test Script for Health Monitor

1. **Description**: Tests for the health monitoring script (`health_monitor.py`).
2. **File**: `test_health_monitor.py`
3. **Execution**:
   - Ensure `unittest` is installed (usually included with Python).
   - Run the test script: `python3 test_health_monitor.py`

## Folder Structure

problem2/
│
├── health_monitor.py
├── log_analyzer.py
├── health_checker.py
├── test_health_monitor.py
├── health_checker_helper.py
└── README.md

### Instructions:

- Ensure Python 3.x and pip are installed on your system.
- Use a virtual environment (`venv` recommended) for managing dependencies (`env/` folder not included in repository).
- Customize scripts and variables (`URL`, `log_file_path`) according to your environment and requirements.
- Execute scripts from within the `problem2` directory using Python 3:
  ```sh
  cd /path/to/qa-test/problem2
  python3 script_name.py
  ```

Notes:
Scripts provided for system monitoring, log analysis, and application health checking.
Extend and modify scripts as needed for specific testing and monitoring tasks.
For the application health checker, ensure health_checker-helper.py is running on port 5000 before executing health_checker.py.

This README.md file provides comprehensive instructions and details for each script (`health_monitor.py`, `log_analyzer.py`, `health_checker.py`, `test_health_monitor.py`, `health_checker_helper.py`) in your `problem2` folder. Adjust paths, dependencies, and instructions based on your specific environment and setup.
