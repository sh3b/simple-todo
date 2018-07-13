from flask import make_response, jsonify
from werkzeug.exceptions import  abort

from app import db, Todo


def preprocessor_post_limit_entries(**kw):
    if db.session.query(Todo).count() >= 5:
        return abort(make_response(jsonify(error="Maximum entries reached"), 400))