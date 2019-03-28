# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:57:53 2019

@author: rutherfordw, robinsonka
"""

def staff_base():
    '''staff member identifies themself to be assigned the clearance
    (security_level) associated with their ID'''
    ID=raw_input("Who are you?")              #ID prompt
    if ID=="shemp":                           #assigns appropriate clearance
        security_level=0
    elif ID=="curly":
        security_level=1
    elif ID=="larry":
        security_level=2
    elif ID=="moe":
        security_level=3
    else:
        print("Who?")                        #recursion if failed to ID input with a recognized staff member                          
        staff_base()
    return(security_level)                  #return clearance

def request():
    '''record whether they want to read or write'''
    request1=raw_input("Would you like to read or write a file?")   #action prompt
    if request1== "read" or request1== "write":
        return(request1)                                           #return action
    else:
        request()                                                  #recursion upon improper input
    
def request2(request1):   
    '''staff members identifies what level of clearance document they would like to read or write'''
    request2=raw_input("What level of security document?")            #document clearance level prompt
    if request2== "public":
        security_requirement=0                                         #assigns appropriate clearance
    elif request2== "secret":
        security_requirement=1
    elif request2== "top secret":
        security_requirement=2
    elif request2== "her majesty's eyes only":
        security_requirement=3
    else:
        print("security level not recognized")
        request()                                                       #recursion upon improper input

    return(security_requirement)                                        #return document clearance
    
    
def response(security_level, request1, security_requirement):
    '''Compares clearance level of staff with the clearance level of the request, if the staff member has the
    proper clearance then they may do as they have requested'''
    if security_level >= security_requirement:                         #compare clearances
        print("You may " + str(request1) + ".")                        #allow or deny based upon comparison
    else:
        print("Access denied.")     

        
def main():            
    '''calls the functions in their proper order and calls the main itself'''
    x=staff_base()                                 #variable placeholders/function callers
    y=request()
    z=request2(x)
    response(x,y,z)      
main()                                              #calls main


        