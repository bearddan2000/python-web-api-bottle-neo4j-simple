from bottle import route, run

import logging
from model import DbModel

logging.basicConfig(level=logging.INFO)

neo = DbModel()

@route('/')
def smoke_test():
    cipher = 'UNWIND range(1, 3) AS n RETURN n, n * n as n_sq'
    d = neo.connect().run(cipher).data()
    return {'results': d}

@route('/dog')
def get_all():
    return neo.get_all()

@route('/dog/name/<name>')
def filter_by_name(name: str):
    return neo.filter_by_name(name)

@route('/dog/breed/<breed>')
def filter_by_breed(breed: str):
    return neo.filter_by_breed(breed)

@route('/dog/color/<color>')
def filter_by_color(color: str):
    return neo.filter_by_color(color)

run(host='0.0.0.0', port=8000,debug=True)
