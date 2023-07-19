def edit_file(file_path):
  # Open the file and make your edits
	with open(file_path, "a") as f:
		f.write("\n console.log('hello');")