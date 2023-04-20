sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

words = sentence.split()

"""
#test
a=words[0]
print(type(a))
b=a[0:1]
print(b)
"""

goal_dict={}

for i in range (len(words)):
    if i==0 or i==4 or i==5 or i==6 or i==7 or i==8 or i==14 or i==15 or i==18:
        tmp1=words[i]
        #print(tmp1[0:1])
        goal_dict[i+1] = tmp1[0:1]
    else:
        tmp2=words[i]
        #print(tmp2[0:2])
        tmp2[0:2]
        goal_dict[i+1] = tmp2[0:2]
        
print(goal_dict)