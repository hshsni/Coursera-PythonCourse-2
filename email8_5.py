#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message).
#Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
lst=list()
for line in fh:
    line=line.rstrip()
    if line.startswith('From:'):
        lst=line.split()
        print(lst[1])
        count+=1
print("There were", count, "lines in the file with From as the first word")
