"""n-gramPermalink
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，
”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
"""

import re

sentence = "I am an NLPer"



#print(type(no_space))
#<class 'str'>

#print(no_space)
#IamanNLPer


def moji_bi_gram(sentence):
    #複数の空白を除去する（substitude）
    #\sは、空白文字（スペース、タブ、改行、復帰など）にマッチする特殊文字
    #+は、直前のパターンが1回以上繰り返されることを表す
    no_space = re.sub('\s', "", sentence)
    bi_split_str = [no_space[x:x+2] for x in range(0, len(no_space), 2)]
    #今回の場合xは０，２，４，６・・となる．
    
    #bi_split_str = [no_space[x:x+N] for x in range(0, len(no_space), N)]
    #Nを一致して変えることで文字数を調整可能
    print(bi_split_str)

def tango_bi_gram(sentence):
    words = sentence.split()
    tmp_list=[]
    tmp_str=""
    count=0
    for i in range (len(words)):
        count+=1
        tmp_str+=words[i]
        if count == 2:
            tmp_list.append(tmp_str)
            tmp_str=""
            count=0
    print(tmp_list)



moji_bi_gram(sentence)

tango_bi_gram(sentence)