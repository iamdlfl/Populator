def remove_punctuation(string: str):
    return string.translate({ord(i): None for i in '.,!?()[:;]}{%$#@^&*\'"\\|`~'})

def create_letter_text(replacement_dict: dict, letter_text: str, titles: list) -> str:
    """
    Takes the form letter text and the replacement dictionary and returns the 
    letter text for the dictionary in question

    Returns
    temp_text: The text of the letter with the replaced words
    """
    temp_text = letter_text
    for word in titles:
        if "bool" in word:
            temp_text = temp_text.replace(word, process_bool(word, replacement_dict))
        else: 
            temp_text = temp_text.replace(word, replacement_dict[word])
    return temp_text

def make_safe_filename(filename: str) -> str:
    """
    Returns a filename without any characters disallowed by Windows file system
    """
    bad_chars = '<>:"/|?*\\'
    return filename.translate({ord(i): None for i in bad_chars})

def process_bool(title: str, replacement_dict: dict) -> str:
    """
    A simple tool to process boolean values in the csv file - will return either
    the word with any underscores and "bool" stripped from it or that word with "not" in front of it.

    Will return "****ERROR****" if it doesn't find one of those two values
    """
    new_word = title.replace("_", "").strip("bool").lower()
    value = replacement_dict[title]
    if value == "1":
        return new_word
    elif value == "0":
        return f'not {new_word}'
    else:
        return "****ERROR****"

def sort_titles(titles: list) -> tuple:
    """
    Processes a list of titles and returns a sorted tuple. 

    Since Python will replace "substrings" of our titles this sorts the list so that
    the longer strings are replaced first and shorter strings are replaced last. It does so
    by counting how many times a given string appears in the other strings of the list. 

    Example: In the PopuList example, "_PARTY_NAME" would replace the "_PARTY_NAME_ENGLISH" 
    substring of "_PARTY_NAME." So for Sinn Fein, this would result in "Sinn Fein_ENGLISH."
    Since "_PARTY_NAME" appears in 3 total list items (itself, "_PARTY_NAME_ENGLISH" and 
    "_PARTY_NAME_SHORT"), it will be sorted last.
    """
    new_list = []
    title_tuple = tuple(titles)
    for title in titles:
        counter = 0
        for word in title_tuple:
            if title in word:
                counter += 1
        new_list.append((title, counter))
    sorted_titles = sorted(new_list, key=lambda title: title[1])
    titles_tuple = tuple([title[0] for title in sorted_titles])
    return titles_tuple


if __name__ == "__main__":
    print("manipulators.py running directly")
else:
    print("importing manipulators.py")