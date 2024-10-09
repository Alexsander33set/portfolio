import pymongo
import re

class User:
  def __init__(self, email:str, password:str):
    self.email = email
    self.password = password

  def validate(self):
    if not self.email or not self.password:
      raise ValueError("Email and password are required")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
      raise ValueError("Invalid email address")
    if not re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", self.password):
      raise ValueError("Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number and one special character")