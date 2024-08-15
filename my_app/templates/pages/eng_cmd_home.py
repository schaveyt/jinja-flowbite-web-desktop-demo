from flask import render_template
import requests
from my_app.webapp import app_services, app


@app.route("/eng_cmd_home")
def eng_cmd_home_page():	
	return render_template("pages/eng_cmd_home.html",
			app_services=app_services,
			page_title="Eng Cmd Home")


@app.route("/get_eng_cmd_info_async")
def get_eng_cmd_info_async():
	
	
	# 1. Go hit the eng_cmd_ws endpoint.
	#    which return as json string
	#
	# { 
	# 	"msg": "EngCmd Service is Running!",
	# 	 "payload": null,
	# 	 "status_code": 0
	# }
	#
	# 2. Parse the response json for the `msg`
	# 3. if msg contains "is Running" then its alive
	#

	eng_cmd_svc_resp = requests.get("http://localhost:5000/")

	status_json = eng_cmd_svc_resp.json()
	
	eng_cmd_svc_val = True if "is Running" in status_json["msg"] else False	
	
	return render_template("pages/eng_cmd_home_info_partial.html",
			app_services=app_services,
			eng_cmd_svc_status_is_active=eng_cmd_svc_val)
