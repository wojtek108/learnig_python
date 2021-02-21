import os
def selectiv_copy(inFolder):
	inFolder = os.path.abspath(inFolder)
	for folderName, subfolders, filenames in os.walk(inFolder):
		for file in filenames:
			if os.path.getsize(os.path.join(folderName, file)) > 100000000:
				print(os.path.join(folderName, file))

selectiv_copy('f:\\zzzzz')
