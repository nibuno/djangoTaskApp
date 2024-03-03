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

## shell_plusの実行
```shell
$ python manage.py shell_plus
```

### sqlを出力する際
```shell
$ python manage.py shell_plus --print-sql
```

## tailwindcssのコンパイル
```shell
$ python manage.py tailwind start
```