from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def getIndex():
  return "Can you redirect me to Home?"

@app.route('/test')
def testr():
    return render_template('calc.html')

@app.route('/calc', methods = ['POST'])
def calc():
    return request.get_json()

if __name__ == '__main__':
  app.run(host="0.0.0.0", threaded=True, port=5050, debug=True) 