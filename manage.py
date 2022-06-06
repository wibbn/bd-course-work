from flask.cli import FlaskGroup

from app import app, db
# from app.utils import fill_with_data

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

# @cli.command("fill_db")
# def fill_db():
#     fill_with_data()

if __name__ == '__main__':
    cli()