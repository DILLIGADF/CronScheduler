# test_cronscheduler.py
"""
Tests for CronScheduler module.
"""

import unittest
from cronscheduler import CronScheduler

class TestCronScheduler(unittest.TestCase):
    """Test cases for CronScheduler class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CronScheduler()
        self.assertIsInstance(instance, CronScheduler)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CronScheduler()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
