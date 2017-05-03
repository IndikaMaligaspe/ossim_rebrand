#!/usr/bin/env python

import os
import yaml



def read_yaml(config_file_location,config_file_name):
	""" reads config file and reads all elements into a dictionary """
	global sensor_configs ,standard_configs
	sensor_configs = {}
	standard_configs = {}
	file_status = 'success'
	try:
		with open(config_file_location+config_file_name, 'r') as yfile:
			doc = yaml.load(yfile)
			sensor_configs['source_file'] = doc["sensor"]["source_file"]
			sensor_configs['source_location'] = doc["sensor"]["source_location"]
			sensor_configs['items_list'] = doc["sensor"]["items_list"]
			sensor_configs['replace_what'] = doc["sensor"]["replace_what"]
			sensor_configs['replace_with'] = doc["sensor"]["replace_with"]

			standard_configs['debug'] = doc["config"]["debug"]
			standard_configs['log'] = doc["config"]["log"]
			standard_configs['log_location'] = doc["config"]["log_location"]
			standard_configs['log_name'] = doc["config"]["log_name"]
			standard_configs['format'] = doc["config"]["format"]


	except (yaml.YAMLError,IOError) as exc:
		file_status = ' Failed with ' + exc.args[1]

	message = 'Open: '+config_file_name+' ' +file_status
	return message

def find_and_replace(text, what_str, with_str):
	""" Gets a text  and replaces the with_str with what_str """

	if what_str is None:
		return "what_str can not be Null"
	if with_str is None:
		return "with_str can not be Null"

	if text is None:
		return "text can not be Null"

	if what_str in text.split():
		print ("String Before - "+text)
		text = text.replace(what_str,with_str)
		print ("String After - "+text)
	else:
		return what_str+" Not in "+ text
	return text

import unittest

class RebrandOSSIMTest(unittest.TestCase):

	def setUp(self):
		pass

	def test_read_yaml(self):
		self.assertEqual(read_yaml('src/config/','ossim_rebrand_config.yaml'),'Open: ossim_rebrand_config.yaml success')

	def test_read_yaml_with_wrong_file_name(self):	
		self.assertEqual(read_yaml('src/config/','ossim_rebrand.yaml'),'Open: ossim_rebrand.yaml  Failed with No such file or directory')

	def test_find_and_replace(self):
		self.assertEqual(find_and_replace('Alienvault Setup','Alienvault', 'Securmatic'),'Securmatic Setup')

	def test_find_and_replace_when_which_string_not_in_text(self):
		self.assertEqual(find_and_replace('Alienvault Setup','Test', 'Securmatic'),'Test Not in Alienvault Setup')

	def test_find_and_replace_when_what_string_None(self):
		self.assertEqual(find_and_replace('Alienvault Setup',None, 'Securmatic'),'what_str can not be Null')

	def test_find_and_replace_when_with_string_None(self):
		self.assertEqual(find_and_replace('Alienvault Setup','Alienvault', None),'with_str can not be Null')

	def test_find_and_replace_when_text_None(self):
		self.assertEqual(find_and_replace(None,'Alienvault', 'Securmatic'),'text can not be Null')



if __name__ == '__main__':
    unittest.main()