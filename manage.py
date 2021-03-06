import json
from flask.cli import FlaskGroup

from api import app, db
from api.models import NationalPark

cli = FlaskGroup(app)

@cli.command('create_db')
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('add_parks')
def add_national_parks():
    national_park_filename = "luontokeskukset.json"
    with open(national_park_filename, "r") as national_park_data:
        data = json.load(national_park_data)
        if data:
            for national_park in data:
                db_entry = NationalPark(name=national_park["name"], longitude=national_park["lon"], latitude=national_park["lat"])
                db_entry.save()
            db.session.commit()
            print("Entries created!")
        else:
            print("Data was not found!")
            print(f"Filename: {national_park_filename}")
            print(f"Data object: {national_park_data}")
if __name__ == "__main__":
    cli()