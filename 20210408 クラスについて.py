"""
ubf-8      20210408

※クラスについて？
クラスを設定してからオブジェクト作成で楽に管理できる。
どんどんリストに入れることで同じ名前でも別のものとして保存できる。

使用法？
キーボードで１を打つとクラスから一人作られてリストに追加される。
２を押すとリストの中の人のナンバー、年齢、職業（ただの数字）を羅列する。

これでシューティングの弾とか敵キャラとかの管理ができる！？。。。。。かもしれない
"""
import random as ransu  #「randint()」をつかえるように
#↑「as」は「random」を「ransu」として変換の意味

#まずクラス（+オブジェクト持つ要素ののパターン）の定義をする
class hito : #「hito」というクラスを作成
    name = None #「None」＝何もない。という意味（この時点では）
    nenrei = None
    shokugyou = None
    def shoukai(self):    #「shoukai」という関数（一連の処理）を決める
    #「self」の部分はインスタンスの名前？が入る
        print("{0} \n 年齢：{1}才 \n 職業：{2}"
              .format ( self.name, self.nenrei , self.shokugyou ))
list = []
sample = hito()
sample.name = "sample"
sample.nenrei = "sample"
sample.shokugyou= "sample"
#クラスをもとにインスタンスというものを作る（オブジェクトとの違いは知らない）
#これ（↑）が楽にできるようになるのがメリット

def tuika(): #ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    print("現在" + str(len(list)+1) +"人" )
    someone = hito()   # ↓ 「random.randint」=「ransu.arndint」
    someone.name = "No." + str(  ransu.randint(1000,9999)  )
    someone.nenrei = ransu.randint(10,100)
    someone.shokugyou = ransu.randint(0,9)
    list.append(someone)
    print("\n"+"\n"+"\n")
    taiki()

def raretu(): #----------------------------------
    for i in range( len(list) +0) :
        print("ーーーーーーーーーーー"+ str(i+1) + "人目")
        list[i].shoukai()
    print("ーーーーーーーーーーー以上。\n"+ "\n"+"\n"+"\n")
    taiki()

def taiki(): #------------------------------------------------------
    print("～1で追加2で羅列～")
    a = input()
    if a== "1" :
        print("追加しました。")
        tuika()
    if a== "2" :
        print("羅列します。")
        raretu()
    else:
        taiki()
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
taiki()
