# file_data=["rishabh - meerut","imtiyaz - delhi","nilima - cochin","rati - shimla","ayishah - delhi","raghu - shimla","naseer - kanpur","karthikeyan - delhi","salma - jaipur","pankaj - delhi"]
f=open("question4.txt","r")
file1=open("delhi.txt","w")
file2=open("shimla.txt","w")
file3=open("other.txt","w")
file=f.read()
file_data=file.split("\n")
# print(file_data)
i=0
while i<len(file_data):
    if "delhi" in file_data[i]:
        file1.write(file_data[i])
        file1.write("\n")
      
    elif "shimla" in file_data[i]:
        file2.write(file_data[i])
        file2.write("\n")
    else:
        file3.write(file_data[i])
        file3.write("\n")
    i+=1                                                
print(file1)
# print(file2)
# print(file3)
