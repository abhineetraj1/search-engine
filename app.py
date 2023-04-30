import wikipedia as w
import os
from flask import *
from flask import request, render_template

app=Flask(__name__,static_folder="ico", template_folder=os.getcwd())

@app.route("/",methods=["POST","GET"])
def mn():
	if(request.method == "GET"):
		return render_template("index.html", info="")
	else:
		try:
			return render_template("index.html",info=w.summary(request.form["search"]))
		except:
			return render_template("index.html", info="Information not found")

if "__main__" == __name__:
	app.run()
