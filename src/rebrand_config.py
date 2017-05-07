#!/usr/bin/env python

import os
import sys
import fileinput
import yaml
import logging
import datetime
from shutil import move


def read_yaml(config_file_location,config_file_name):
	""" reads config file and reads all elements into a dictionary """
	logging.info(" reads config file and reads all elements into a dictionary ")
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

def enable_logging():
	logging.basicConfig(filename='test.log',level=logging.DEBUG)

def find_and_replace(text, what_str, with_str):
	logging.debug ("find_and_replace {0} , {1} - " .format(what_str,with_str))
	""" Gets a text  and replaces the with_str with what_str """

	if what_str is None:
		return "what_str can not be Null"
	if with_str is None:
		return "with_str can not be Null"

	if text is None:
		return "text can not be Null"

	if what_str.upper() in text.upper():
		logging.debug ("String Before - "+text)
		text = text.replace(what_str,with_str)
		logging.debug ("String After - "+text)
	else:
		logging.debug (what_str+" Not in "+ text)
	return text

def open_config_files(config_path,config_file_name,file_extenssion):
	global read_file , write_file

	read_file_path_name = config_path+config_file_name+file_extenssion
	write_file_path_name = config_path+config_file_name+'.fer'

	try:
		read_file = open(read_file_path_name,"r")
		write_file = open(write_file_path_name,"w")
	except IOError as err:
		logging.error('Error while opening read_file_path_name  - '+str(err))
		return False
	return True

def read_and_replace_lines(read_file,write_file_name,item_list,what_str,with_str):
	try:
		write_line=''
			
		for line in read_file:
			if "=" in line:
				key_value =  line.split('=')
				logging.debug('Key Value.....'+str(key_value))
				logging.debug('item_list.....'+str(item_list))
				if key_value[0] in item_list:
					new_line = find_and_replace(line, what_str, with_str)
					line = new_line
	
			write_line = write_line + line
		write_file = open(write_file_name,"w")
		write_file.write(write_line)	
		write_file.close()
		logging.info("---------------Finished Writing %s -------------------" %write_file_name)
	except Exception as exe:
		logging.error('Error while reading and replacing lines - '+str(exe))
		return False
	return True

def backup_and_rename_main_file(file_location,original_file,tmp_file):
	try:
		back_up_file_name = datetime.datetime.now().strftime("%d-%M-%Y-%I")
		abs_original_file = file_location+original_file
		abs_backup_file  = file_location+original_file +".backup."+back_up_file_name
		abs_tmp_file = file_location+tmp_file

		logging.debug("original File {0}".format(str(abs_original_file)))
		logging.debug("backup File {0}".format(str(abs_backup_file)))

		move(abs_original_file,abs_backup_file)
		move(abs_tmp_file,abs_original_file)
		logging.info("{0} file recreated with renamed charactaers...".format(abs_original_file))

	except IOError as ioer:
		logging.error('Error while backing up and renaming - '+str(ioer))
		return False
	return True;

def close_config_files(read_file,write_file):
	try:
		read_file.close()
		write_file.close()
	except IOError as err:
		logging.error('Error while closing read_file / write files  - '+str(err))
		return False
	return True


def main():
	
if __name__ == '__main__':
    main()