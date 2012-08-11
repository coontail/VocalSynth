#! /usr/bin/python
# -*- coding: UTF-8 -*-

exceptions = open("exceptions_fr.txt").read()
exceptions = exceptions.split("\n")

exceptions_api = open("exceptions_api.txt").read()
exceptions_api = exceptions_api.split("\n")

pairescolonnes = open("pairescolonnes.txt").read()
paires = pairescolonnes.split("\n")

regex_to_api = open("regex_to_api.txt").read()
regex_to_api = regex_to_api.split("\n")

regex = open("regex.txt").read()
regex = regex.split("\n")

consonnes =["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
consonnessansh =["b","c","d","f","g","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
voyelles=["a","e","i","o","u","y","é","è"]
replace=["-","\'","\"",",",":",";",".","(",")"]



def apitexte(texte):
	import re
	texte=texte.split()
	liste = []
	for mots in texte:
		for each in fr2:
			if re.search(each,mots):
				mots = re.sub(each,regex_to_api[fr2.index(each)],mots)
		liste.append(mots)
	return liste


def apimatch(texte):
	import re
	listevide = []
	bob = 0
	for each in replace:
		texte = texte.replace(each,"")
	texte=texte.split()
	for each in texte:
		listevide.append("")
	for mots in range(len(texte)):
		if texte[mots] in exceptions:
			listevide[mots]= exceptions_api[exceptions.index(texte[mots])]
			texte[mots] =""
		elif bob == 0:
			while len(texte[mots])!=0:
				bob =1
				for elements in range(len(regex)):
					if bob==1 and re.search(regex[elements],texte[mots]):
						delete = re.search(regex[elements],texte[mots])
						listevide[mots]= listevide[mots]+str(regex_to_api[regex.index(regex[elements])])
						delete = delete.end()
						texte[mots] = texte[mots][delete:len(texte[mots])]
						elements = 0
						bob = 0
	return listevide

def vox(texte):
	import subprocess
	import os
	api = apimatch(texte)
	api = "&".join(api)	
	replacefr = ["an","in","on","un"]
	replaceapi = ["α","ϵ","σ","π"]
	fichiers = []
	for elements in api:
		fichiers.append(str(elements)+".wav")
	subprocess.call(['sox']+fichiers+['out.wav'])
	print(fichiers)
	os.system("aplay out.wav")
	
def voxbi(texte):
	import subprocess
	import os
	api = apimatch(texte)
	api = "&".join(api)	
	replacefr = ["an","in","on","un"]
	replaceapi = ["α","ϵ","σ","π"]
	fichiers = []
	son =[]
	tailleapi = len(api)
	for each in range(len(api)):
		while len(api) !=0:
			if api.index(api[each])== len(api)-1:
				son.append(str(api[each]))
				api = api.replace(str(api[each]),"",1)
			elif str(api[each]+api[each+1]) not in paires:
				son.append(str(api[each]))
				api = api.replace(str(api[each]),"",1)
			
			elif str(api[each]+api[each+1]) in paires:
				son.append(str(api[each]+api[each+1]))
				api = api.replace(str(api[each]+api[each+1]),"",1)
	for elements in son:
		fichiers.append("paires/"+str(elements)+".wav")
	subprocess.call(['sox']+fichiers+['paires.wav'])
	os.system("aplay paires.wav")


