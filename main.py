from eve import Eve

def people_callback(request, payload):
    print 'A post to "people" was just performed!'

app = Eve()

app.on_post_POST_people += people_callback

if __name__ == '__main__':
    app.run(host='0.0.0.0')