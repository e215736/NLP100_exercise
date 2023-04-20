word1="パトカー"
word2="タクシー"

new_word= []

for i in range (len(word1)):
    tmp1=word1[i]
    tmp2=word2[i]
    
    new_word.append(tmp1)
    new_word.append(tmp2)
    
print(new_word)
print("".join(new_word))
