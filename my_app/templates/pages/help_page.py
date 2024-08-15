from flask import render_template
from my_app.webapp import app_services, app


@app.route("/help")
def help_page():
	return render_template("pages/help_page.html",
			app_services=app_services,
			page_title="Help")

