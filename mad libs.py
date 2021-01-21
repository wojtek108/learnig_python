''' The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events. '''

from pathlib import Path 
testFile = open(Path.home() / 'madlibs.txt')
content = testFile.read()
punctuationList = ['.', ',', '?', '!', '*']
for item in punctuationList:
	if item in content:
		a = str(item)
		b = str (' ' + item + ' ')
		content = content.replace(a, b)

contentList = content.split()

for index, item in enumerate(contentList):
	if item == 'ADJECTIVE':
		print('Enter an adjective:')
		userAdjective = str(input())
		contentList[index] = userAdjective
	elif item == 'NOUN':
		print('Enter a noun:')
		userNoun = str(input())
		contentList[index] = userNoun
	elif item == 'VERB':
		print('Enter a verb:')
		userVerb = str(input())
		contentList[index] = userVerb

listToStr = ' '.join([elem for elem in contentList]) 


for item in punctuationList:
	a = str(' ' + item + ' ')
	if a in listToStr:
		b = str(item + ' ')
		listToStr = listToStr.replace(a, b)
	c = str(' ' + item)
	if c in listToStr:
		d = str(item + ' ')
		listToStr = listToStr.replace(c, d)
# print(contentList)
print(listToStr)

testFile.close()