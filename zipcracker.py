#!/usr/bin/env python
import zipfile
import argparse

__author__ = 'mustafauzun0'

'''
  ___________ _____   _____ _____            _____ _  ________ _____  
 |___  /_   _|  __ \ / ____|  __ \     /\   / ____| |/ /  ____|  __ \ 
    / /  | | | |__) | |    | |__) |   /  \ | |    | ' /| |__  | |__) |
   / /   | | |  ___/| |    |  _  /   / /\ \| |    |  < |  __| |  _  / 
  / /__ _| |_| |    | |____| | \ \  / ____ \ |____| . \| |____| | \ \ 
 /_____|_____|_|     \_____|_|  \_\/_/    \_\_____|_|\_\______|_|  \_\
                                                                                                                                    
'''

def helpMe():
	return '''
		ZipCracker
	'''

def main():
	parser = argparse.ArgumentParser(description=helpMe())

	parser.add_argument('-f', '--file', dest='file', help='File Path and Name', required=True)
	parser.add_argument('-d', '--dictionary', dest='dictionary', help='Dictionary Path and Name', required=True)

	args = parser.parse_args()

	zipFilePath = args.file
	dictionaryFilePath = args.dictionary
	
	try:
		zipFile = zipfile.ZipFile(zipFilePath)
	except:
		print('[-] Zip file not found please file path check')
		return

	dictionary = open(dictionaryFilePath)

	for line in dictionary.readlines():
		password = line.strip('\n')
		try:
			zipFile.extractall(pwd=password)
			print('[+] Password found: ' + password)
			return
		except:
			pass
		
	print('[-] Password not found.')

if __name__ == '__main__':
	main()
