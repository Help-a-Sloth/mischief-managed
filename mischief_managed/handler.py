import os
import time
from .variables import *

def recent_handler( directory, num_recents, files_info):

	"""
		Move number of recent files into "Recent" folder
	"""

	# Get all folder and files in diectory
	all_entities = os.listdir(directory)
	
	all_files = []
	
	for file in all_entities:
	
		fullpath = os.path.join(directory,file)
		# Only include files
		if os.path.isfile( fullpath ):
			all_files.append( fullpath )

	# Sort files by their last modified date
	recent_files = sorted(all_files, key=os.path.getmtime)[-num_recents:]

	recent_folder = os.path.join(directory,"Recent-{}".format(num_recents))
	# Create a recent folder
	os.mkdir(recent_folder)

	for recent_file in recent_files:
		file = os.path.basename(recent_file)
		new_path = os.path.join(recent_folder,file)
		os.rename( recent_file , new_path )

	files_info['Recent'] = recent_files


def check_ext_sanity( filename ):

		"""
			Check if file is not hidden, i.e check for period as first
			character filename and also extension is not empty
		"""

		extension = filename.split(".")[-1]

		if extension!="" and filename.strip()[0]!="." and not ( extension in non_permisable_ext ):
			return True, extension

		return False,None


def ext_handler(directory, files_info, use_def):

	"""
		Move files into subfolder based on extension of files
	"""

	# Get all files and folders
	all_entities = os.listdir(directory)

	for entity in all_entities:

		entity_path = os.path.join(directory,entity)

		if os.path.isfile( entity_path ):

			is_sane,extension = check_ext_sanity( entity )

			if is_sane:

				# By default use extension as folder name
				ext_folder = extension

				# If flagged to use general definitions,
				# provided in `variables`
				if use_def:
					if extension in ext_definition:
						ext_folder = ext_definition[extension]

				ext_folder_path = os.path.join( directory , ext_folder )

				if ext_folder in files_info:
					files_info[ ext_folder ].append(entity)
				else:
					files_info[ ext_folder ] = [ entity ]
					# Create folder for new folder
					os.mkdir( ext_folder_path )


				new_entity_path = os.path.join( ext_folder_path, entity )
				# Renaming does the job of moving
				os.rename( entity_path , new_entity_path )


def show_file_map(record):

	"""
		Display info of files moved into subfolders to tidy
	"""

	print( "-"*50 )
	print("\tFiles Managed Info - ")
	print( "-"*50 )

	for key,val in record.items():
		print( f" {key} files ==> {len(val)} " )


def date_handler(directory,files_info):

	"""
		Move files into subfolder based on last modified date of files
	"""

	# Get all files and folder
	all_entities = os.listdir(directory)

	for entity in all_entities:

		entity_path = os.path.join(directory,entity)

		# Only operate on files
		if os.path.isfile( entity_path ):

			# Get modification date in D-M-Y format
			modif_time = os.path.getmtime(entity_path)
			file_date = time.strftime("%d-%b-%Y", time.localtime(modif_time) )

			date_folder = os.path.join( directory , file_date )

			if file_date in files_info:
				files_info[ file_date ].append(entity)
			else:
				files_info[ file_date ] = [ entity ]
				# Create folder for new folder
				os.mkdir( date_folder )


			new_entity_path = os.path.join( date_folder	, entity )
			os.rename( entity_path , new_entity_path )





