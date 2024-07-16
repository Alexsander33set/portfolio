import toml

def parse_toml_file(file_path, key):
    with open(file_path, 'r') as file:
        file_data = toml.load(file)
    data = []
    
    for item_name, item in file_data[key].items():
        data.append(item)
    
    return data