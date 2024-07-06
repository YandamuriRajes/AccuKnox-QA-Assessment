import psutil
import time

CPU_THRESHOLD = 80  # percentage
MEMORY_THRESHOLD = 80  # percentage
DISK_THRESHOLD = 80  # percentage

def check_cpu_usage(threshold=CPU_THRESHOLD):
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > threshold:
        return f"High CPU usage detected: {cpu_usage}%"
    return f"CPU usage is normal: {cpu_usage}%"

def check_memory_usage(threshold=MEMORY_THRESHOLD):
    memory_info = psutil.virtual_memory()
    if memory_info.percent > threshold:
        return f"High memory usage detected: {memory_info.percent}%"
    return f"Memory usage is normal: {memory_info.percent}%"

def check_disk_usage(threshold=DISK_THRESHOLD):
    disk_info = psutil.disk_usage('/')
    if disk_info.percent > threshold:
        return f"High disk usage detected: {disk_info.percent}%"
    return f"Disk usage is normal: {disk_info.percent}%"

def check_system_health():
    print(check_cpu_usage())
    print(check_memory_usage())
    print(check_disk_usage())

if __name__ == "__main__":
    while True:
        check_system_health()
        time.sleep(5)


