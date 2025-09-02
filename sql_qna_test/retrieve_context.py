import json
import re

def parse_schema_item(item):
    if item.startswith("Table"):
        match = re.match(r"Table (\w+): (.+)", item)
        if match:
            return {
                "type": "table",
                "name": match.group(1),
                "description": match.group(2)
            }
    elif item.startswith("Column"):
        match = re.match(r"Column (\w+): (.+)", item)
        if match:
            return {
                "type": "column",
                "name": match.group(1),
                "description": match.group(2)
            }
    return None

def json_to_arr(filename):
    with open(filename, 'r') as file:
        schema = json.load(file)

    structured_schema = [parse_schema_item(item) for item in schema if parse_schema_item(item) is not None]
    return structured_schema