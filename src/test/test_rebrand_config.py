#!/usr/bin/env python


import unittest
import rebrand_config

class TestRebrandOSSIM(unittest.TestCase):
	
	def setUp(self):
		pass

	def test_read_yaml(seld):
		self.assertEqual(rebrand_config.read_yaml('config/ossim_rebrand_config.yaml'))


if __name__ == '__main__':
	unittest.main()
