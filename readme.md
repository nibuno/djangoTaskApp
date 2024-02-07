Djangoで作成するTask管理アプリケーション


## venvの作成と有効化
```shell
$ python -m venv venv
$ source venv/bin/activate
```

## requirements.txtのインストール
```shell
$ pip install -r requirements.txt
```

## マイグレーション
```shell
$ cd mysite
$ python manage.py makemigrations
$ python manage.py migrate
```

## 起動方法
```shell
$ python manage.py runserver
```

## 管理者ユーザー作成
```shell
$ python manage.py createsuperuser
```

## blackの実行
```shell
$ black .
```
