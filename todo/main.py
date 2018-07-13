from app import app, db
import models
import views

if __name__ == '__main__':
    app.run()
    # No need to do (debug=True), as in config.py, debug = true is already set.
    # app.run(debug=True)
    # app.run(debug=True, use_debugger=False, use_reloader=False)
