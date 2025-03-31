"""
20201207    ubf-8
テキストファイルの読み込み

"""

# 一つ目　表示先は一列目
#「 open('XXXXX.txt') 」でXXXXXファイルを読み込む
text = open('20201207 読み込み用.txt')
#「 XXXXX.readline() 」で一列目を読み込む
print(text.readline())

#--------------------------------------------------------------
#二つ目　表示先は2列目以降
#　ファイルの読み込み
text = open("20201207 読み込み用.txt")
#　繰り返し処理で一行ずつ読み込み
wordlist= []
for date in text:
    print("date="+date)
    word = date.strip("\n")      #改行(\n)で区切って一列ずつ読み込み
    wordlist.append(word)        #wordlistに一列ずつ追加していく
    print("word="+word)              #一回毎に表示
print(wordlist)                #リストにしたのをまとめて表示


input()
