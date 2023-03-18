from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id":"1",
     "title":"Associate Analyst",
    "location":"Delhi",
    "salary":"10K/per month",
  },
  {
    "id":"2",
     "title":"Data Analyst",
    "location":"Delhi",
    "salary":"12lakh CTC",
  },
  {
    "id":"3",
     "title":"Senior Analyst",
    "location":"Delhi",
    "salary":"2.2 lakh ctc",
  },
  {
    "id":"4",
     "title":"sales manager",
    "location":"Delhi",
  
  },
]

@app.route("/")
def hello_world():
  return render_template('Home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobss():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)
