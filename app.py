from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Lagos, Nigeria',
  'salary': '$50,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Maryland, USA',
  'salary': '$170,000'
}, {
  'id': 3,
  'title': 'Database Engineer',
  'location': 'Lisbon, Porugal',
  'salary': '$110,000'
}, {
  'id': 1,
  'title': 'Devops Engineer',
  'location': 'London, U.K',
  'salary': '$150,000'
}, {
  'id': 1,
  'title': 'Frontend Engineer',
  'location': 'Remote',
}]


@app.route("/")
def hello_jovian():
  return render_template('home.html', jobs=JOBS, company_name='Dovian')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
