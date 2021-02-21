import os, shutil
def selectiv_copy(inFolder, outFolder, ext):
	outFolder = os.path.abspath(outFolder)
	inFolder = os.path.abspath(inFolder)

	#create outFolder folder if it doesn't exist
	if not os.path.exists(outFolder):
		os.makedirs(outFolder)

	for folderName, subfolders, filenames in os.walk(inFolder):
		for file in filenames:
			if file.endswith(ext):
				shutil.copy(os.path.join(folderName, file), outFolder)
				print(file)

selectiv_copy('f:\\learning\\Python\\', 'f:\\zzzzz', 'csv')
