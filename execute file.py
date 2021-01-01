#here are the commands to demonstrate how to access and perform operations on a main file


#run the MODULE of MAIN FILE and import mainfile as a library

import main 
#importing the main file("code" is the name of the file I have used) as a library 


main.create("sankar",25)
#to create a key with key_name,value given and with no time-to-live property


main.create("src",70,20) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


main.read("sankar")
#it returns the value of the respective key in Jasonobject format 'key_name:value'

main.read("src")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR

main.read("example__key")
#if we try to read an unknown key


main.create("sankar",50)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#either use modify operation to change the value of a key
#or use delete operation and recreate it


main.modify("sankar",55)
#it replaces the initial value of the respective key with new value 
main.read('sankar')
 
main.delete("sankar")
#it deletes the respective key and its value from the database(memory is also freed)


#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mistake or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB

