# This is a draft. The solution is pretty crude.

import os, random, shutil
from pathlib import Path


def createFiles(dir, prefix):
	if not os.path.exists(dir):
			os.makedirs(dir)

	os.chdir(dir)
  
  # create a set of 20 files with given prefix in a given directory. For the sake of demonstration I chose to create text files (*.txt). Could use regex to 
  # search for any type of files. 
	for n in range(1,21):
		if n <= 9:
			s = prefix + '00' + str(n)
			f = open(s + '.txt', 'w')
			f.close()
		else:
			s = prefix + '0' + str(n)
			f = open(s + '.txt', 'w')
			f.close()

	fileList = os.listdir(dir)
	r = random.randint(1,18)
	selectFile = fileList[r]
	print('Initial number of items in a list ' + str(len(fileList)) +'. Deleting file number ' + str(r + 1) + ': ' + selectFile)

	delFile = os.path.join(dir, selectFile)
	os.unlink(delFile)

	p1 = Path(delFile)
	fileStem = p1.stem
	# newStem = fileStem.replace('spam', '')
	indexStem = int(fileStem.strip(prefix))
	fileList1 = os.listdir(dir)
	print('Number of items in a new list ' + str(len(fileList1)))

  # create a list of int from file names
	indexList = []
	for f in fileList1:
		f2 = Path(os.path.join(dir, f))
		f3 = f2.stem
		iindex = int(f3.strip(prefix))
		indexList.append(iindex)
    
  # determine the gap number
	for n in range(1, len(indexList)):
		if indexList[n-1] != indexList[n]-1:
			elem = indexList[n] 
			indexN = indexList.index(elem)
      
	# create a new list with int sequence without the gap
	bList = [n - 1 for n in (indexList[indexN:])]
	cList = indexList[:indexN]
	finalList = cList + bList
	
	# create a list of file names withouth the gap
  fileNames = []
	for ffile in finalList:
		if ffile < 10:
			newFile = prefix + '00' + str(ffile) + '.txt'
			fileNames.append(newFile)
		else:
			newFile = prefix + '0' + str(ffile) + '.txt'
			fileNames.append(newFile)

  # create a list of complete paths to new files
	pathsList = []
	for dFile in fileNames:
		nnFile = (os.path.join(dir, dFile))
		pathsList.append(nnFile)


	print(pathsList)

  # rename files
	for a in range(19):
		x = fileList1[a]
		y = pathsList[a]
		shutil.move(x, y)



dirTest = 'f:\\zzzz'
prefixTest = 'wg'

createFiles(dirTest, prefixTest)
