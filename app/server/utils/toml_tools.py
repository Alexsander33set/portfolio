import toml

def parse_toml_file(file_path):
    with open(file_path, 'r') as file:
        file_data = toml.load(file)
    
    data = []
    
    for item in file_data['projects'].items():
        data.append(item)
    
    return data