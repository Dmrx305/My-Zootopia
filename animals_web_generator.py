import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')
output = ""
for animal in animals_data:
    output += f"Name: {animal['name']}\n"
    output += f"Diet: {animal["characteristics"]["diet"]}\n"
    output += f"Location: {animal['locations'][0]}\n"
    if "type" in animal["characteristics"]:
        output += f"Type: {animal["characteristics"]["type"]}\n"
#print(output)

with open("animals_template.html", "r") as template:
  html_content = template.read()
#print(html_content)

new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output)
print(new_html_content)

with open("animals.html", "w") as new_file:
  new_file.write(new_html_content)