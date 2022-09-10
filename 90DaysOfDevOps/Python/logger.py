import logging

print(dir(logging))
logging.basicConfig(format= "%(asctime)s %(message)s",filename='my_server_logs.log', datefmt='%d/%m/%y %I:%M:%S %p', level=logging.DEBUG)
logging = logging.getLogger()
print(dir(logging))


logging.warn("this may break")

logging.info("this is fine")

logging.error("this is an error,fix it")

logging.critical("This is a critical error, fix it")