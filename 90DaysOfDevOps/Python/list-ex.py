list_of_names = list(["aws","gcp","azure"])
list_of_envs = ["prod","dev"]



# print (list_of_envs[0])

# print (list_of_names[2])
# list_of_envs.append("client")
for i in list_of_envs:
    print("Deploying to:")
    print(i)

# print(dir(list_of_envs))

list_of_envs.insert(4,"users")

print (list_of_envs)