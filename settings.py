
MONGO_DBNAME = 'apitest'
MONGO_HOST = 'db'
MONGO_PORT = 27017

ITEM_METHODS = ['GET', 'PATCH', 'DELETE']


people_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'username': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
        'required': True,
        'unique': True,
    },
    'firstname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
    },
    'lastname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
    },
    'password': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 1000,
        'required': True,
    },
    'token': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 1000,
    },
    # 'role' is a list, and can only contain values from 'allowed'.
    'role': {
        'type': 'list',
        'allowed': ["author", "contributor", "copy"],
    },
    # An embedded 'strongly-typed' dictionary.
    'location': {
        'type': 'dict',
        'schema': {
            'address': {'type': 'string'},
            'city': {'type': 'string'},
            'zip': {'type': 'number'},
        },
    },
}


people = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'person',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'lastname'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': people_schema
}


property_schema = {
    'latitube': {
        'type': 'number',
    },
    'longitude': {
        'type': 'number',
    },
    'sqft': {
        'type': 'number',
    },
    'sqftUnfinished': {
        'type': 'number',
    },
    'vacant': {
        'type': 'boolean',
    },
    # An embedded 'strongly-typed' dictionary.
    'location': {
        'type': 'dict',
        'schema': {
            'address': {'type': 'string'},
            'city': {'type': 'string'},
            'zip': {'type': 'string'},
        },
    },
}


property = {
    'item_title': 'property',
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST'],
    'schema': property_schema
}

DOMAIN = {
    'people': people,
    'properties': property,
}