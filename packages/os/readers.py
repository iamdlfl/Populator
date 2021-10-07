import csv

def get_replacement_words_and_letter_text(txt_filename: str) -> tuple:
    """
    Function to find the words to be replaced (they must begin with an underscore _ )
    and gather the whole letter text.

    """
    with open(txt_filename, 'r') as my_txt:
        letter_text = my_txt.read()

    split_text = letter_text.split()
    list_of_words = []
    for word in split_text:
        if word[0] == '_':
            new_word = word.translate({ord(i): None for i in '.,!?()[]}{%'})
            list_of_words.append(new_word)

    return (list_of_words, letter_text)
    
def get_titles_and_create_dictionaries_for_replacement(csv_filename: str) -> tuple:
    """
    Function to create a list of dictionaries of the CSV rows. Uses the headers of
    the CSV file as the key for the dictionary and the corresponding value for the value.
    Returns two objects, a list of strings and a list of dictionaries.

    """
    # Get CSV data
    with open(csv_filename, 'r') as my_csv:
        csv_list = list(csv.reader(my_csv, delimiter=","))

    titles = csv_list[0]
    list_of_replacement_dictionaries = []

    # Create list of dictionaries with CSV data
    for item in csv_list[1:]:
        temp_dict = {}
        for count, value in enumerate(item):
            temp_dict[titles[count]] = value
        list_of_replacement_dictionaries.append(temp_dict)

    return titles, list_of_replacement_dictionaries

if __name__ == "__main__":
    print("readers.py running directly")
else:
    print("importing readers.py")