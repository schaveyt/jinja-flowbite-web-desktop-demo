from flask import render_template
from my_app.webapp import app_services, app
import time
import datetime

@app.route("/run_executable")
def run_executable_page():
	return render_template("pages/run_executable_page.html",
			app_services=app_services,
			page_title="Run Executable")



@app.route("/run_executable__run_exe")
def run_executable__run_exe():

	time.sleep(1)
	timestamp = 'Timestamp: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())
	python_version_result = app_services.run_external_cmd(["python", "--version"])
	pwd_result = app_services.run_external_cmd(["pwd"])

	response = f"""{timestamp}
Ran the command:
   python --version

{python_version_result.stdout}
------------------------------------------------
Ran the command:
	pwd

{pwd_result.stdout}
"""

	return response

