
word1 = "paraparaparadise"

word2 = "paragraph"


def moji_bi_gram(sentence):
  
    bi_split_str = [sentence[x:x+2] for x in range(0, len(sentence), 2)]
    #今回の場合xは０，２，４，６・・となる．
    return(bi_split_str)
    
X = moji_bi_gram(word1)

Y = moji_bi_gram(word2)

print(X)
print(Y)
print(type(X))

XY_union = set(X) | set(Y)

print("X union Y")
print(XY_union)

XY_intersection = set(X) & set(Y)

print("X intersection Y")
print(XY_intersection)


print("X difference Y")

XY_difference = set(X) - set(Y)
print(XY_difference)