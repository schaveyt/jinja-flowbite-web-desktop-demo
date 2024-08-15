from flask import render_template
from my_app.webapp import app_services, app


@app.route("/")
def index_page():
	return render_template("pages/index_page.html",
			app_services=app_services,
			page_title="Index")

