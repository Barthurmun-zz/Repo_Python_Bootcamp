#Author : Jakub Bryl


filename = 'ShowIpRoute.txt'
f = open(filename,'r')
txt = f.read()

import re

text = re.split(r"\n+", txt) # list of lines 

pattern = re.compile(r'^\w.*via.*') #Spliting ShowIpRoute on two parts, desc includes description of keys,
desc = re.compile(r'(\w+\d?\s-\s.*?)[,\n]') # pattern includes Routing table

foo = desc.finditer(txt)


lista = []
description = []
counter = 0
for line in text:
    if pattern.match(line):
        lista.append(line)
        counter+=1
for i in foo:
    description.append(i.group(1))

dic = {} #Dictionary with meaning of every index 
for elem in description:
    s = re.split(r" - ", elem)
    dic[s[0]] = s[1]

dic['E'] = 'EGP'
dic['H'] = 'NHRD' #Description not included in file

pattern1 = re.compile(r'\d+(.\d+){3}')
lista2 = [] #There are 2 types of routing informations in show ip route, here I make is 'same'
lista3 = []
for line in lista:
    if pattern1.match(line.split(' ') [1]):
        lista2.append(line)
    else:
        line = line.replace(line[1:4],'')
        lista3.append(line)
        
lista = lista2 + lista3         


Protocol =[i.split(' ') [0] for i in lista]
Prefix =[i.split(' ') [1] for i in lista]
AD_METRIC =[i.split(' ') [2] for i in lista]
Next_Hop =[i.split(' ') [4] for i in lista]
Time =[i.split(' ') [5] for i in lista]
Int =[i.split(' ') [6] for i in lista]


for nr in range(0,counter):
    val = dic[Protocol[nr]]
    AD_METRIC[nr] = AD_METRIC[nr][1:-1]
    Next_Hop[nr] = Next_Hop[nr][:-1]
    Time[nr] = Time[nr][:-1]
    print('Protocol:',val)
    print('Prefix:',Prefix[nr])
    print('AD/Metric:',AD_METRIC[nr])
    print('Next-Hop:',Next_Hop[nr])
    print('Last Update:',Time[nr])
    print('Outbound interface:',Int[nr],'\n')
