from flaskcode.cli import create_flask_app
import os
app = create_flask_app(username='admin', password='admin')

app.config['FLASKCODE_RESOURCE_BASEPATH'] = os.environ.get('CODE_DIR',os.getcwd())

if __name__ == '__main__':
    app.run()