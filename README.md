# Hackapi

Everything runs in docker. Check the makefile for options.

```
make build
make mongo
make api
```

```
>>> pprint(header)
{'Content-Type': 'application/json'}
>>> pprint(person)
{'firstname': 'bob', 'lastname': 'dole'}
>>> u
'http://0.0.0.0:5000/'
>>> r = requests.post(u + "people", data=json.dumps(person), headers=header)
>>> r.text
u'{"_updated": "Sat, 09 Jun 2018 19:45:47 GMT", "_links": {"self": {"href": "people/5b1c2e6bfc6b160001a1b83b", "title": "person"}}, "_created": "Sat, 09 Jun 2018 19:45:47 GMT", "_status": "OK", "_id": "5b1c2e6bfc6b160001a1b83b", "_etag": "c685a37f179828938e7874b52071e98725673a87"}'

```