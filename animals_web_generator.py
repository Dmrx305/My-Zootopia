import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)
animals_data = load_data('animals_data.json')


def serialize_animal(animal_obj):
    """ Serializes a list of animals """
    output = ""
    output += '<li class="cards__item">'
    output += '<div class="card__title">'f"{animal_obj['name']}</div>"
    output += '<p class="card__text">'
    output += '<strong>Scientific Name: </strong>'f"{animal_obj["taxonomy"]['scientific_name']}<br/>\n"
    output += '<strong>Diet: </strong>'f"{animal_obj["characteristics"]["diet"]}<br/>\n"
    output += '<strong>Location: </strong>'f"{animal_obj["locations"][0]}<br/>\n"
    if "type" in animal_obj["characteristics"]:
        output += '<strong>Type: </strong>'f"{animal_obj["characteristics"]["type"]}<br/>\n"
        output += '</p>'
    output += "</li>"
    return output

output = ''
for animal_obj in animals_data:
    output += serialize_animal(animal_obj)

with open("animals_template.html", "r") as template:
    html_content = template.read()

new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output)
print(new_html_content)

with open("animals.html", "w") as new_file:
    new_file.write(new_html_content)