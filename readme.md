Djangoで作成するTask管理アプリケーション

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

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

## ruffの実行（format）
```shell
ruff format .
```

## shell_plusの実行
## docker compose を利用して書き換える
```shell
docker compose run web python mysite/manage.py shell_plus
```

### sqlを出力する際
```shell
docker compose run web python mysite/manage.py shell_plus --print-sql
```

## tailwindcssのコンパイル
```shell
docker compose run web python mysite/manage.py tailwind start
```

## dbshellの実行
```shell
docker compose run web python mysite/manage.py dbshell
```

## DBのdump
```shell
docker compose run web python mysite/manage.py dumpdata > db.json
```

## DBのload
```shell
docker compose run web python mysite/manage.py loaddata db.json
```

## コンテナへの入り方

web
```shell
docker compose exec web /bin/bash
```

db
```shell
docker compose exec db /bin/bash
```
