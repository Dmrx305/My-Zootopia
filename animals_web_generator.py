import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')
output = ""

for animal in animals_data:
    output += '<li class="cards__item">'
    output += '<div class="card__title">'f"{animal['name']}</div>"
    output += '<p class="card__text">'
    output += '<strong>Diet: </strong>'f"{animal["characteristics"]["diet"]}<br/>\n"
    output += '<strong>Location: </strong>'f"{animal["locations"][0]}<br/>\n"
    if "type" in animal["characteristics"]:
        output += '<strong>Type: </strong>'f"{animal["characteristics"]["type"]}<br/>\n"
        output += '</p>'
    output += "</li>"

with open("animals_template.html", "r") as template:
    html_content = template.read()

new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output)
print(new_html_content)

with open("animals.html", "w") as new_file:
    new_file.write(new_html_content)