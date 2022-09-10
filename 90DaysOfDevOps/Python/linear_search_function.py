# list_of_env = ["dev","stg","prod","test","qa"]

# key = "test"

def linear_search(list_of_env,key):
    
    is_found = False

    for env in list_of_env : 
        
        if env == key:
            is_found = True


    # if is_found:
    #     print("Found")

    # else:
    #     print("Not Found")
    
    return is_found
        # print("found")

# found = linear_search(list_of_env,key)

# print(found)
# It is used to calling a file directly or indirectly 
if __name__ == "__main__":
    print("hi i am from linear search planet...")