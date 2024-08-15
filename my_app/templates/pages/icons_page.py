from flask import render_template
from my_app.webapp import app_services, app


@app.route("/icons")
def icons_page():
	return render_template("pages/icons_page.html",
			app_services=app_services,
			page_title="Icons")

