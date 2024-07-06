import sys
import psutil
import unittest
sys.path.append('/Users/anjaligopal/qa-test/problem2/')


from src.health_monitor import check_cpu_usage, check_memory_usage, check_disk_usage

# Rest of your script follows...


class TestHealthMonitor(unittest.TestCase):

    def test_cpu_usage_normal(self):
        # Mock psutil.cpu_percent to return a normal value
        psutil.cpu_percent = lambda interval: 50
        self.assertEqual(check_cpu_usage(80), "CPU usage is normal: 50%")

    def test_cpu_usage_high(self):
        # Mock psutil.cpu_percent to return a high value
        psutil.cpu_percent = lambda interval: 85
        self.assertEqual(check_cpu_usage(80), "High CPU usage detected: 85%")

    def test_memory_usage_normal(self):
        # Mock psutil.virtual_memory to return a normal value
        psutil.virtual_memory = lambda: type('', (), {"percent": 50})()
        self.assertEqual(check_memory_usage(80), "Memory usage is normal: 50%")

    def test_memory_usage_high(self):
        # Mock psutil.virtual_memory to return a high value
        psutil.virtual_memory = lambda: type('', (), {"percent": 85})()
        self.assertEqual(check_memory_usage(80), "High memory usage detected: 85%")

    def test_disk_usage_normal(self):
        # Mock psutil.disk_usage to return a normal value
        psutil.disk_usage = lambda _: type('', (), {"percent": 50})()
        self.assertEqual(check_disk_usage(80), "Disk usage is normal: 50%")

    def test_disk_usage_high(self):
        # Mock psutil.disk_usage to return a high value
        psutil.disk_usage = lambda _: type('', (), {"percent": 85})()
        self.assertEqual(check_disk_usage(80), "High disk usage detected: 85%")

if __name__ == "__main__":
    unittest.main()

