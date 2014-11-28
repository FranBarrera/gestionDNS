# -*- coding: utf-8 -*-

import sys
import os
dns = open('/var/cache/bind/db.tronos', 'a')

modo = sys.argv[1]

if modo == '-a':
	tipo = sys.argv[2]
	nombre = sys.argv[3]
	alias = sys.argv[4]

	if tipo == '-dir':
		inv = open('/var/cache/bind/db.192','a')
		dns.write(nombre+'    IN    A       '+alias+'\n')
		inv.write(alias+'    IN    PTR    '+nombre+'.tronos.com.\n')
		inv.close()
	elif tipo == '-alias':
		dns.write(nombre+'      CNAME   '+alias+'\n')
dns.close()

if modo == '-b':
#solo elimina si la línea tiene una palabra
	nombre = sys.argv[2]

	dns = open("/var/cache/bind/db.tronos","r")
	lineas = dns.readlines()

	dns.close()

	dns = open("/var/cache/bind/db.tronos","w")

	for linea in lineas:
		if linea != nombre+"\n":
			dns.write(linea)
os.system('service bind9 restart')

dns.close()









