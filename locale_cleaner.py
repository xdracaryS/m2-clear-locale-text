# dracaryS
import glob
import os
import sys

bArg = ['(','[',':']
gArg= ['\t','\n',',',')',' ','%','+',']']

maxArgCount = 5 # max arg in one line...

USING_UISCRIPTLOCALE_FILE = 1
# if you don't using uiscriptlocale file so set to 0

fileTypes = ["","uiscript/"]
localeData = []
oldlocaleDataFileNames = ["locale_game.txt"]
oldlocaleData = []
localeFileName= ["localeinfo"]
localeData.append([])
oldlocaleData.append([])

if USING_UISCRIPTLOCALE_FILE:
	localeFileName= ["localeinfo","uiscriptlocale"]
	oldlocaleDataFileNames = ["locale_game.txt","locale_interface.txt"]
	localeData.append([])
	oldlocaleData.append([])

calculateMaxCount = 0
calculateReadCount = 0

for fileName in oldlocaleDataFileNames:
	try:
		lines = open(fileName).readlines()
	except:
		print fileName+" this file not exist!"
		os.system("PAUSE")
		sys.exit()
	for line in lines:
		calculateMaxCount+=1

for fileName in oldlocaleDataFileNames:
	index = oldlocaleDataFileNames.index(fileName)
	lines = open(fileName).readlines()
	for line in lines:
		lineList = line.split('\t')
		item =[]
		for j in lineList:
			j_index = lineList.index(j)
			if j_index == len(lineList)-1:
				j = j[:-1]
			item.append(j)
		#print item
		oldlocaleData[index].append(item)

		calculateReadCount+=1
		print "Locale files reading status: %d\n"% (calculateReadCount*float(float(100)/float(calculateMaxCount)))

def countofText(str):
	count = 0
	for i in str:
		count += 1
	return count

def checkText(arg, localtext):
	dotCount = 0
	for i in arg:
		if i >= 'a' and i <= 'z' or i >= '0' and i <= '9':
			continue
		if i == '.':
			dotCount+=1
			if dotCount > 1:
				return False
		for j in bArg:
			if i == j:
				return False
		for j in gArg:
			if i == j:
				if dotCount == 0:
					return False
				index = localeFileName.index(localtext)
				if not arg[countofText(localtext)+1:arg.find(i)] in localeData[index]:
					localeData[index].append(arg[countofText(localtext)+1:arg.find(i)])
				return True
	return False

calculateMaxCount = 0
calculateReadCount = 0

for localtext in localeFileName:
	for types in fileTypes:
		for fileName in glob.glob("%s*.py"%types):
			for line in lines:
				calculateMaxCount+=1

for localtext in localeFileName:
	for types in fileTypes:
		for fileName in glob.glob("%s*.py"%types):
			lines = open(fileName).readlines()
			for line in lines:
				arg = 0
				if line.find("import") != -1:
					continue
				for j in xrange(maxArgCount):
					arg = line.lower().find(localtext)
					if arg == -1:
						break
					checkText(line[arg:],localtext)
					line = line[arg+1:]

				calculateReadCount+=1
				print "Python files reading status: %d\n"% (calculateReadCount*float(float(100)/float(calculateMaxCount)))

def getOldLocaleItems(text, type):
	index = localeFileName.index(localeName)
	for item in oldlocaleData[index]:
		if text == item[0]:
			return item
	return 0

calculateMaxCount = 0
calculateReadCount = 0
for localeName in localeFileName:
	index = localeFileName.index(localeName)
	for text in localeData[index]:
		calculateMaxCount+=1

for localeName in localeFileName:
	index = localeFileName.index(localeName)
	localeData[index].reverse()
	localeFile = open("new_"+oldlocaleDataFileNames[index],"w+")
	for text in localeData[index]:
		item = getOldLocaleItems(text,localeName)
		if item == 0:
			localeFile.write(text+"\tNone Text\n")
		else:
			if len(item) == 3:
				text = item[0]+'\t'+item[1]+'\t'+item[2]+'\n'
			else:
				text = item[0]+'\t'+item[1]+'\n'
			localeFile.write(text)
		
		calculateReadCount+=1
		print "Creating new locale files status: %d\n"% (calculateReadCount*float(float(100)/float(calculateMaxCount)))
	localeFile.close()

print "Work is done!\n "
print "Check this files:\n "
print "new_locale_game.txt\n"
if USING_UISCRIPTLOCALE_FILE:
	print "new_locale_interface.txt\n"
print "by dracaryS\n"
print "discord: dracaryS#9089"
print "skype: kuun_12"
os.system("PAUSE")
