from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "<p>Hello Ayoub!!</p>"

if __name__ == "__main__":
  print("i'am insid the main")
  app.run(host='0.0.0.0', debug=True)
