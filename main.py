from flask import Flask

app = Flask(__name__)

@app.route('/')
def getIndex():
  return "Can you redirect me to Home?"

if __name__ == '__main__':
  app.run(threaded=True, port=5017, debug=True) 