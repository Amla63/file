var=["76","54","43","21"]
my_file2 = open("var.txt", "w")
i=0
while i<len(var):
    my_file2.write(var[i])
    my_file2.write(" ")
    i=i+1
# print(my_file2)
# my_file2.write(var)
# my_file2.write("Ranveer - Delhi")
my_file2.close()