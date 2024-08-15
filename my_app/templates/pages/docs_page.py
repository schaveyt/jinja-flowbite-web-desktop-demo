from flask import render_template
from my_app.webapp import app_services, app


@app.route("/docs")
def docs_page():
	return render_template("pages/docs_page.html",
			app_services=app_services,
			page_title="Documents")

