from flask import render_template
from my_app.webapp import app_services, app


@app.route("/fetch_example")
def fetch_example_page():

	data = app_services.get_pokedex_data()


	return render_template("pages/fetch_example_page.html",
			app_services=app_services,
			page_title="Fetch Example",
			model=data)

