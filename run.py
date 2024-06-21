from flask_app import app, db

if __name__ == "__main__":

    # Create all database tables
    with app.app_context():
        db.create_all()

    app.run(debug=True)
