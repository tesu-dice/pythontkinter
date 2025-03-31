"""
ubf-8   2021116
リストの中の文字の最大数を取得
"""
list = ["abcde" , "123456789" , "a;df"]
print(list)
print(len(list[0]))

n_list =[]
for i in range(len(list)):
    n_list.append(len(list[i]))

print(n_list)
input()
