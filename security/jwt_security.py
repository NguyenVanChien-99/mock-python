from entity.user import User
from repository.user_repository import UserRepository
from flask_jwt_extended import JWTManager

jwt = JWTManager()

@jwt.user_identity_loader
def user_identity(id):
    return id


# @jwt.user_lookup_loader
# def user_lookup_callback(_jwt_header, jwt_data):
#     identity = jwt_data["sub"]
#     user = UserRepository.find_by_id(identity)
#     if user is not None:
#         return user.json()
#     return None
