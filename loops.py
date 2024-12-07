# list is a data sturactore which can hold multiple values multiple type
# arrry is a data structer which can hold multiple values of same type
list_of_cloud = ["aws","azure","gcp","digital ocean","utho"] 
cloud = "gcp" #variable

print(list_of_cloud)

#add a new cloud salesfore

list_of_cloud.append("salesforce")

#add a new cloud IBM

list_of_cloud.append("IBM") #adds to the end of list

print(list_of_cloud)

list_of_cloud.insert(2,"heroku")   #insert is a comand to use  to past in  location in any list 

print(list_of_cloud)

print(len(list_of_cloud))  #to find length of list of itne use len comand

#insert "hello cloud" to oth index of list

list_of_cloud.insert(0,"hello cloud")
print(list_of_cloud)

#iteration of a list
for cloud in list_of_cloud:
    print(cloud)

    for i in range(1,11):
        print(i)