# with open('my_input_file.txt') as file_object:
#     contents = file_object.read(10)
#     contents2 = file_object.read(10)
#     print(file_object.tell())
#
# print(contents)
# print(contents2)


with open('my_input_file.txt', 'r+') as file_object:
    for line in file_object:
        print(line)
    file_object.write("This is the last line I just added\n")


# with open('my_input_file.txt') as file_object:
#     lines = file_object.readlines()
#
# for l in lines:
#     print(l.rstrip())
#
# print(lines)
#
# print(len(lines))



# Here are the contents of the file.\n
# This is the 2nd line.\n

