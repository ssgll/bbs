# encoding:utf-8
from flask import Flask
from config import config
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.exts import db
from app.urls import indexBlueprint


def createApp():
    app = Flask(
        __name__, 
        template_folder=config["Default"].TEMPLATES_FOLDER,
        static_folder=config["Default"].STATIC_FOLDER,
    )
    app.config.from_object(config["Default"])
    app.register_blueprint(indexBlueprint)

    return app

# 实例化app
app = createApp()

# 绑定app
migrate = Migrate(app)
migrate.init_app(app=app, db=db)

# 添加迁移脚本命令行
manager = Manager(app)
manager.add_command('db', MigrateCommand)