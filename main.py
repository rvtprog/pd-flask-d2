from flask import Flask

app = Flask(__name__)

@app.route('/')
def getIndex():
  return "Can you redirect me to Home?"

if __name__ == '__main__':
  app.run(host="0.0.0.0", threaded=True, port=5050, debug=True) 