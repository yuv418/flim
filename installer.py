import sys
import os

sys.path.append(os.getcwd() + "/app")
from app import db


print("Flim database installer v1.0")
print("Installing database. This might take a while..")

db.create_all()

print("Installing finished. No error reported.")

