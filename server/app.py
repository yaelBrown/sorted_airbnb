from flask import Flask
from flask_cors import CORS

from controllers.dataController import dataController

app = Flask(__name__)
CORS(app)

app.register_blueprint(dataController, url_prefix='/api/')

if __name__ == "__main__":
  app.run(port=5000, debug=True)