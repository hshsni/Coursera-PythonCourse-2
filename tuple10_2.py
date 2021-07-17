#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
lst=list()
hour=dict()
for line in fh:
    line=line.rstrip()
    if line.startswith('From '):
        t=line.split()[5].split(':')
        hour[t[0]]=hour.get(t[0],0)+1
for key,val in hour.items():
    lst.append((key,val))
lst.sort()
for key,val in lst:
    print(key,val)     