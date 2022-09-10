file_object = open('my_file.txt','r') #open

print(file_object.readlines()) #process


file_object.close() #close


try:
    file_object_new = open('my_new_file.txt','r') #open

except FileNotFoundError:
    print("error handled")
    file_object_new = open('my_new_file.txt','w+') #open
    file_object_new.read() #process
finally:
    file_object_new.close() #close