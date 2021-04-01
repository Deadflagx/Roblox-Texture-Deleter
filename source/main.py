# -*- coding: utf-8 -*-
import os 
import ctypes
from sys import exit
import json
import traceback
import sys
import logging
import shutil
import time

			
def main():
	pass

def show_msgbox(text, title):
	ctypes.windll.user32.MessageBoxW(0, text, title, 0)
	exit(0)

def get_version(path):
	for file in os.listdir(path):
		if 'version' in file.lower():
			return f'{path}/{file}/PlatformContent/pc/textures'
	#if version not found
	logging("Get Version Error\n"+traceback.format_exc())
	show_msgbox('Version Not Found\nContact The Developer', 'Version Not Found')

def getall_dir(path):
	files = os.listdir(path)
	return [files.lower() for files in files if os.path.isdir(f'{path}\\{files.lower()}')]

def get_setings():
	try:
		f = open('settings')
		jsonsettings = json.loads(f.read())
		f.close()
		only_true_sets = {k: v for k, v in jsonsettings.items() if v}
		return [only_true_sets for only_true_sets in only_true_sets]
	except ValueError:
		logging.error("Error In Setting\n"+traceback.format_exc())
		show_msgbox('Error In Setting File\nCheck Settings File', 'Bad Setting File')
	except FileNotFoundError:
		logging.error("Setting File Not Found\n"+traceback.format_exc())
		show_msgbox('Settings File Not Found\nCheck Settings File', 'Settings Not Found')	
	except Exception as e:
		logging.error("Unknown Error\n"+traceback.format_exc())

		"""
		ex_type, ex_value, ex_traceback = sys.exc_info()
		trace_back = traceback.extract_tb(ex_traceback)
		stack_trace = list()
		for trace in trace_back:
			stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))

		print("Exception type : %s " % ex_type.__name__)
		print("Exception message : %s" %ex_value)
		print("Stack trace : %s" %stack_trace)
		"""


def create_backup_folder(path):
	if not os.path.exists(path+'/Backup Textures'):
		os.mkdir(path+'/Backup Textures')

def clear_backup(backup_path):
	dirs = os.listdir(backup_path)
	[shutil.rmtree(f'{backup_path}/{directory}') for directory in dirs]
	

def move_textures_to_backup(path, path_to, settings):
	for folder in settings:
		try:
			shutil.move(f'{path}/{folder}', path_to)
		except OSError as e:
			logging.error(e)
			show_msgbox(str(e), 'No such file or directory')

		

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG, filename='error.log', format='%(asctime)s %(levelname)s:%(message)s', filemode="w")
	logging.info("Applicationg Run")
	current_username = os.getlogin()
	version_path = f'C:/Users/{current_username}/AppData/Local/Roblox/Versions'
	path = get_version(version_path)
	directories = getall_dir(path)
	settings = get_setings()
	create_backup_folder(path)
	clear_backup(f'{path}/Backup Textures')
	move_textures_to_backup(path, f'{path}/Backup Textures', settings)
	#main()





