#!/usr/bin/env python


import unittest
import rebrand_config

class RebrandOSSIMTest(unittest.TestCase):

	def setUp(self):
		global read_file , write_file,  item_list
		item_list = ['label','text','confirm','menus','info','next','next_else']
		rebrand_config.enable_logging()
		write_file = open('/workspace/OSSIM/rebranding/May-2017/rebranded/menu.cfr',"w")
		read_file = open('/workspace/OSSIM/rebranding/May-2017/rebranded/menu.cfg',"r")
		

	def test_000_read_yaml(self):
		self.assertEqual(rebrand_config.read_yaml('config/','ossim_rebrand_config.yaml'),'Open: ossim_rebrand_config.yaml success')

	def test_001_read_yaml_with_wrong_file_name(self):	
		self.assertEqual(rebrand_config.read_yaml('config/','ossim_rebrand.yaml'),'Open: ossim_rebrand.yaml  Failed with No such file or directory')

	def test_002_find_and_replace(self):
		self.assertEqual(rebrand_config.find_and_replace('label=Alienvault Setup','Alienvault', 'Securmatic'),'label=Securmatic Setup')

	def test_003_find_and_replace_when_which_string_not_in_text(self):
		self.assertEqual(rebrand_config.find_and_replace('Alienvault Setup','Test', 'Securmatic'),'Alienvault Setup')

	def test_004_find_and_replace_when_what_string_None(self):
		self.assertEqual(rebrand_config.find_and_replace('Alienvault Setup',None, 'Securmatic'),'what_str can not be Null')

	def test_006_find_and_replace_when_with_string_None(self):
		self.assertEqual(rebrand_config.find_and_replace('Alienvault Setup','Alienvault', None),'with_str can not be Null')

	def test_007_find_and_replace_when_text_None(self):
		self.assertEqual(rebrand_config.find_and_replace(None,'Alienvault', 'Securmatic'),'text can not be Null')

	def test_008_open_config_file(self):
		self.assertTrue(rebrand_config.open_config_files('/workspace/OSSIM/rebranding/May-2017/rebranded/','menu','.cfg'))

	def test_009_open_config_file_with_incorrect_path(self):
		self.assertFalse(rebrand_config.open_config_files('/workspace/OSSIM/rebranding/May-2017','menu','.cfg'))

	def test_010_read_and_replace_lines(self):
		self.assertTrue(rebrand_config.read_and_replace_lines(read_file,'/workspace/OSSIM/rebranding/May-2017/rebranded/menu.ctr',item_list,'AlienVault','Securmatic'))

	def test_011_close_config_file(self):
		self.assertTrue(rebrand_config.close_config_files(read_file,write_file))

	def test_012_backup_and_rename_main_file(self):
		self.assertTrue(rebrand_config.backup_and_rename_main_file('/workspace/OSSIM/rebranding/May-2017/rebranded/','menu.cfg.test','menu.ctr'))

	def tierDown(self):
		pass


if __name__ == '__main__':
    unittest.main()