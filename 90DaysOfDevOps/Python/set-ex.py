set_1 = {1,1,1,1,1,1,1,1,1,34,134,13,35,67}
set_2 = {1,1,1,1,1,1,1,45,78,23,66,34}


print(set_1.intersection(set_2))

print(set_1.union(set_2))


list_of_envs = ["dev","qa","prod","test","qa","test"]

list_of_envs = list(set(list_of_envs))

print(list_of_envs)