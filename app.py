import wikipedia
from flask import *
from flask import request
def r(a):
	return open(a,"r+").read()

app=Flask(__name__,static_folder="ico")

@app.route("/",methods=["POST","GET"])
def mn():
	if(request.method == "GET"):
		return r("a.html")
	else:
		try:
			m = r("result.html").replace("<--Co-->",wikipedia.summary(request.form["search"]))
		except:
			m = r("404.html")
		return m

@app.route("/about")
def mn1():
	return r("about.html")

@app.route("/dev")
def mn2():
	return r("dev.html")

@app.route("/contact",methods=["GET","POST"])
def mn3():
	if (request.method == "GET"):
		return r("form.html").replace("sdfsdfzds","contact")
	else:
		rt = "\n\n\nEmail: "+request.form["email"]+"\n\nMessage: "+request.form["message"]
		open("con/data.txt","a").write(rt)
		return r("form.html").replace("sdfsdfzds","contact") + "<script>alert('Your response has been submitted');</script>"

@app.route("/feedback", methods=["GET","POST"])
def mn4():
	if (request.method == "GET"):
		return r("form.html").replace("message","feedback").replace("sdfsdfzds","feedback")
	else:
		rt = "\n\n\nEmail: "+request.form["email"]+"\n\nMessage: "+request.form["message"]
		open("con/data.txt","a").write(rt)
		return r("form.html").replace("message","feedback").replace("sdfsdfzds","feedback") + "<script>alert('Your response has been submitted');</script>"

@app.route("/report")
def mn5():
	if (request.method == "GET"):
		return r("form.html").replace("message","issue").replace("sdfsdfzds","report")
	else:
		rt = "\n\n\nEmail: "+request.form["email"]+"\n\nMessage: "+request.form["message"]
		open("con/data.txt","a").write(rt)
		return r("form.html").replace("message","issue").replace("sdfsdfzds","report") + "<script>alert('Your response has been submitted');</script>"

if "__main__" == __name__:
	app.run()
