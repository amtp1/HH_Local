from orm import Model, Integer, String, DateTime
from objects.globals import db, metadata

class AdminAuth(Model):
    __tablename__ = "admin_auth"
    __database__ = db
    __metadata__ = metadata

    id       = Integer(primary_key=True)
    login    = String(max_length=255)
    password = String(max_length=255)