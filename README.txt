*** INTRO ***
This the readme for the Populator program (Form Letter Generator) to create massive amounts of form letters in a short amount of time.

This program was designed and created by David Lynch for use in the Center for European Studies.

THE ACTUAL PROGRAM IS FOUND IN DIST/MAIN

*** REQUIREMENTS ***
This program requires a CSV file and a TXT/DOCX form letter. Please ensure that the placeholder words in the letter:
1. Match the column titles (headers) of the CSV file EXACTLY
2. Start with an underscore
3. Are one word

*** PLACEHOLDER WORDS ***
See a list of acceptable placeholder words below:
"_Firstname"
"_FIRST_NAME"
"_Event_date"
"_event-date"
"_honAmount"

See a list of UNACCEPTABLE placeholder words below:
"_First name"
"Firstname"
"_event date"
"-event-date"

*** REPLACEMENT LOGIC ***
This program does simple replacement of the placeholder word with whatever is in the row for that corresponding column.

The only exception is handling boolean logic. See guidance for booleans below:
1. Placeholder words for booleans MUST end with "_bool". 
2. Use 1 and 0 for True and False.
3. The rest of the placeholder word must be what you want to input for the value. See example below:
	"_populist_bool" becomes "populist" or "not populist" for values of 1 and 0 respectively.
	"_a_great_country_bool" becomes "a great country" or "not a great country" for values of 1 and 0 respectively.

4. Note that underscores become replaced by spaces for the boolean placeholder word.
5. Please also note that it is case sensitive - whatever case you have will be retained for the replacement word.
