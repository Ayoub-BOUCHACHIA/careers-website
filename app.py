from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'DATA ANALYSTE',
  'location': 'Paris, France',
  'salary': '3300.00 £'
}, {
  'id': 2,
  'title': 'DATA ENGINEER',
  'location': 'Paris, France',
  'salary': '4500.00 £'
}, {
  'id': 3,
  'title': 'DATA SCIENTIST',
  'location': 'Paris, France',
  'salary': '5500.00 £'
}, {
  'id': 4,
  'title': 'Front-end develpment',
  'location': 'Paris, France',
  'salary': '3200.00 £'
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name="Jovian")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  print("i'am insid the main")
  app.run(host='0.0.0.0', debug=True)
