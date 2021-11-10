# This is the way to make the file and give it to the variable name for the later use u can say

fname = "hello.txt"
# This is the way to open the file to wrute something in the file

f_object = open(fname, "w")
# This is the way to write something in the file system
f_object.write("Hellow this is faizan tanveer and making the file system in the python")

f_object.close()

# There is another way to write the programe in same file system

with open(fname, "w") as f_object:
    f_object.write("This is another method to write something in the file system")



# Here is another method to read the file
with open(fname, "r") as f_object:
    print(f_object.read()) 