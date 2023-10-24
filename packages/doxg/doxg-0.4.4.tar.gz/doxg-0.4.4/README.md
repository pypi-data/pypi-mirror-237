# distribution for the first time

### describe: my first python package uploaded on https://pypi.org/ and uploaded on github for distribution
### PYPI에 package를 업로드하고 깃허브와 연동하여 배포


---

View at:
https://pypi.org/project/doxg

INSTALL

    $ pip install doxg
  
DEV

    $ git clone ...
    $ cd doxg
    $ pdm venv create
    $ source .venv/bin/activate
    (hello-doxg-3.8) $ pdm install
    
DEPLOY

    $ pdm publish
    
Contributing

    $ git branch 0.2.0/doxg
    
    $ git switch 0.2.0/doxg
    Switched to branch '0.2.0/doxg'
    
    $ vi pyproject.toml
    
    $ git status
    On branch 0.2.0/doxg
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git restore <file>..." to discard changes in working directory)
            modified:   pyproject.toml
    
    no changes added to commit (use "git add" and/or "git commit -a")
    
    $ git add .
    
    $ git status
    On branch 0.2.0/doxg
    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
            modified:   pyproject.toml
    
    $ git commit -m "start dev 0.2.0"
    [0.2.0/doxg 4ed0751] start dev 0.2.0
     1 file changed, 1 insertion(+), 1 deletion(-)
     
    $ git push
    fatal: The current branch 0.2.0/doxg has no upstream branch.
    To push the current branch and set the remote as upstream, use
    
        git push --set-upstream origin 0.2.0/doxg
    
    $ git push --set-upstream origin 0.2.0/doxg


function examples
---

doxg-imp

    # basic
    import numpy as np
    import pandas as pd
    import math

    # visualize
    import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly.express as px
    from plotly.subplots import make_subplots
    import plotly.figure_factory as ff
    import plotly.graph_objs as go

    # crawling
    import requests
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options


    import pickle
    
doxg-pic

                               :!????7~                         :^~^.

                             .YY!:..:^?5!   .:^~~!!7777!!~^:. !555Y555~

                             P?        .Y5?J??7!~~^^~JYYYY5555PJ77777J#~

                            .#:          ^:          !?77777??7?????77#!

                             JP:                     :7???????????77JGJ

                              ~YJ7.          .::::    .~7?????YYYYJ7PG

                                !#.       .~!~^^^^       :^!77???????#~

                                YJ        ~^                 .:^~~~!!PY

                                B~            ^77~.          ^YPGP?. ?P

                               :#:          .P#YP@&?        ~@B^?@@G !P?^

                               :#.          !@#7Y@@#        ^#@#&@@P   ~P?

                               .#:     ..... ?B@@&P^   ....  .755J~ :!!~!B!

                                G!    :!7777!. ::.   .YYYYYJ        :~~~:YY

                                J5     .:^^^:.        5YYY5Y             G!

                                :#:                   ~PYYP^            YY

                                 J5                    ~55~           ^5?

                                  B~                    .:::^~~!!!!~~5G~

                                 !G.      ::.     :^!?JJJJJ#J!!!!!!!7???JJ?7~:

                                :B^       !??????GPJ7~^^:::PJ   ..     ...:~7JY?^

                                P?            ..^~7JJJ7!7~:!B:..............  .PY

                               7G                    :!J7G!:PJ ...............^B:

                              .B^                 ..::^^~G7:~#^.............. 5J

                              J5        .!!77???YPJJJ??77~:::JG............. ~B.

                             .B^        .~^^:.. :#~::::^YYY?::PY ............G7

                             ?P                  Y5::::!B^!&~:^G? ......... ?P

                             G!                  .B!::::^:~7:::^G? ....... ~B:

                            ~B                    7B^::?7:::::::^GJ...... ~B~

                            ?P                     Y5:^#?^:::::::^55.... !B~

                            7G         :?JJ!        PJ:~J~:::::::::JP^ :JP:

                             PJ        ?7.^#:       .GJ^^^^^^^~~~~~!Y#Y57

                              ?57:        .#:  ......^5JJJJJJ????Y#7~^~.

                               .!JJ?!~^:. ?#??????????7??????????J^

                                  .:~!77??5^                  ..


doxg-who

    I am simon

test

    ==================================== 3 passed in 0.02s ====================================
    (doxg-3.8)  doxg@LAPTOP-M2348M93  ~/code/doxg   0.3.0/docker ±  pytest --cov
    =================================== test session starts ===================================
    platform linux -- Python 3.8.18, pytest-7.4.2, pluggy-1.3.0
    rootdir: /home/doxg/code/doxg
    plugins: cov-4.1.0
    collected 3 items

    tests/test_app.py ...                                                               [100%]

    ---------- coverage: platform linux, python 3.8.18-final-0 -----------
    Name                   Stmts   Miss  Cover
    ------------------------------------------
    src/doxg/__init__.py       0      0   100%
    src/doxg/app.py            8      0   100%
    tests/__init__.py          0      0   100%
    tests/test_app.py         10      0   100%
    ------------------------------------------
    TOTAL                     18      0   100%


    ==================================== 3 passed in 0.04s ====================================



from doxg.game import coin_game

coin_game(num) # num은 게임 인원 수

    ==========================================================================================
    A가 마셔야할 술 5잔, 싫다면 코인을 던지세요
    코인이 모두 뒷면(■,■)일 경우 당첨!! 코인을 던지시겠습니까?(Y/N) :Y
    1......
    2............
    3..................
    코인 결과: ('■', '■') !!!!
    ==========================================================================================
    🌺팡팡💥파라바라~팡팡팡 🎊ヲヲヲヲヲヲヲヲヲヲヲ🌺팡팡💥파라바라~팡팡팡 🎊ヲヲヲヲヲヲヲヲヲヲヲ🌺팡팡💥파 라바라~팡팡팡 🎊ヲヲヲヲヲヲヲヲヲヲヲ🌺팡팡💥파라바라~팡팡팡 🎊ヲヲヲヲヲヲヲヲヲヲヲ🌺팡팡💥파라바라~팡팡팡 🎊ヲヲヲヲヲヲヲヲヲヲヲ
    >>>>>>>>>>>>>  A 당첨!! 5잔을 마셔야합니다!


from doxg.game import coin_game

    coin_game( number of players : int):

![image](https://github.com/doxgxxn/doxg/assets/135602281/c709e41a-6fb1-4d55-8603-1f83a33e403c)

