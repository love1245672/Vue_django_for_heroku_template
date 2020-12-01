#   **host環境建立(一)**
1.安裝 [Python 3.6.3rc1](https://www.python.org/downloads/release/python-363rc1/)

2.安裝 [node.js 12.16.1](https://nodejs.org/download/release/v12.16.1/)

3.安裝 Vue.js 2.5.17  ```npm install vue```

#   **host環境建置(二)**
1.將 bitbucket 內所有文件複製到D槽，在 `D:\`下執行以下指令:
    `git clone bitbucket_URL`
    
2.首先進入 `D:\vue_django_for_heroku_template` 終端中利用package.json建立環境，在`D:\vue_django_for_heroku_template`下執行指令:
    ```npm install```
    
3.建立好環境後，為了建立index.html檔案，在 `D:\vue_django_for_heroku_template` 下執行指令:
	```npm run build```
	
4.確認網頁跑的狀態，看是否有成功建置，在`D:\vue_django_for_heroku_template`下執行指令:
	```python manage.py runserver```
	
# **架站流程(heroku)**
1.參考以下教學，[Heroku 部署網站](https://djangogirlstaipei.herokuapp.com/tutorials/deploy-to-heroku/?os=windows)，其中設定檔的部分皆以建置完畢
  * 請先根據教學安裝好heroku工具

2.先登入 heroku 網站 創建 app <`license_app`>

3.在`D:\`下執行以下指令(請自行登入自身帳號)
	```heroku login```
	
4.使用cmd登入heroku後，回到heroku網站點選Settings，找到Heroku git URL，在`D:\`下執行:
	```git clone Heroku_git_URL```
(Heroku_git_URL 為https://git.heroku.com/xxxxxxxxx.git)

5.將建置好的 vue_django_for_heroku_template 內所有檔案複製到剛剛clone下來的 license_app 中

6.其中複製進來的檔案資料夾內，需確認 .gitignore 是否與下方一致:
    
    .DS_Store
    node_modules/
    db.sqlite3
    /venv
    __pycache__/
    
    # local env files
    .env.local
    .env.*.local
    
    # Log files
    npm-debug.log*
    yarn-debug.log*
    yarn-error.log*
    
    # Editor directories and files
    .idea
    .vscode
    *.suo
    *.ntvs*
    *.njsproj
    *.sln
    *.sw*

	
7.為了將剛剛複製的檔案上傳到heroku，請在 `D:\license_app` 下執行
	```git init```
	```git add ```
	```git commit -m "XXX"```
	```heroku config:set DJANGO_SETTINGS_MODULE=backend.settings.prod```
	```git push```
	
8.heroku 會自動建置heroku資料庫，請在 `D:\license_app` 下執行
	```heroku run python manage.py migrate```

9.打開上傳的heroku網站，請在 `D:\license_app` 下執行
    ```heroku open```

# **Notice**
**Table,DB相關問題**
目前所建置的model以及DB可依照使用者需求制訂
