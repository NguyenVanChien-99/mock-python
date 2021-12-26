from database.data_source import db


class User(db.Model):
    __tablename__ = "tbl_user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))
    age = db.Column(db.Integer)
    fullName = db.Column(db.String(255))

    def __init__(self, _id: int, username, password, email, age: int, full_name):
        self.id = _id
        self.username = username
        self.password = password
        self.email = email
        self.age = age
        self.fullName = full_name

    def __str__(self):
        return "User [id= {}, username={}, password={}, email={}, full name={}, age={}]".format(self.id, self.username,
                                                                                                self.password,
                                                                                                self.email,
                                                                                                self.fullName,
                                                                                                self.age)

    def json(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "fullName": self.fullName,
            "age": self.age
        }
