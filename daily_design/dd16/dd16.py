#!usr/bin/python3
#Ella Adam
#12/10/19

contents = ""

save_path = "./design_file.txt" 
write_file = open(save_path, "w")

contents += "\nThis is some text"

write_file.write(contents)
write_file.close()


read_file = open(save_path, "r")

contents = read_file.read()
print(contents)
read_file.close()
