from flask import Flask

from payments.ext import api, model, site


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = b"_!b\x8c\xfb\xffIR\xe5\x95E\x83\xd2xX\x10"
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "mysql+pymysql://root:pass12344!@127.0.0.1:3306/payments"
    model.init_app(app)
    api.init_app(app)
    site.init_app(app)
    return app
