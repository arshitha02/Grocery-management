from app import app
from app.models.database import close_db_connection


if __name__ == "__main__":
    app.run(debug=True)

    #close db 
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        close_db_connection()