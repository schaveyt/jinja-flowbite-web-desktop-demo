from flask import render_template
from my_app.webapp import app_services, app


@app.route("/components")
def components_page():
	
    table_data = [
        ["1", "Bulbasaur",	"Seed Pokémon",	"Bulbasaur can be seen napping in bright sunlight. There is a seed on its back. By soaking up the sun’s rays, the seed grows progressively larger."],
        ["2", "Ivysaur",	"Seed Pokémon",	"There is a bud on this Pokémon’s back. To support its weight, Ivysaur’s legs and trunk grow thick and strong. If it starts spending more time lying in the sunlight, it’s a sign that the bud will bloom into a large flower soon."],
        ["3", "Venusaur",	"Seed Pokémon",	"There is a large flower on Venusaur’s back. The flower is said to take on vivid colors if it gets plenty of nutrition and sunlight. The flower’s aroma soothes the emotions of people."],
        ["4", "Charmander",	"Lizard Pokémon",	"The flame that burns at the tip of its tail is an indication of its emotions. The flame wavers when Charmander is enjoying itself. If the Pokémon becomes enraged, the flame burns fiercely."],
    ]

    return render_template("pages/components_page.html",
			app_services=app_services,
			page_title="Components",
            table_data=table_data)

