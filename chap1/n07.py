"""
07. テンプレートによる文生成Permalink
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．
"""


def repeat(x, y, z):
    print(f'{x}時の{y}は{z}')


repeat(12,"気温",22.4)

"""
(dm) nishino@nishinonoMacBook-Air chap1 % python n07.py
12時の気温は22.4
"""
