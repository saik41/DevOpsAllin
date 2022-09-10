import builtins

from cmath import e


list_of_env = ["dev","stg","prod","test","qa"]

try:
    print(list_of_env[5])
    raise Exception("This is an exception")
except:
    print("exception handled")
finally:
    print("it will execute anyways")

print("this code is running")





try:
    print(list_of_env[5])
    a = 10
    b = 0
    c = a/b
except ZeroDivisionError as e:
    print("1",e)

except IndexError as e:
    print ("2",e)



    print(dir(builtins))