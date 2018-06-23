from bottle import debug
from bottle import route, run, template, request, HTTPError
debug(True)

READABLE_SEX = ['メス', '不明', 'オス']


@route('/')
def index():
    return template('templates/index.tpl')


@route('/abalone', method='POST')
def resutl():
    try:
        sex = int(request.params['sex'])
        length = int(request.params['length'])
        diameter = int(request.params['diameter'])
        height = int(request.params['height'])
        weight = int(request.params['weight'])
    except (KeyError, ValueError) as e:
        raise HTTPError(status=400, body=e)

    return template('templates/result.tpl',
                    sex=READABLE_SEX[sex],
                    length=length,
                    diameter=diameter,
                    height=height,
                    weight=weight,
                    age=0)


run(host='localhost', port=8080, reloader=True)
