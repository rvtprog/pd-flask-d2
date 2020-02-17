from flask import Flask, request, render_template, json, jsonify

app = Flask(__name__)

@app.route('/')
def getIndex():
  return "Can you redirect me to Home?"

if __name__ == '__main__':
  app.run(threaded=True, port=5017, debug=True) 