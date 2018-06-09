IMAGE ?= hackapi

build:
	docker build -t hackapi .

mongo:
	docker run --name some-mongo -d mongo

api:
	docker run --link some-mongo:db -p 5000:5000 -it hackapi

