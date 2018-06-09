from eve import Eve
from eve.auth import BasicAuth
from flask import current_app as app
from flask import Blueprint

from pprint import pprint


blueprint = Blueprint('prefix_uri', __name__)

@blueprint.route('/login', methods=['GET'])
def del_user():
    print "testing this login route"
    return "stuff"


def pre_people_post_callback(request):
    pprint(request)
    print('A GET request on the contacts endpoint has just been received!')


def people_callback(request, payload):
    print 'A post to "people" was just performed!'


app = Eve()
app.on_post_POST_people += people_callback
app.on_pre_POST_people += pre_people_post_callback
app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(host='0.0.0.0')