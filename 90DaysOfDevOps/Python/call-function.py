from re import search
from unittest import result
from linear_search_function import linear_search

from utils import check_even_odd

from add_num import add_two_nums

key = "test"

list_of_env = ["dev","stg","prod","test","qa"]

found = linear_search(list_of_env,key)

print(found)



result = check_even_odd(45)

print(result)



sum = add_two_nums(24,78)

print(sum)