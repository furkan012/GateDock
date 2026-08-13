# test_gatedock.py
"""
Tests for GateDock module.
"""

import unittest
from gatedock import GateDock

class TestGateDock(unittest.TestCase):
    """Test cases for GateDock class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GateDock()
        self.assertIsInstance(instance, GateDock)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GateDock()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
