# test_web3core.py
"""
Tests for Web3Core module.
"""

import unittest
from web3core import Web3Core

class TestWeb3Core(unittest.TestCase):
    """Test cases for Web3Core class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Web3Core()
        self.assertIsInstance(instance, Web3Core)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Web3Core()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
