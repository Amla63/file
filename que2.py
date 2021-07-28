file=open("exercise.txt","r")
file_data=file.readlines()
i=0
while i<len(file_data):
    i=i+1
print(i)
file.close()