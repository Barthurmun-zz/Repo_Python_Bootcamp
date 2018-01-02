#Author: Jakub Bryl

filename = 'command.txt'

with open(filename,'r') as f: 
    txt = f.readlines()
 
import re

pattern = re.compile(r'\bswitchport trunk allowed vlan (\d).*\b')  #Finding right lines 


lista = []
counter = 0
for line in txt:
    if pattern.match(line): 
        lista.append(line)
        counter+=1
        
nums = [i.strip().split(' ') [4] for i in lista] #Taking from list just nr. of Vlan's

n = []
for i in nums:
    for e in i.split(','):
        n.append(e)  

dic = {}
for i in n:
    if i in dic.keys():
        dic[i] = dic[i]+1   #Dictionary with two numbers, first one represent number of VLAN, second one is nr.of repeats in file
    else:
        dic[i] = 1  

l_only_one = []
l_every_time = []
for key in dic.keys():
    if dic[key] == 1:
        l_only_one.append(key)
    elif dic[key] == counter:
        l_every_time.append(key)
   
l_only_one.remove('')
        
for idx,nr in enumerate(l_only_one):
    l_only_one[idx]=int(l_only_one[idx])
for idx,nr in enumerate(l_every_time):
    l_every_time[idx]=int(l_every_time[idx])
    
 
print("All unique values : " , sorted(l_only_one))
print("All common vlans : " , sorted(l_every_time)) 


