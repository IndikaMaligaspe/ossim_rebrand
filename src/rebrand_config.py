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
			sensor_configs['menu-cfg.source_file'] = doc["sensor"]["menu-cfg"]["source_file"]
			sensor_configs['menu-cfg.source_location'] = doc["sensor"]["menu-cfg"]["source_location"]
			sensor_configs['menu-cfg.source_file_ext'] = doc["sensor"]["menu-cfg"]["source_file_ext"]
			sensor_configs['menu-cfg.dest_file'] = doc["sensor"]["menu-cfg"]["dest_file"]
			sensor_configs['menu-cfg.dest_file_ext'] = doc["sensor"]["menu-cfg"]["dest_file_ext"]
			sensor_configs['menu-cfg.items_list'] = doc["sensor"]["menu-cfg"]["items_list"]
			sensor_configs['menu-cfg.replace_what'] = doc["sensor"]["menu-cfg"]["replace_what"]
			sensor_configs['menu-cfg.replace_with'] = doc["sensor"]["menu-cfg"]["replace_with"]

			sensor_configs['menu-network-cfg.source_file'] = doc["sensor"]["menu-network-cfg"]["source_file"]
			sensor_configs['menu-network-cfg.source_location'] = doc["sensor"]["menu-network-cfg"]["source_location"]
			sensor_configs['menu-network-cfg.source_file_ext'] = doc["sensor"]["menu-network-cfg"]["source_file_ext"]
			sensor_configs['menu-network-cfg.dest_file'] = doc["sensor"]["menu-network-cfg"]["dest_file"]
			sensor_configs['menu-network-cfg.dest_file_ext'] = doc["sensor"]["menu-network-cfg"]["dest_file_ext"]
			sensor_configs['menu-network-cfg.items_list'] = doc["sensor"]["menu-network-cfg"]["items_list"]
			sensor_configs['menu-network-cfg.replace_what'] = doc["sensor"]["menu-network-cfg"]["replace_what"]
			sensor_configs['menu-network-cfg.replace_with'] = doc["sensor"]["menu-network-cfg"]["replace_with"]

			sensor_configs['ossim-setup.source_file'] = doc["sensor"]["ossim-setup"]["source_file"]
			sensor_configs['ossim-setup.source_location'] = doc["sensor"]["ossim-setup"]["source_location"]
			sensor_configs['ossim-setup.source_file_ext'] = doc["sensor"]["ossim-setup"]["source_file_ext"]
			sensor_configs['ossim-setup.dest_file'] = doc["sensor"]["ossim-setup"]["dest_file"]
			sensor_configs['ossim-setup.dest_file_ext'] = doc["sensor"]["ossim-setup"]["dest_file_ext"]
			sensor_configs['ossim-setup.items_list'] = doc["sensor"]["ossim-setup"]["items_list"]
			sensor_configs['ossim-setup.replace_what'] = doc["sensor"]["ossim-setup"]["replace_what"]
			sensor_configs['ossim-setup.replace_with'] = doc["sensor"]["ossim-setup"]["replace_with"]

			sensor_configs['issue.source_file'] = doc["sensor"]["issue"]["source_file"]
			sensor_configs['issue.source_location'] = doc["sensor"]["issue"]["source_location"]
			sensor_configs['issue.source_file_ext'] = doc["sensor"]["issue"]["source_file_ext"]
			sensor_configs['issue.dest_file'] = doc["sensor"]["issue"]["dest_file"]
			sensor_configs['issue.dest_file_ext'] = doc["sensor"]["issue"]["dest_file_ext"]
			sensor_configs['issue.items_list'] = doc["sensor"]["issue"]["items_list"]
			sensor_configs['issue.replace_what'] = doc["sensor"]["issue"]["replace_what"]
			sensor_configs['issue.replace_with'] = doc["sensor"]["issue"]["replace_with"]

			sensor_configs['motd-tail.source_file'] = doc["sensor"]["motd-tail"]["source_file"]
			sensor_configs['motd-tail.source_location'] = doc["sensor"]["motd-tail"]["source_location"]
			sensor_configs['motd-tail.source_file_ext'] = doc["sensor"]["motd-tail"]["source_file_ext"]
			sensor_configs['motd-tail.dest_file'] = doc["sensor"]["motd-tail"]["dest_file"]
			sensor_configs['motd-tail.dest_file_ext'] = doc["sensor"]["motd-tail"]["dest_file_ext"]
			sensor_configs['motd-tail.items_list'] = doc["sensor"]["motd-tail"]["items_list"]
			sensor_configs['motd-tail.replace_what'] = doc["sensor"]["motd-tail"]["replace_what"]
			sensor_configs['motd-tail.replace_with'] = doc["sensor"]["motd-tail"]["replace_with"]



			sensor_configs['hostname.source_file'] = doc["sensor"]["hostname"]["source_file"]
			sensor_configs['hostname.source_location'] = doc["sensor"]["hostname"]["source_location"]
			sensor_configs['hostname.source_file_ext'] = doc["sensor"]["hostname"]["source_file_ext"]
			sensor_configs['hostname.dest_file'] = doc["sensor"]["hostname"]["dest_file"]
			sensor_configs['hostname.dest_file_ext'] = doc["sensor"]["hostname"]["dest_file_ext"]
			sensor_configs['hostname.replace_what'] = doc["sensor"]["hostname"]["replace_what"]
			sensor_configs['hostname.replace_with'] = doc["sensor"]["hostname"]["replace_with"]

			sensor_configs['hosts.source_file'] = doc["sensor"]["hosts"]["source_file"]
			sensor_configs['hosts.source_location'] = doc["sensor"]["hosts"]["source_location"]
			sensor_configs['hosts.source_file_ext'] = doc["sensor"]["hosts"]["source_file_ext"]
			sensor_configs['hosts.dest_file'] = doc["sensor"]["hosts"]["dest_file"]
			sensor_configs['hosts.dest_file_ext'] = doc["sensor"]["hosts"]["dest_file_ext"]
			sensor_configs['hosts.replace_what'] = doc["sensor"]["hosts"]["replace_what"]
			sensor_configs['hosts.replace_with'] = doc["sensor"]["hosts"]["replace_with"]



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
	global read_file

	if None == file_extenssion:
		file_extenssion=''

	read_file_path_name = config_path+config_file_name+file_extenssion

	try:
		read_file = open(read_file_path_name,"r")
	except IOError as err:
		logging.error('Error while opening read_file_path_name  - '+str(err))
		return False
	return True

def read_and_replace_lines(read_file,write_file_name,item_list,what_str,with_str):
	try:
		write_line=''
		what_str_list = what_str.split(',')
		with_str_list = with_str.split(',')

		for line in read_file:
			key_value = ['']
			if "=" in line:
				key_value =  line.split('=')
				logging.debug('Key Value.....'+str(key_value))
				logging.debug('item_list.....'+str(item_list))
			if (key_value[0] in item_list) or (len(item_list)==0):
				i=0
				for what_str in what_str_list:
					new_line = find_and_replace(line, what_str, with_str_list[i])
					line = new_line
					i+=1
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
		logging.debug("file_location - {0} / {1}, with {2}".format(file_location , original_file,tmp_file))
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

def close_config_files(read_file):
	try:
		read_file.close()
	except IOError as err:
		logging.error('Error while closing read_file / write files  - '+str(err))
		return False
	return True


def main():
	""" This is the main module """
	enable_logging()
	read_yaml('src/config/','ossim_rebrand_config.yaml')
	write_file_name = sensor_configs['menu-cfg.dest_file']+sensor_configs['menu-cfg.dest_file_ext']

	""" For menu.cfg file in /etc/ossim folder """
	if open_config_files(sensor_configs['menu-cfg.source_location'],sensor_configs['menu-cfg.source_file'],sensor_configs['menu-cfg.source_file_ext']):
		if read_and_replace_lines(read_file,sensor_configs['menu-cfg.source_location']+write_file_name,sensor_configs['menu-cfg.items_list'],sensor_configs['menu-cfg.replace_what'],sensor_configs['menu-cfg.replace_with']):
			if close_config_files(read_file):
				backup_and_rename_main_file(sensor_configs['menu-cfg.source_location'],sensor_configs['menu-cfg.source_file']+sensor_configs['menu-cfg.source_file_ext'],write_file_name)

	""" For menu-network.cfg file in /etc/ossim folder """
	if open_config_files(sensor_configs['menu-network-cfg.source_location'],sensor_configs['menu-network-cfg.source_file'],sensor_configs['menu-network-cfg.source_file_ext']):
		if read_and_replace_lines(read_file,sensor_configs['menu-network-cfg.source_location']+write_file_name,sensor_configs['menu-network-cfg.items_list'],sensor_configs['menu-network-cfg.replace_what'],sensor_configs['menu-network-cfg.replace_with']):
			if close_config_files(read_file):
				backup_and_rename_main_file(sensor_configs['menu-network-cfg.source_location'],sensor_configs['menu-network-cfg.source_file']+sensor_configs['menu-network-cfg.source_file_ext'],write_file_name)

	""" For ossim-setup.conf file in /etc/ossim-setup.conf folder """
	if open_config_files(sensor_configs['ossim-setup.source_location'],sensor_configs['ossim-setup.source_file'],sensor_configs['ossim-setup.source_file_ext']):
		if read_and_replace_lines(read_file,sensor_configs['ossim-setup.source_location']+write_file_name,sensor_configs['ossim-setup.items_list'],sensor_configs['ossim-setup.replace_what'],sensor_configs['ossim-setup.replace_with']):
			if close_config_files(read_file):
				backup_and_rename_main_file(sensor_configs['ossim-setup.source_location'],sensor_configs['ossim-setup.source_file']+sensor_configs['ossim-setup.source_file_ext'],write_file_name)

	""" for /etc/issue to change login screen """
	file_ext = sensor_configs['issue.source_file_ext']
	if None == file_ext:
		file_ext = ''

	if open_config_files(sensor_configs['issue.source_location'],sensor_configs['issue.source_file'],file_ext):
		if read_and_replace_lines(read_file,sensor_configs['issue.source_location']+write_file_name,sensor_configs['issue.items_list'],sensor_configs['issue.replace_what'],sensor_configs['issue.replace_with']):
			if close_config_files(read_file):
				backup_and_rename_main_file(sensor_configs['issue.source_location'],sensor_configs['issue.source_file']+file_ext,write_file_name)

	""" for /etc/motd.tail to change login screen. Will be replacing the motd.tail with issue file """
	if open_config_files(sensor_configs['motd-tail.source_location'],sensor_configs['motd-tail.source_file'],file_ext):
		if close_config_files(read_file):
			write_file_name = sensor_configs['issue.source_file']
			backup_and_rename_main_file(sensor_configs['motd-tail.source_location'],sensor_configs['motd-tail.source_file']+file_ext,write_file_name)

	""" for changing the hostname """
	file_ext = sensor_configs['hostname.source_file_ext']
	if None == file_ext:
		file_ext = ''
	write_file_name = sensor_configs['hostname.dest_file']+sensor_configs['hostname.dest_file_ext']

	if open_config_files(sensor_configs['hostname.source_location'],sensor_configs['hostname.source_file'],file_ext):
		if read_and_replace_lines(read_file,sensor_configs['hostname.source_location']+write_file_name,'',sensor_configs['hostname.replace_what'],sensor_configs['hostname.replace_with']):
			if close_config_files(read_file):
				backup_and_rename_main_file(sensor_configs['hostname.source_location'],sensor_configs['hostname.source_file']+file_ext,write_file_name)

	""" for changing the hosts file """
	file_ext = sensor_configs['hosts.source_file_ext']
	if None == file_ext:
		file_ext = ''
	write_file_name = sensor_configs['hosts.dest_file']+sensor_configs['hosts.dest_file_ext']

	if open_config_files(sensor_configs['hosts.source_location'],sensor_configs['hosts.source_file'],file_ext):
		if read_and_replace_lines(read_file,sensor_configs['hosts.source_location']+write_file_name,'',sensor_configs['hosts.replace_what'],sensor_configs['hosts.replace_with']):
			if close_config_files(read_file):
				backup_and_rename_main_file(sensor_configs['hosts.source_location'],sensor_configs['hosts.source_file']+file_ext,write_file_name)




if __name__ == '__main__':
    main()
