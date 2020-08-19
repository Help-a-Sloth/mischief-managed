import argparse
from .handler import *

def main():

	parser = argparse.ArgumentParser( 
										description= ("Files outside any folder are "
										"made tidy by putting inside folder based on "
										"their extension or date")
									)

	parser.add_argument(
			"--path",
			type=str,
			default=".",
			help="Directory to manage or target"
		)

	parser.add_argument(
		"--ext",
		type=bool,
		default=True,
		help="Flag if to tidy the files into the extension based folders"
		)

	parser.add_argument(
		"--use-def",
		action='store_true',
		help="Flag to use general folder name like 'Images' for extensions -  jpg,png etc "
		)

	parser.add_argument(
		"--date",
		action='store_true',
		help="Flag if to tidy the files into the date based folders"
		)

	parser.add_argument(
		"-r",
		"--recent",
		type=int,
		default=0,
		help="Give number of files to include in recently created files"
		)

	# Get all arguments given as Namespace object
	args = parser.parse_args()

	# Store info about type of files
	files_info = {}

	if args.recent!=0:
		# To create recent folder with atmost given number of files
		recent_handler(args.path,args.recent,files_info)

	# If data flag is given, make date folders else
	# extension folders are created default
	if args.date:
		date_handler(args.path,files_info)
	else:
		ext_handler(args.path,files_info, args.use_def )	

	show_file_map(files_info)

	print("\n** Made by Help-a-Sloth org. Check out on github.**")

if __name__=='__main__':
	main()


