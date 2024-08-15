from flask import render_template
from my_app.webapp import app_services, app


@app.route("/components")
def components_page():
	return render_template("pages/components_page.html",
			app_services=app_services,
			page_title="Components")

