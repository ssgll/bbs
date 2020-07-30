import os
import mysql.connector


class Config:
    DEBUG = True
    SECRET_KEY = "ssgll"

    # 数据库配置
    HOSTNAME = "127.0.0.1"
    PORT = 3306
    DATABASE = "bbs"
    USERNAME = "ssgll"
    PASSWORD = "jxm989851."
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8".format(
        USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE
    )
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # session配置

    # 环境配置
    BASE_DIR = os.getcwd()
    TEMPLATES_FOLDER = os.path.join(BASE_DIR, "templates/")
    STATIC_FOLDER = os.path.join(BASE_DIR, "static/")


class Development(Config):
    pass


class Production(Config):
    DEBUG = False
    SECRET_KEY = "#jQLw#w0HFLAO%SHOv$%MNQ24aviBdwg"
    HOSTNAME = "127.0.0.1"
    PORT = 3306
    DATABASE = "bbs"
    USERNAME = "ssgll"
    PASSWORD = "webadmin"
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8".format(
        USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE
    )


config = {
    "Config": Config,
    "Development": Development,
    "Production": Production,
    "Default": Config,
}
