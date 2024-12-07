import os

command = "uptime"
command = "cpu"
command = "date"

def check_cpu(command):
print(os.system(command))


check_cpu("systeminfo")

def check_date(command): #define function
    print(os.system(command))

check_date("date") #calling