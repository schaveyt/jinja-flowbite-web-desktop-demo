from flask import render_template
# from my_app import app
from my_app.webapp import app_services, app


@app.route("/counter_example")
def counter_example_page():
	return render_template("pages/counter_example_page.html",
			app_services=app_services,
			page_title="Counter Example")


@app.route("/counter_incr", methods=["POST"])
def counter_incr_partial():
	app_services.app_state.counter += 1
	return f"{app_services.app_state.counter}"

@app.route("/counter_reset", methods=["POST"])
def counter_reset_partial():
	app_services.app_state.counter = 0
	return f"{app_services.app_state.counter}"