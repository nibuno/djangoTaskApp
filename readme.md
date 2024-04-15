Djangoで作成するTask管理アプリケーション

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## dockerコンテナの起動
```shell
docker compose up
```

## requirements.txtのインストール
```shell
docker compose run web pip install -r requirements/requirements.txt
docker compose run web pip install -r requirements/requirements-dev.txt
```

## マイグレーション
```shell
docker compose run web python mysite/manage.py migrate
```

## 管理者ユーザー作成
```shell
docker compose run web python mysite/manage.py createsuperuser
```

## ruffの実行（format）
```shell
docker compose run web ruff format .
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
