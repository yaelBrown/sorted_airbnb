from flask import Flask, request, Blueprint

import json

dataController = Blueprint('dataController', __name__)

@dataController.route('/data', methods=["GET"])
def getData():
  return "getData()", 200

@dataController.route('/test', methods=["GET"])
def testData():
  return "dataController works", 200