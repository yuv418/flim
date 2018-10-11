from flask import render_template
from app import app


@app.errorhandler(500)
def error_500_handler(error):
	return render_template("500.html")

@app.errorhandler(404)
def error_404_handler(error):
	return render_template("404.html")
