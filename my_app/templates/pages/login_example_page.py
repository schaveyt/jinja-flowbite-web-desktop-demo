from flask import render_template
from my_app.webapp import app_services, app


@app.route("/login_example")
def login_example_page():
	return render_template("pages/login_example_page.html",
			app_services=app_services,
			page_title="Login Example",
			layout="main")

@app.route("/login_example_stacked")
def login_example_stacked_page():
	return render_template("pages/login_example_page.html",
			app_services=app_services,
			page_title="Login Example Stacked",
			layout="stacked")

