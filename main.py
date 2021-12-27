from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from controller.user_controller import UserInfo, UserRegister, UserUpdateInfo, UserChangePassword, UserForgotPassword, \
    UserLogin
from controller.product_controller import ProductDetail, ProductGetAll
from flask_jwt_extended import JWTManager
import yaml

username = ""
password = ""
host = ""
dbname = ""
with open("config.yaml", "r") as f:
    try:
        config = yaml.safe_load(f)
        username = config['database']['username']
        password = config['database']['password']
        host = config['database']['host']
        dbname = config['database']['dbname']
    except yaml.YAMLError as exc:
        print(exc)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{username}:{password}@{host}/{dbname}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JWT_SECRET_KEY'] = "secret-key"
jwt = JWTManager(app)
api = Api(app)

if __name__ == '__main__':
    from database.data_source import db

    db.init_app(app)
    with app.app_context():
        db.create_all()
    api.add_resource(UserLogin, "/api/login")
    api.add_resource(UserInfo, "/api/user/getUserInfo")
    api.add_resource(UserRegister, "/api/user/register")
    api.add_resource(UserUpdateInfo, "/api/user/update")
    api.add_resource(UserChangePassword, "/api/user/changePassword")
    api.add_resource(UserForgotPassword, "/api/user/forgotPassword")

    api.add_resource(ProductDetail, "/api/product/<int:product_id>")
    api.add_resource(ProductGetAll, "/api/products")
    app.run(debug=True)
