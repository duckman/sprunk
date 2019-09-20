from flask import Flask

class Web:
    def __init__(self, radio = None):
        self.radio = radio
    
    def web_thread(self):
        app = Flask(__name__)
        app.add_url_rule('/', 'index', self.hello_world)
        app.run(host='0.0.0.0')

    def hello_world(self):
        return self.radio.current.str()