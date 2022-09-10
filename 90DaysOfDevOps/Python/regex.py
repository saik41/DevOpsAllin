""""

Rgular Expressions for Extracting email-id's


"""""

from cgitb import text
import re

# print(dir(re))

# print(re.findall.__doc__)

text = """
This service served to text notifiers sai.kiran1213@gmail.com and saikiran.sarab@accionlabs.com and saikiran.sarab@boomiteam.com

"""""
list_of_emails = re.findall("[a-z0-9\.\_\-+]+@+[a-z0-9\.\-+_]+\.[a-z]+",text)


print(list_of_emails)