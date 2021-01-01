#KEYVALUE DATASTORE ASSIGNMENT
#SANKAR K - sankark2k@gmail.com



import threading 
from threading import*
import time

json={} #'json' is the dictionary in which we store data

 

#create operation
def create(key,value,timeout=0): #timeout is optional you can continue by passing two arguments without timeout
    if key in json:
        print("error: this key", key, "already exists") #If 2nd time we entered a same key it gives an ERROR
    else:
        if(key.isalpha()):
            if len(json)<(1024*1024*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    json[key]=l
            else:
                print("error: Memory limit exceeded!! ")#Gives error message if memory limit exeed 
        else:
            print("error: Invalind key_name!!",key, "key_name must contain only alphabets and no special characters or numbers")#Gives error message if invalid key_name


#read operation
def read(key):
    if key not in json:
        print("error: given key does not exist in database. Please enter a valid key") #Gives error message if entered a unknown key 
    else:
        b=json[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                string=str(key)+":"+str(b[0]) #To return the value in the format of JasonObject i.e.,"key_name:value"
                print(string)
                return string
        
            else:
                print("error: time-to-live of",key,"has expired") #If entered key is time out then it gives an Error Message
        else:
            string=str(key)+":"+str(b[0])
            print(string)
            return string
            

#for delete operation
def delete(key):
    if key not in json:
        print("error: given key does not exist in database. Please enter a valid key") #Try to access key after deleted it gives an Error
    else:
        b=json[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del json[key]
                print("key- ",key," is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            del json[key]
            print("key - ",key, " is successfully deleted")



#Here I attached an additional operation of modify in order to change the value of key before its expiry time if provided

#for modify operation 
def modify(key,value):
    b=json[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in json:
                print("error: given key does not exist in database. Please enter a valid key") #if unknown key entered gives an error
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                json[key]=l
        else:
            print("error: time-to-live of",key,"has expired") #if expired gives an error
    else:
        if key not in json:
            print("error: given key does not exist in database. Please enter a valid key") #if unknown key entered gives an error
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            json[key]=l

