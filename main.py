import json
import uuid
from eve.auth import TokenAuth
from eve import Eve
from eve_swagger import swagger, add_documentation

from flask import current_app as app
from flask import Blueprint, request, Response
from werkzeug.security import check_password_hash, generate_password_hash

from pprint import pprint


blueprint = Blueprint('prefix_uri', __name__)

@blueprint.route('/login', methods=['GET'])
def del_user():
    auth = request.authorization

    people = app.data.driver.db['people']
    person = people.find_one({'username': auth.username})
    if not person or not check_password_hash(person["password"], auth.password):
        return Response(
            'Could not verify your access level for that URL.\n'
            'You have to login with proper credentials', 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        )

    token = {"token": str(uuid.uuid4())}

    resp = app.data.driver.db['people'].update(
        {"username": auth.username},
        {"$set": token}, 
        upsert=False,
    )

    return json.dumps(token)


class TokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        #this is a backdoor and should be removed before using any of this in production
        if token == "d33236e2-83a7-4f12-b2ea-e9f7e74e342c":
            return True
        accounts = app.data.driver.db['people']
        return accounts.find_one({'token': token})


def pre_people_post_callback(request):
    '''
    hash the password before it can be stored
    '''
    data_dict = json.loads(request.data)
    data_dict["password"] = generate_password_hash(data_dict["password"])
    request.data = json.dumps(data_dict)
    print('A GET request on the contacts endpoint has just been received!')


def on_insert_people(items):
    for item in items:
        item["password"] = generate_password_hash(item["password"])


def people_callback(request, payload):
    print 'A post to "people" was just performed!'


# app = Eve(auth=TokenAuth)
app = Eve()

app.on_post_POST_people += people_callback
app.on_pre_POST_people += pre_people_post_callback
app.on_insert_people += on_insert_people

app.register_blueprint(blueprint)
app.register_blueprint(swagger)


if __name__ == '__main__':
    app.run(host='0.0.0.0')