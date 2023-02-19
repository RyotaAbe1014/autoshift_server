# -*- coding: utf-8 -*-
# DBへの接続設定
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
import os
# .envファイルの読み込み
load_dotenv()

# 接続したいDBの基本情報を設定
user_name = os.environ["USERNAME"]
password = os.environ["PASSWORD"]
host = os.environ["HOST"]
database_name = os.environ["DATABASE_NAME"]

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    user_name,
    password,
    host,
    database_name,
)

# DBとの接続
ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

# Sessionの作成
session = scoped_session(
    # ORM実行時の設定。自動コミットするか、自動反映するか
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

# modelで使用する
Base = declarative_base()
# DB接続用のセッションクラス、インスタンスが作成されると接続する
Base.query = session.query_property()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
