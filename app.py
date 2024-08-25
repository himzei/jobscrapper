from flask import Flask, render_template, request, redirect, send_file
from scrapper import search_incruit, search_jobkorea
from file import save_to_file

app = Flask(__name__)

db = {}
pages = 5

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")

    if keyword == "": 
        return redirect("/")
    if keyword in db: 
        jobs = db[keyword]

    else: 
        jobs_jobkorea = search_jobkorea(keyword, pages)
        jobs_incruit = search_incruit(keyword, pages)
        jobs = jobs_jobkorea + jobs_incruit
        db[keyword] = jobs


    return render_template(
        "search.html", 
        keyword=keyword, 
        jobs=enumerate(jobs), 
        counts=len(jobs)
        )

@app.route("/export") 
def export(): 
    keyword = request.args.get("keyword")

    if keyword == "": 
        return redirect("/") 
    
    if keyword not in db: 
        return redirect(f"/search?keyword={keyword}")
    
    save_to_file(keyword, db[keyword])

    return send_file(f"./{keyword}.csv", as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)