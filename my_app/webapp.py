import os
from flask import render_template
from my_app import app
from my_app.services.app_services import ApplicationServices


APP_VERSION = "v9.9.9"



# if a win_exe_version_info.py exist, then we want to read the app version from the file.
#
script_dir = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(script_dir, "win_exe_version_info.py")
config_file = os.path.abspath(config_file)
if os.path.isfile(config_file):
    with open(config_file) as f:
        for _, line in enumerate(f):
            if "ProductVersion" in line:
                sanitized_line = line.strip().replace("StringStruct('ProductVersion', '", "")
                sanitized_line = sanitized_line.replace("'),", "")
                APP_VERSION = sanitized_line


app_services: ApplicationServices = ApplicationServices("AppTitle", APP_VERSION)

if app.debug == True:
    print("dbg: detected app in debug mode.")
else:
    print("dbg: not in debug mode")


# import the page handlers
#
import my_app.templates.pages.index_page
import my_app.templates.pages.components_page
import my_app.templates.pages.icons_page
import my_app.templates.pages.docs_page
import my_app.templates.pages.fetch_example_page
import my_app.templates.pages.help_page
import my_app.templates.pages.login_example_page
import my_app.templates.pages.counter_example_page
import my_app.templates.pages.run_executable_page
import my_app.templates.pages.eng_cmd_home





