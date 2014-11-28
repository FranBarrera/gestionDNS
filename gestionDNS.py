# -*- coding: utf-8 -*-

import sys

dns = open('/home/fran/dns', 'a')

modo = sys.argv[1]

if modo == '-a':
	tipo = sys.argv[2]
	nombre = sys.argv[3]
	alias = sys.argv[4]

	if tipo == '-dir':
	        dns.write(nombre+'      A       '+alias+'\n')

	elif tipo == '-alias':
		dns.write(nombre+'      CNAME   '+alias+'\n')
	dns.close()

if modo == '-b':
	nombre = sys.argv[2]

	dns = open("/home/fran/dns","r")
	lineas = dns.readlines()

	dns.close()

	dns = open("/home/fran/dns","w")

	for linea in lineas:
		if linea != nombre+"\n":
			dns.write(linea)

dns.close()









