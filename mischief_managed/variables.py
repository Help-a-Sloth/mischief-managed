# Extensions not to be touched
non_permisable_ext = [
		"ini"
	]

definition_ext = {
	"Images" : ['jpg',"png","jpeg"],
	"Application" : ["exe"],
	"Compressed" : ["7z","zip","gzip","rar"],
	"Documents" : ["txt","doc","docx","pdf"],
}

# Create hashmap of mapping extension to their general names
ext_definition = {}
for general_def in definition_ext:

	ext_list = definition_ext[ general_def ]
	for ext in ext_list:
		ext_definition[ext] = general_def


