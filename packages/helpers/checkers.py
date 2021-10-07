import os

def replacement_words_and_titles_match(rep_words: list, titles: list) -> bool:
    """
    Checks that all the words that need to be replaced in the letter have a value in the csv file.
    """
    for word in rep_words:
        if word not in titles:
            return False
    return True

def check_dir(name: str, home_folder: str) -> bool:
    """
    Checks that a folder has not been already created with the same name.

    Returns False if folder already exists and True if it does not.
    """
    dirs = os.listdir(home_folder)
    if name not in dirs:
        return True
    return False


if __name__ == "__main__":
    print("checkers.py running directly")
else:
    print("importing checkers.py")