#! python3
# downloadXkcd.py Xkcdコミックをダウンロードする

import requests,os,bs4
from time import sleep


url="http://xkcd.com"
os.makedirs(r"c:\MyPythonScripts\xkcd",exist_ok=True) #データを入れるディレクトリを作成しておく。すでにファイルがあっても無視

while not url.endswith("#"): # ends with urlの最後に"#"がついているのが、"Prevボタンのリンク"
    #---- ページをダウンロードする ----
    print("ページをダウンロード中{}...".format(url))   #進行状況が解るように出力する
    res=requests.get(url)                            #レスポンス（html)を取得
    res.raise_for_status()                           #エラーチェック
    soup=bs4.BeautifulSoup(res.text)                 #レスポンスのテキストをスープする
    
    #---- コミック画像のurlを見つける ----
    comic_elem=soup.select("#comic img") # id="comic" の imgタグ
    if comic_elem==[]:                   #もし comic_elemが なにもなかったら（終了処理）
        print("コミック画像が見つかりませんでした")
        
    else:                                #もし comic_elemが あったら（通常処理）
        comic_url="http:"+comic_elem[0].get("src")#コミックのあるurlをセット ソースsrcをゲット　"//imgs.xkcd.com/comics/voting_software.png" 
        
        #---- 画像ダウンロードする ----
        print("コミック画像をダウンロード中です{}...".format(comic_url))
        res=requests.get(comic_url) # コミックのあるurl先のhtmlレスポンスを取得　
        res.raise_for_status()      # レス取得後は都度　エラーチェック
        
        #---- 画像を保存する ----
        image_file=open(os.path.join(r"c:\MyPythonScripts\xkcd",os.path.basename(comic_url)),"wb")
        for chunk in res.iter_content(10000):   #100kB毎保存する
            image_file.write(chunk)            
        image_file.close()#閉じる
        
    #---- prev ボタンのurlを取得する
    prev_link=soup.select("a[rel='prev']")[0]   #prevボタンを押したときのurl
    url="http://xkcd.com"+prev_link.get("href") #prevボタンを押した先のページのurlを定義 href="/2031/" 
    #sleep(5)
    
print("完了")

