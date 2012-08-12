#!/usr/bin/env python                                                                                         
# coding:utf8
#
# Author: Lichain.Yu (lichain) <airy.cloud@gmail.com>
# Copyright: Lichain.Yu (lichain) <airy.cloud@gmail.com>
# License: MIT 
#

##read input data
volatile_settings = {
	'file_name':'test.cs',
	'type':'1',
	'class_name':'sp_input'
	}

data_member =[
	'test1',
	'test2',
	'test3',
	'test4'
	]


data =""
file = open('template.txt','r')
while True:
	line = file.readline()
	if(len(line)==0):
		break

	if('##file_name##' in line):
		data += line.replace('##file_name##',volatile_settings['class_name'])
	elif('##data_member##' in line):
		context =""
		for s in data_member:
			context += "\tpublic string " + s + " {get; set;}\n"
		data += line.replace('##data_member##',context)
	else:
		data += line
		#break;
#	data += line

file.close()

print data

fout = open("test.cs", "w")
fout.write(data)
fout.close()

#print volatile_settings['file_name']

#for s in data_member:
	#print s
