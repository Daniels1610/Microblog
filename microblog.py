from app import app
import os

os.environ['FLASK_ENV'] = "development"
app.run()