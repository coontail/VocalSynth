#! /usr/bin/python
# -*- coding: UTF-8 -*-

consonnes =["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
consonnessansh =["b","c","d","f","g","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]

voyelles=["a","e","i","o","u","y","é","è"]


fr =["a","â","é","ez","er$","ai","è","ô","eau","au","ö","o","eu$","eu","u","^eu$","ou","oû","hou","on","un$","ein","ain","in$","^in","im","on","an","i","î","ï","b","ss","s"+str(consonnes),"ce","ça","c"+str(consonnessansh),"k","^ch","d","f","ff","ga","go","gu","gno","ge","g","j","l","ll","m","mm","n","nn","p","pp","r","rr","t","tt","v","w","z","^s"+str(voyelles),"s"+str(voyelles),"ch","sh","gn","y"+str(voyelles),"ouet","ouai","^ou","ui","t$","x$","s$","ent$","e$",]

api = ["a","a","e","e","e","ê","ë","ö","ï","à","ɛ","ɛ","o","o","o","o","ɔ","ø","œ","y","y","u","u","u","ɔ̃","œ̃","ɛ̃","ɛ̃","ɛ̃","ɛ̃","ɛ̃","ɔ̃","ɑ̃","i","i","i","b","s","s","sə","sa","k","k","k","d","f","f","ga","go","g","gno","ʒɛ","ʒ","ʒ","l","ll","m","m","n","n","p","p","r","r","t","t","v","v","z","s","z","ʃ","ʃ","ɲ","j","wɛ","wɛ","w","µi","","","","",""]



fr2 = ["aille","eille","s(?=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'])", "c(?=['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'])","^s(?=['a', 'e', 'i', 'o', 'u', 'y'])", "s(?=['a', 'e', 'i', 'o', 'u', 'y'])", "y(?=['a', 'e', 'i', 'o', 'u', 'y'])","ment$", "e(?="+str(consonnes)+"{2})","^an(?="+str(voyelles)+")","^en(?="+str(voyelles)+")","^en(?="+str(consonnes)+")","qu",'^eu$', 'ent$', 'ouai', 'ouet', '^ch(?='+str(consonnes)+")", '^in', '^ou', 'ain', 'eau', 'ein', 'er$', 'eu$', 'gno', 'hou', 'in$', 'un$', 'ai', 'an', 'au', '^ce$','ce', '^ch(?='+str(voyelles)+")", 'eu', 'ez', 'ff', 'ga', 'ge', 'gn', 'go', 'gu', 'im', 'mm', 'nn', 'on', 'ou', 'oû', 'pp', 'rr', 's$', 'sh', 'ss', 't$', "e$",'tt', 'ui', 'x$', 'ça', 'a', 'b', 'd', 'f', 'g', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 't', 'u', 'v', 'w', 'z', 'â', 'è', 'é', 'î', 'ï', 'ô', 'ö']

api2 = ["u","a","ɛz","ɑ̃","g","g","ʒ","ij","l","wa","s","ɛn","iz","an","ɔn","ɔ̃","wɛ̃","","","le","ʒ","","l","s","sɛ̃","i","","t","in","f","j","ɑ̃","øz","ɛ","aj","ɛj",'s', 'k',"k","s","s", 'z','j','mɑ̃','ɛ','e','an','en','ɑ̃','k','y', '', 'wɛ', 'wɛ', 'k', 'ɛ̃', 'w', 'ɛ̃', 'o', 'ɛ̃', 'e', 'ø', 'gno', 'u', 'ɛ̃', 'œ̃', 'ɛ', 'ɑ̃', 'o', 'sə','sɛ', 'ʃ', 'œ', 'e', 'f', 'ɲ', 'ɛ̃', 'm', 'n','on', 'ɔ̃', 'u', 'p', 'r', '', 'ʃ', 's', '','', 't', 'µi', '', 'sa', 'a', 'b', 'd', 'f', 'ʒ', 'i', 'ʒ', 'k', 'm', 'n', 'ɔ', 'p', 'r', 't', 'y', 'v', 'w', 'z', 'a', 'ɛ', 'e', 'i', 'i', 'o', 'o',"k","e","ɛ"]


prout = ["^(ou|ou$)","^à$","^aise$","^en$","^gu","^g(?=['o','a','u'])","^g(?=['e','i','y'])","^ille","^(l|ll)","^oi","^t(?=['i'])","^aine$","^ys","^an(?="+str(voyelles)+")","^onne$","^on$","^oin$","^t$","^p$","^les$","^j\'","^h(?="+str(voyelles)+")","^l\'","^c\'","^sym(?="+str(consonnes)+")","^y(?="+str(consonnes)+")","^es$","^th","^ine$","^ph","^i(?=['a','i','o','u'])","^and$","^euse$","^est$","^aille","^eille","^s(?=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'])", "^c(?=['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'])","^c(?=['a','u','o'])","^c(?=['e','y','i'])","^s(?=['a', 'e', 'i', 'o', 'u', 'y'])", "^s(?=['a', 'e', 'i', 'o', 'u', 'y'])","^y(?=['a', 'e', 'i', 'o', 'u', 'y'])","^ment$", "^e(?="+str(consonnes)+"{2})","^e(?="+str(consonnes)+"{1})","^an(?="+str(voyelles)+")","^en(?="+str(voyelles)+")","^en(?="+str(consonnes)+")","^qu",'^eu$', '^ent$', '^ouai', '^ouet', '^ch(?='+str(consonnes)+")", '^in', '^ou(?='+str(voyelles)+")", '^ain', '^eau', '^ein', '^er$', '^eu$', '^gno', '^hou', '^in$', '^un$', '^ai', '^an', '^au', '^ce$','^ce', '^ch(?='+str(voyelles)+")", '^eu', '^ez', '^ff', '^gn', '^im', '^mm', '^nn','^on(?='+str(voyelles)+")", '^on(?='+str(consonnes)+")", '^oû', '^pp', '^rr', '^s$', '^sh', '^ss', '^t$', "^e$",'^tt', '^ui', '^x$', '^ça', '^a', '^b', '^d', '^f', '^g', '^i', '^j', '^k', '^m', '^n', '^o', '^p', '^r', '^t', '^u', '^v', '^w', '^z', '^â', '^è', '^é', '^î', '^ï', '^ô', '^ö',"^c$","^é","^è"]



def apitexte(texte):
	import re
	texte=texte.split()
	caca = []
	for mots in texte:
		for each in fr2:
			if re.search(each,mots):
				mots = re.sub(each,api2[fr2.index(each)],mots)
		caca.append(mots)
	return caca
	
def apimatch(texte):
	import re
	listevide = []
	bob = 0
	texte=texte.split()
	for each in texte:
		listevide.append("")
	for mots in range(len(texte)):
		if bob == 0:
			while len(texte[mots])!=0:
				bob =1
				for elements in range(len(prout)):
					if bob == 1:
						if re.search(prout[elements],texte[mots]):
							delete = re.search(prout[elements],texte[mots])
							listevide[mots]= listevide[mots]+str(api2[prout.index(prout[elements])])
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
	replaceapi = ["ɑ̃","ɛ̃","ɔ̃","œ̃"]
	fichiers = []
	for elements in api:
		fichiers.append(str(elements)+".wav")
	subprocess.call(['sox']+fichiers+['out.wav'])
	print(fichiers)
	os.system("aplay out.wav")
	
	

