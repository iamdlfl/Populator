import os

fn = os.path.join(os.path.dirname(__file__), "constants.py")

def get_lines() -> list:
    """
    Reads in the constants file and gets current lines
    """
    with open(fn, 'r') as constants:
        lines = constants.readlines()
    return lines

def get_values(lines: list) -> dict:
    """
    Uses return from get_lines() to find the values of each constant and
    create a dictionary of the constant variable name and the value
    """
    values = {}
    for line in lines:
        value_start = line.index("'")+1
        value_end = line.index("'", value_start)
        key_end = line.index("=")-1
        key = line[0:key_end]
        value = line[value_start:value_end]
        values[key] = value
    return values

def put_values(values: dict):
    """
    Takes in a dictionary of values like the one returned by get_values()
    and modifies the constants.py file to update the values of the constants

    Of special note is that a dictionary of ALL constant values must be provided,
    even if only one of them is different. This function rewrites the file completely 
    and as such any missing constants from the dictionary will be deleted from the file.
    """
    with open(fn,'w') as constants:
        for k, v in values.items():
            constants.write(f"{k} = '{v}'\n")



if __name__ == "__main__":
    print(get_values(get_lines()))
    put_values({
        "HOME_FOLDER": "'Affiliate Faculty'\n",
        "CSV_FILENAME": "'data.csv'\n",
        "TXT_FILENAME": "'letter.txt'\n"
    })
else:
    print("importing change_constants.py")