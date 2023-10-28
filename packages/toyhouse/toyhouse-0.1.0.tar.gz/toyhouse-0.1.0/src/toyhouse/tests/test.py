from Session import Session
from Character import Character
from User import User
import os
session = Session("ceruloryx", "Winterwatcher566")
session.auth()
user = User(session, "mangosonmars")
print(user.user_pic(download=True))