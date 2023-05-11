
# def cipher(sent):
#     checked_list =[]

#     for i in range(len(sent)):
#         #文字が小文字の場合の処理
    
#         if sent[i].islower():
#             checked_list += chr(219 - ord(sent[i]))
        
        
#         #文字が小文字の場合の処理
#         if sent[i].isupper():
#             checked_list += sent[i]
            
#     return checked_list

#result
#['W', 'v', 'i', 'v', 'S', 'g', 'f', 'x', 'p', 'O', 'm', 'T', 's', 'v', 'E', 'w', 't', 'v']



def cipher(sent):
    checked_list =[]
    checked_list_string=""

    for i in range(len(sent)):
        #文字が小文字の場合の処理
        if sent[i].islower():
            checked_list.insert(i, chr(219 - ord(sent[i])))
        
        
        #文字が小文字の場合の処理
        if sent[i].isupper():
            checked_list.insert(i, (sent[i]))
#result
#['W', 'v', 'i', 'v', 'S', 'g', 'f', 'x', 'p', 'O', 'm', 'T', 's', 'v', 'E', 'w', 't', 'v']
    for ii in range(len(checked_list)):
        checked_list_string +=checked_list[ii]
    
    return checked_list_string

test_sentence = "Were Stuck On The Edge. "
print(cipher(test_sentence))


# (dm) nishino@nishinonoMacBook-Air chap1 % python n08.py
# WvivSgfxpOmTsvEwtv