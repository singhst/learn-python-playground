# webscrape-toy-figure-website


```shell
# create and activate virtual environment
$ virtualenv venv
$ . venv/bin/activate

# install dependency
$ pip install -r requirement.txt

# Start to scrape all-product table
$ python main.py
```


Expected output from terminal:

```shell
# see current path
$ pwd
xxxx/learn-python-playground/webscrape-toy-figure-website

# run
$ python app/main.py 
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=0
>>> Created folder: ./product_list//html/shop=05-001/dt=20220704/
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=1
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=2
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=3
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=4
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=5
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=6
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=7
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=8
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=9
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=10
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=11
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=12
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=13
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=14
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=15
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=16
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=17
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=18
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=19
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=20
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=21
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=22
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=23
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=24
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=25
>>> _whole_url: https://p-bandai.com/hk/search?text=&sort=relevance&shop=05-001&page=26
>>> Created folder: ./product_list//csv/shop=05-001/dt=20220704/
(817, 4)
   page                                               name           shop_product_code                                            img_url  
0     0                               METAL BUILD I.W.S.P.     /hk/item/N2623282001001  https://p-bandai.com/img/hk/p/t/N2623282001001...  
1     0  S.H.Figuarts KAMEN RIDER SABELA KONCHUU DAIHYAKKA     /hk/item/N2611071001001  https://p-bandai.com/img/hk/p/t/N2611071001001...
2     0          S.H.Figuarts KAMEN RIDER GENM MUSOU GAMER     /hk/item/N2631818001001  https://p-bandai.com/img/hk/p/t/N2631818001001... 
...                                                      
14    25           Super Robot ????????? ????????? (Free Shipping)     /hk/item/N2171116001002  https://p-bandai.com/img/hk/p/t/N2171116001002...  
15    25                    FiguartsZERO ???????????? [7??? ??????]     /hk/item/N2171128001001  https://p-bandai.com/img/hk/p/t/N2171128001001...  
16    25    FiguartsZERO ???????????? [7??? ??????] (Free Shipping)     /hk/item/N2171128001002  https://p-bandai.com/img/hk/p/t/N2171128001002...
  
```


list all files:

```shell
# see current path
$ pwd
xxxx/learn-python-playground/webscrape-toy-figure-website

$ ls -l
-rw-r--r--  1 user  staff    3963  4 Jul 22:51 README.md
drwxr-xr-x  6 user  staff     192  4 Jul 23:00 app
drwxr-xr-x  4 user  staff     128  4 Jul 23:05 product_list
-rw-r--r--  1 user  staff     418  4 Jul 00:51 requirements.txt
drwxr-xr-x  7 user  staff     224  4 Jul 01:26 venv
```