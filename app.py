from flask import Flask, render_template, jsonify

#creating flask app
app = Flask(__name__)

JOBS= [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs.10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs.15,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs.12,00,000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
  }
]
#registered an route (html route)
@app.route("/")
def hello_mansi():
  return render_template('home.html',jobs=JOBS)

#api route
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS) 

#checking if we are running as python script
if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)