#! /usr/bin/python
# -*- coding: UTF-8 -*-

import re
import subprocess
import os
import json

exceptions = json.loads(open("../data/phono.json").read())
paires_disponibles = open("../data/paires_disponibles.csv").read().split()
useless_chars = "([•|—|–|\-|\’|,|?|!|^|\r|°|“|”|...|«|»|…|\\|\/|!|?|\"|\'|\[|\]|\(|\)|\]|<|>|=|+|%|$|&|#|;|*|:|}|{|`|\s\s])"

def parse_csv(file):
	dictionary = {}
	conversion = open(file).read().split("\n")
	for element in conversion :
		rule = element.split("#")
		dictionary[rule[0]] = rule[-1]
	return dictionary

conversion = parse_csv("../data/conversion.csv")

def apimatch(texte):
	texte = re.sub(useless_chars," ",texte).lower().split()
	api = []
	for words in texte:
		if words in exceptions.keys():
			api.append(exceptions[words])
		else :
			api.append("")
			while len(words):
				for rule in conversion.keys():
					if re.match(rule,words):
						api[-1] += conversion[rule]
						words = re.sub(rule,"",words)
	return api
	
def voxbi(texte):
	api = apimatch(texte)
	api = "_".join(api)	
	fichiers = []
	son = []
	for index in range(len(api)):
		while len(api):
			if index == len(api)-1:
				son.append(api[index])
				api = api.replace(api[index],"",1)
			elif api[index]+api[index+1] in paires_disponibles:
				son.append(api[index]+api[index+1])
				api = api.replace(api[index]+api[index+1],"",1)
			else :
				son.append(api[index])
				api = api.replace(api[index],"",1)
	for paire in son:
		fichiers.append("../data/paires/"+paire+".ogg")
	subprocess.call(['sox']+fichiers+['../data/vocal.wav'])
	os.system("aplay ../data/vocal.wav")


