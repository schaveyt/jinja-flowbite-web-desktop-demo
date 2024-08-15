import os
from flask import Flask
import jinja2

app = Flask(__name__)
app.jinja_env.auto_reload = True

enhanced_loader = jinja2.ChoiceLoader([
    jinja2.PackageLoader("jinja_flowbite", ""),
    app.jinja_loader
])

app.jinja_loader = enhanced_loader
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = '35d092ab79d654448e9041683b53975d8d432cad82ebd009'



import my_app.webapp