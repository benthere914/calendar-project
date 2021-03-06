import os
import psycopg2
from flask import (Blueprint, render_template)
from app.forms import AppointmentForm
bp = Blueprint('main', __name__, url_prefix='/')
CONNECTION_PARAMETERS = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASS"),
    "dbname": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
}
@bp.route('/')
def main():
    form = AppointmentForm()
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            curs.execute('''
            SELECT id, name, start_datetime, end_datetime
            FROM appointments
            ORDER BY start_datetime;
            ''')
            rows = curs.fetchall()
            output = []
            for row in rows:
                tempobj = {}
                tempobj['id'] = row[0]
                tempobj['name'] = row[1]
                tempobj['start'] = row[2]
                tempobj['end'] = row[3]
                output.append(tempobj)
    rows = output
    return render_template('main.html', rows=rows, form=form)
