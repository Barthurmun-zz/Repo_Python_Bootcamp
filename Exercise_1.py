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

print(IP)

mask = mask.split('/')[1]

mask = int(mask)
ones = 2**32-1 #Maximym mask value

num = (ones << 32-mask)& ones #making C-like uint8_t

bnum = bin(num).split('b')[1] #Binary representation of mask

bbask = [bnum[0:8], bnum[8:16], bnum[16:24], bnum[24:32]] #Sorted into 4 octets
print(bbask)

bmask = [int(i,2) for i in bbask] #Decimal representation of bbask

print('Network address :',[ ip&mask for ip, mask in zip(IP, bmask)]) #Network address

print('Broadcask address :',[ ip|(255-mask) for ip, mask in zip(IP, bmask)]) #Broadcast address

