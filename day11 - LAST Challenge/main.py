"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
from flask import Flask, render_template, request, redirect, send_file
from scrapper.remoteok import get_jobs as get_jobs_remoteok
from scrapper.weworkremotely import get_jobs as get_jobs_weworkremotely
from exporter import save_to_file

app = Flask("Remote Jobs")

db = {}

@app.route("/")
def home():
  return render_template("main.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else:
      jobs = get_jobs_remoteok(word) + get_jobs_weworkremotely(word)
      db[word] = jobs
  else:
    return redirect("/")
  return render_template(
    "report.html", 
    searchingBy=word,
    resultsNumber=len(jobs),
    jobs=jobs
  )


@app.route("/export")
def export():
  try:
    word = request.args.get('word')
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    save_to_file(jobs)
    return send_file("jobs.csv")
  except:
    return redirect("/")
  

app.run(host="0.0.0.0")
