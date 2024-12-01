import yaml
import json

with open("./data/tada_ui.json") as f:
    data = json.load(f)

with open("./out.yaml", 'w') as f:
    yaml.dump(data, f)