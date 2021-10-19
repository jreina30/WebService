from app import app
from db import db

db.init_app(app)

@app.before_first_request
def create_tables():
    try:
        db.create_all()
    except:
        print("Cannot create tables")
