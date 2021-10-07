import os
from tkinter import messagebox


from .helpers.checkers import replacement_words_and_titles_match # type: ignore
from .os.readers import get_replacement_words_and_letter_text, get_titles_and_create_dictionaries_for_replacement # type: ignore
from .os.writers import create_dir, create_all_letters # type: ignore
from .doc_files.docs import process_all_docs, get_doc_words # type: ignore

def do_app(home, csv, txt):
    """
    Takes values from the main level app to create all the letters. This allows for the values of folder
    or file names to be updated during the GUI in a way that simply importing those values does not allow.

    Returns a boolean to continue and the number of files created (via number of dictionary entries)
    """
    if csv[-3:] != 'csv':
        message = "You appear to have selected a file that is not a CSV file. Please ensure that the CSV filename point to a CSV file."
        return False, messagebox.showerror(title="ERROR", message=message)
    if txt[-3:] == 'txt':
        CSV_FILE = os.path.join(home, csv)
        TXT_FILE = os.path.join(home, txt)

        titles, replacement_dicts = get_titles_and_create_dictionaries_for_replacement(CSV_FILE)
        replacement_words, letter_text = get_replacement_words_and_letter_text(TXT_FILE)

        if not replacement_words_and_titles_match(replacement_words, titles):
            return False, messagebox.showerror(title="ERROR", message="Error, please check that words to be replaced in letter and titles in CSV are the same")


        cont, folder_name = create_dir(home)

        if cont:
            create_all_letters(replacement_dicts, letter_text, titles, folder_name)

            return True, len(replacement_dicts)
        
        else:
            return False, None

    elif "doc" in txt[-5:]:
        CSV_FILE = os.path.join(home, csv)
        DOC_FILE = os.path.join(home, txt)

        titles, replacement_dicts = get_titles_and_create_dictionaries_for_replacement(CSV_FILE)
        replacement_words = get_doc_words(DOC_FILE)

        if not replacement_words_and_titles_match(replacement_words, titles):
            return False, messagebox.showerror(title="ERROR", message="Error, please check that words to be replaced in letter and titles in CSV are the same")

        cont, folder_name = create_dir(home)

        if cont:
            process_all_docs(replacement_dicts, DOC_FILE, titles, folder_name)

            return True, len(replacement_dicts)

        return False, None

    else:
        message = "Error, it appears, you have chosen a letter file that is not a TXT or DOCX. Please ensure that the filetype"
        message += " of the letter file is a txt or docx"
        return False, messagebox.showerror(title="ERROR", message=message)


if __name__ == "__main__":
    pass
else:
    print('importing app.py')