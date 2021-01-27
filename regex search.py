from pathlib import Path
import re

print('Give me a string/regex to search for:')
searchString = str(input())
p1 = Path('f:/some path/stuff/')
txtList = list(p1.glob('*.txt'))
hit = re.compile(searchString)
for n in txtList:	
	with open(n) as f:	
		mo = hit.search(f.read())
		if mo:
			print('YES! Match:  ' + mo.group() + ' found in: ' + str(n))