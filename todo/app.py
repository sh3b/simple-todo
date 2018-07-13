import flask_restless
from flask import Flask
from flask_migrate import MigrateCommand
from flask_script import Manager
from config import Configuration

import flask_sqlalchemy

# Flask app
app = Flask(__name__)

# Config
app.config.from_object(Configuration)

# DB
db = flask_sqlalchemy.SQLAlchemy(app)

# Manager
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# RestLess Flask
from models import Todo
from api_helpers import preprocessor_post_limit_entries

manager_api = flask_restless.APIManager(app, flask_sqlalchemy_db=db)
manager_api.create_api(Todo,
                       url_prefix='/api/v1',
                       collection_name='todo',
                       methods=['GET', 'POST', 'PATCH', 'DELETE'],
                       preprocessors=dict(POST=[preprocessor_post_limit_entries]))


# Most minimum
# from flask import Flask
# import flask_restless
# import flask_sqlalchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/flask_restless.db'
# db = flask_sqlalchemy.SQLAlchemy(app)
#
#
# # class Todo(db.Model):
# #     __tablename__ = "todo"
# #
# #     id = db.Column(db.Integer, primary_key=True)
# #     description = db.Column(db.String(255))
#
#
# db.create_all()
#
# # Create the Flask-Restless API manager.
# manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)
# manager.create_api(Todo, methods=['GET', 'POST', 'PATCH', 'DELETE'])
#
#
# if __name__ == "__main__":
#     # Start the server with 'python \<name_of_this_file.py\>'
#     app.run()