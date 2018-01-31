#Author: Jakub Bryl
import re

ip = input('\nEnter Ip address:') #Checking if IP address is allowed (right one)
pattern1 = re.search('^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]).([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]).([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]).([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))$',ip)

while pattern1 == None:
    print('IP Address is invalid\n')
    ip = input("Enter ip address:")
    pattern1 = re.search('^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]).([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]).([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]).([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))$',ip)

ip=pattern1.group(0)
            
mask = input("Enter subnet mask in decimal format:") #Same thing as above, just for mask, REMEMBER TO WRITE mask with "/"
pattern2 = re.search('^/([0-9]|[1-2][0-9]|3[0-2])$',mask)

while pattern2 == None:
    print('Subnet mask is invalid\n')
    mask = input("Enter subnet mask in decimal format:")
    pattern2 = re.search('^/([0-9]|[1-2][0-9]|3[0-2])$',mask)
    
mask = pattern2.group(0)

IP = ip.split('.')

IP =[int(i) for i in IP]

IP_bin = [f'{z:08b}' for z in IP]

mask = mask.split('/')[1]

mask = int(mask)

ones = 2**32-1 #Maximym mask value

num = (ones << 32-mask)& ones #making C-like uint8_t

bnum = bin(num).split('b')[1] #Binary representation of mask

bbask = [bnum[0:8], bnum[8:16], bnum[16:24], bnum[24:32]] #Sorted into 4 octets

bmask = [int(i,2) for i in bbask] #Decimal representation of bbask

network = [ ip&mask for ip, mask in zip(IP, bmask)]
broadcast = [ ip|(255-mask) for ip, mask in zip(IP, bmask)]
ip_out = str(IP[0]).rjust(7)+' '+str(IP[1]).rjust(8)+' '+str(IP[2]).rjust(8)+' '+str(IP[3]).rjust(8)
ip_binout = (IP_bin[0].rjust(7))+' '+(IP_bin[1].rjust(8))+' '+(IP_bin[2].rjust(8))+' '+(IP_bin[3].rjust(8))
bbask_out = str(bbask[0])+' '+str(bbask[1])+' '+str(bbask[2])+' '+str(bbask[3])
network_out = str(network[0])+'.'+str(network[1])+'.'+str(network[2])+'.'+str(network[3])+'/'+str(mask)
broadcast_out = str(broadcast[0])+'.'+str(broadcast[1])+'.'+str(broadcast[2])+'.'+str(broadcast[3])+'/'+str(mask)
print(ip_out)
print(ip_binout)
print('Network address:',network_out)
print('Broadcast address: ',broadcast_out)