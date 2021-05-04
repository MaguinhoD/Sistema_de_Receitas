import sys 

from src.Main import app, init_database


if __name__ == "__main__":

    if 'init_db' in sys.argv:
        init_database(app)

    app.run(debug=False)