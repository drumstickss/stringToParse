delimeters = [" " , "{" , "}" , "[" , "]" , "(" , ")"]
keywords = ["if" , "else" ,"do" , "while" , "break" , "continue" , "switch" , "case" , "short" , "int" , "long" ,"double" , "float" , "char" , "return" , "void" ,"NULL" ,"struct"] 
operators = ["+" , "-" , "*" , "/" , "<" , ">" ,"="]
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
 
f = open("stringtoparse.txt")
k=f.read()
list = k.split(" ")

i = 0
while i < len(list):
    if list[i] in operators:
        print( list[i] +  " is a operator")
    if list[i] in keywords:
        print(list[i] + " is a keyword")
    if list[i] in delimeters:
        print(list[i] + " is a delimeter")
    if list[i] not in keywords and list[i] not in delimeters :
        if list[i][0] in alphabet:
            print(list[i] + " is Valid Identifier")     
    if list[i].isnumeric() == True:
        print(list[i] + " is a integer ") 
    elif list[i].replace('.', '', 1).isdigit()== True:
        print(list[i] + " is  a real number")
    if list[i] not in keywords and list[i] not in delimeters and list[i] not in alphabet and list[i] not in operators and list[i].isnumeric() == False and list[i].replace('.', '', 1).isdigit()== False and list[i][0] not in alphabet:
        print(list[i] + " is not valid identifier ")    
    i += 1


        
    

