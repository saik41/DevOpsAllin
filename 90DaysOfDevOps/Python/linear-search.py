list_of_env = ["dev","stg","prod","test","qa"]

key = "test"

for env in list_of_env : 
    if env == key:
        is_found = True

if is_found:
    print("Found")

else:
    print("Not Found")

        # print("foun