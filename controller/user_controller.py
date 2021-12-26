from flask_jwt_extended import create_access_token, current_user, jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp

from entity.user import User
from repository.user_repository import UserRepository


class UserInfo(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = UserRepository.find_by_id(user_id)
        if user is None:
            return {"msg": "User not found"}, 404
        return user.json(), 200


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="Username is required!")
    parser.add_argument("password", type=str, required=True, help="Password is required!")
    parser.add_argument("email", type=str, required=True, help="Email is required!")
    parser.add_argument("fullName", type=str, required=False)
    parser.add_argument("age", type=int, required=False)

    def post(self):
        data = UserRegister.parser.parse_args()
        print("create new user")
        # check username
        user = User(1, data.username, data.password, data.email, data.age, data.fullName)
        saved = UserRepository.save(user)
        return saved.json(), 200


class UserChangePassword(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("currentPassword", type=str, required=True, help="Current password required")
    parser.add_argument("newPassword", type=str, required=True, help="New password required")

    @jwt_required()
    def post(self):
        data = UserChangePassword.parser.parse_args()
        # get current user
        user_id = get_jwt_identity()
        user = UserRepository.find_by_id(user_id)
        if user is None:
            return {"message": "User not found with id {user.id}"}, 404
        # compare password
        if safe_str_cmp(data.currentPassword, user.password) == False:
            return {"message": "Incorrect password"}, 401
        # set new password
        user.password = data.newPassword
        saved = UserRepository.update(user)
        return saved.json(), 200


class UserUpdateInfo(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("email", type=str, required=True, help="Email is required!")
    parser.add_argument("fullName", type=str, required=True, help="Fullname is required!")
    parser.add_argument("age", type=int, required=True, help="Age is required!")

    def post(self):
        data = UserUpdateInfo.parser.parse_args()
        print("update user info")
        # get current user
        user = UserRepository.find_by_id(1)
        if user is None:
            return {"message": "User not found with id {user.id}"}, 404
        user.email = data.email
        user.fullName = data.fullName
        user.age = data.age
        saved = UserRepository.update(user)
        return saved.json(), 200


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="Username is required!")
    parser.add_argument("password", type=str, required=True, help="Password is required!")

    def post(self):
        login = UserLogin.parser.parse_args()
        user = UserRepository.find_by_username(login.username)
        if user is None:
            return {"message": "Invalid username"}, 401
        if safe_str_cmp(login.password, user.password) == False:
            return {"message": "Invalid password"}, 401
        access_token = create_access_token(identity=user.id)
        return {
            "token": access_token,
            "userId": user.id
        }


class UserForgotPassword(Resource):

    def get(self):
        # get current user
        # send email -> new pwd
        return {"message": "New password was send to your email"}
