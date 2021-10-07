import os
import sys
from tkinter import messagebox

from ..helpers.manipulators import create_letter_text, make_safe_filename, sort_titles # type: ignore
from ..helpers.checkers import check_dir # type: ignore



def create_dir(home_folder: str) -> tuple:
    """
    Uses the check_dir() function to see if a "Letters" folder has already been made. If not, it makes it. If so, it checks that
    the user wants to continue even though any previous letters may be overwritten.

    Returns boolean value to continue or not and then the path name
    """
    name = 'Letters'
    message = "There appears to be a folder of letters already. Do you want to continue? Any pre-existing letters may be overwritten if you continue."
    path = os.path.join(home_folder, name)
    if check_dir(name, home_folder):
        os.mkdir(path)
        return True, path
        
    answer = messagebox.askquestion(title="Continue?", message=message)
    if answer != "yes":
        messagebox.showerror(title="Discontinuing", message="Okay, stopping creation of letters now") 
        return False, path 
    return True, path

def create_letter(dictionary: dict, letter_text: str, titles: list, folder_name: str) -> str:
    """
    Creates the letter .txt file using the new letter text with the filename consisting of
    the value for the first column in the csv file. Uses a helper function to make this 
    filename safe for Windows machines. Returns the pathname.
    """
    sorted_titles = sort_titles(titles)
    new_letter_text = create_letter_text(dictionary, letter_text, sorted_titles)
    column = 1
    safe_name = make_safe_filename(f'{dictionary[titles[0]]} {dictionary[titles[column]]}')
    while not check_dir(f'{safe_name}.txt', folder_name):
        column += 1
        safe_name += f' {make_safe_filename(dictionary[titles[column]])}'
        if column == len(titles)-1:
            break
            

    name = f'{safe_name}.txt'
    path = os.path.join(folder_name, name)
    with open(path, 'w') as file:
        file.write(new_letter_text)
    return path

def create_all_letters(list_of_dicts: list, letter_text: str, titles: list, folder_name: str):
    """
    Creates all of the letters required.

    I have a hard limit of 5,000 letters so that there isn't some accidental infinite or incredibly long list used.

    """
    if len(list_of_dicts) > 5000:
        return messagebox.showerror(title="ERROR", message="There are too many lines in the CSV, this program cannot handle over 5000 lines")
    
    for dictionary in list_of_dicts:
        letter_name = create_letter(dictionary, letter_text, titles, folder_name)
        print(f'Created a letter {letter_name}')

if __name__ == "__main__":
    print("writers.py running directly")
else:
    print("importing writers.py")