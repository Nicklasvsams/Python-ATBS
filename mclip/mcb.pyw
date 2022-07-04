#! python3
# # mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys, pyinputplus

mcbShelf = shelve.open('mcb')

# TODO: Save clipboard content.
if len(sys.argv) < 2 or len(sys.argv) > 4:
    print('Usage: \nsave [keyword] - Clipboard text to save by keyword \n[keyword] - Clipboard text to load by keyword\nlist - Load all keywords to clipboard\ndelete - Delete all saved keywords\ndelete [keyword] - Delete selected keyword')
    sys.exit

if len(sys.argv) == 3:
    if  sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()

    if sys.argv[1].lower() == 'delete':
        deleteCheck = pyinputplus.inputYesNo(f'Are you sure you want to saved keyword {sys.argv[2]}? (Enter \'yes\' to confirm): ')
        if deleteCheck == 'yes' and mcbShelf.__contains__(sys.argv[2]):
            del mcbShelf[sys.argv[2]]
        else:
            print(f'{sys.argv[2]} does not exist.')

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        if len(mcbShelf) > 0:
            print('List of keywords saved: ')
            for i in mcbShelf:
                print(i)
        else:
            print('There are no keywords saved.')
    elif sys.argv[1].lower() == 'delete':
        deleteCheck = pyinputplus.inputYesNo('Are you sure you want to delete all saved keywords? (Enter \'yes\' to confirm): ')
        if deleteCheck == 'yes':
            mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print('Copied to clipboard: ' + mcbShelf[sys.argv[1]])

mcbShelf.close()