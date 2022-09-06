

dict_of_items1 = {
    "env":"dev",
    "server":"aws-linux",
    "ram":8096,
    "cpu":4,
    "active":True
}


dict_of_items2 = {
    "env":"prod",
    "server":"ubuntu",
    "ram":1024,
    "cpu":8,
    "active":False
}



env_details = [dict_of_items1,dict_of_items2]

# print(dict_of_items.get("ram"))

# if dict_of_items ["active"] :
#     print("server details")
#     print("Environment: ",dict_of_items["env"])


for env in env_details:
    for key,value in env.items():
        if key == "active" and value==True:
            print(env.values())
        # print("\n")