email=input("Enter your email: ")      
#c@g.in -closet condition of gmail, wscube@gmail.com
'''
-minimum 6 characters
-first character is alphabet
-@ usedonly at one time
-position of . is third or fourth from ending 
-no space allowd
-no uppercase allowed
'''
k,j,d=0,0,0
if len(email)>=6:            #ishw
    if email[0].isalpha():    #1ishwari@gmail.com
         if ('@' in email) and (email.count('@')==1):        #ishwari@gmail@.com
             if (email[-4]==".") or (email[-3]=="."):         #ishwari@gmail.c
                for i in email:
                    if i==i.isspace():              #ishwari kape@gmail.com
                        k=1
                    elif i.isalpha():         
                        if i==i.upper():                      #FFFFFF@gmail.com ,Ishwari@gmail.com
                            j=1    
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1       
                if j==1 or k==1:
                    print("wrong email 5")
                else:
                    print("Right email")                    #ishwari@gmail.com
             else:
                 print("wrong email 4")
         else:
             print("wrong email 3")
    else:
        print("wrong email 2")
else:
    print("wrong email 1")
    
  
    

