#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
lst=list()
wd=list()
count=dict()
for line in fh:
    line=line.rstrip()
    if line.startswith('From:'):
        lst=line.split()
        wd.append(lst[1])
for key in wd:
    count[key]=count.get(key,0)+1
bigw=None  
bigc=None
for key,value in count.items():
    if bigc is None or value>bigc:
        bigw=key
        bigc=value
print(bigw,bigc)