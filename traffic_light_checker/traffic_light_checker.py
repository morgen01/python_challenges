#!/usr/bin/env python
# coding: utf-8

# In[277]:


############################
# Traffic Light Checker
#
# C. Morgenstern | 16.07.21 
############################


# In[278]:


# prompt user for input sequence
inp = input('Traffic light sequence: ')


# In[279]:


# specify traffic light codes
code = ['R', 'Y', 'G', 'P', 'C', 'X'] 


# In[281]:


# validate input
# check for spaces in sequence, if none ERROR
# check for upper case letters, if none ERROR
if (len(max(inp.split(' '), key=len)) != 1) or (inp.isupper() == False): 
    print("ERROR")  

# check if numerical values are present, if ERROR
elif any(s.isdigit() for s in inp):
    print("ERROR")

    
else:
    # convert string to list and remove whitespace
    seq =[x for x in inp if x.strip()]

    
    # check for length of sequence, if 0 or > 15 ERROR
    if len(seq) == 0 or len(seq) > 15:
        print("ERROR")
        
    # check if sequence starts with "R", if not REJECT    
    elif seq[0] != "R" :
        print("REJECT")
    
    else:
        
        for i in range(len(seq)-1):
        
            # sequence must always contain one of the letters specified in code, otherwise REJECT
            if seq[i] not in code:
                print("REJECT")
                break
        
            # sequence must not contain any repetitions, otherwise REJECT
            elif seq[i] == seq[i+1]:
                print("REJECT")
                break
        
            # flash lights P and C need to be flanked by R lights, otherwise REJECT
            elif (seq[i] == "P") and (seq[i-1] != "R") and (seq[i+1] != "R"):
                print("REJECT") 
                break
            
            elif (seq[i] == "C") and (seq[i-1] != "R") and (seq[i+1] != "R"):
                print("REJECT") 
                break
            
            # red light needs to be followed by green light or flash sequence, otherwise REJECT
            elif (seq[i] == "R") and (seq[i+1] != "G") and (seq[i+1] != "C") and (seq[i+1] != "P"):
                print("REJECT") 
                break
                
            # green light needs to be followed by yellow light, otherwise REJECT
            elif (seq[i] == "G") and (seq[i+1] != "Y"):
                print("REJECT") 
                break
        
            i =+1
            
                    
        # if sequence meets all requirements         
        else:
            print("ACCEPT")
     


# In[ ]:




