FILEPATH = 'todos.txt'

def get_file(filename=FILEPATH):
    """Reads a text file from argument and return the information as a list."""
    with open(filename, 'r') as info:
        data = info.readlines()
    return data

def write_file(data, filename=FILEPATH):
    """Write the given data in a file, data should be a list."""
    with open(filename, 'w') as info:
        info.writelines(data)

def show_file(filename=FILEPATH):
    """Print out the data in a text file with numbering."""
    info = get_file(filename)

    for i, data in enumerate(info):
        print(f"{i + 1}) {data.strip()}")
