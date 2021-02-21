# the script makes use of glob() method

from pathlib import Path 
import os, shutil
def selectiv_copy(inFolder, outFolder, ext):
	outFolder = os.path.abspath(outFolder)
	inFolder = os.path.abspath(inFolder)
	ext2 = str('*.' + ext)
	#create result folder if it doesn't exist
	if not os.path.exists(outFolder):
		os.makedirs(outFolder)
	for folderName, subfolders, filenames in os.walk(inFolder):
		p1 = Path(folderName) 
		for filename in p1.glob(ext2):  # search for files using glob method
			print(filename)
			shutil.copy(os.path.join(folderName, filename), outFolder)


selectiv_copy('c:\\Users\\User\\Downloads', 'f:\\zzzzz', 'pdf')
