#Josue N Rivera 1/31/2020
import os

files = [f for f in os.listdir() if os.path.isfile(f)] # get all files

try:
	files.remove(os.path.basename(__file__)) # remove this script from the possible files
except Exception as e:
	raise e
	exit()

for file in files:
	try:
		end_std_name = file.index('_attempt')
		start_std_name = file[:end_std_name].rindex("_") + 1
	except Exception as e: # if file doesn't fit pattern skip
		print(" + " + file + " doesn't fit the pattern")
		continue

	hw = file[:start_std_name - 1] # get homework name
	student = file[start_std_name:end_std_name] # get student name
	os.renames(file, hw + "/" + student + "/" + file) # move file