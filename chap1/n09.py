"""
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする
適当な英語の文（例えば
”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）
を与え，その実行結果を確認せよ．
"""

import random

def typo_shuffle(term):
    if len(term) <= 4:
        return term
    else:
        first = term[0]
        last = term[-1]   
        rest = random.sample(list(term[1:-1]), len(term[1:-1]))
        return ''.join([first] + rest + [last])


text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

#print(len(text))
#113

#split sentence in to each element 
#print(text.split())
#['I', 'couldn’t', 'believe', 'that', 'I', 'could', 'actually', 'understand', 'what', 'I', 'was', 'reading', ':', 'the', 'phenomenal', 'power', 'of', 'the', 'human', 'mind', '.']

ans = [typo_shuffle(w) for w in text.split()]
print(ans)
print(''.join(ans))