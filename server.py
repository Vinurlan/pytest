from app.database.db import db
from routes import app

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()