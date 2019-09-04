# links that helped me
# https://www.journaldev.com/23674/python-remove-character-from-string
# https://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists/11520540
# https://www.geeksforgeeks.org/print-colors-python-terminal/

from colorama import Fore, Back, Style


checklist = list()

# create


def create(item):
    checklist.append(item)

# read


def read(index):
    print(checklist[int(index)])

# update


def update(index, item):
    checklist[int(index)] = str(item)

# delete


def destroy(index):
    checklist.pop[int(index)]

# testing


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    list_all_items()
    mark_completed(0)
    user_value = user_input("Please Enter a value: ")
    print(user_value)
# list all items


def list_all_items():
    index = 0
    for list_item in checklist:
        #print(str(index) + list_item)
        print(Fore.LIGHTYELLOW_EX + "{} {}".format(index, list_item))
        index += 1

# Stretch challange - mark complete (append check mark)


def mark_completed(index):
    checklist[int(index)] = "√ " + checklist[int(index)]


def unmark_completed(index):
    checklist[int(index)] = (checklist[int(index)])[-0]
    # del checklist[int(index)]
    # deletes entire item -fix later


def select(input_code):
    # Create
    if input_code == "C" or input_code == "c":
        item_index = user_input("Create Item: ")
        create(item_index)

    # Read
    # Crashes if item does not exist
    elif input_code == "R" or input_code == "r":
        item_index = user_input(Fore.LIGHTMAGENTA_EX + "Index Number? ")
        read(item_index)
        # mark as completed
    elif input_code == "A" or input_code == "a":
        item_index = user_input(Fore.BLUE + "Mark as completed[index]: ")
        mark_completed(item_index)
    elif input_code == "U" or input_code == "u":
        item_index = user_input(Fore.BLUE + "unMark as completed[index]: ")
        unmark_completed(item_index)
    # List all items
    elif input_code == "P" or input_code == "p":
        list_all_items()

    elif input_code == "Q" or input_code == "q":
        # Stop
        # D oes not break out of code - fix later
        return False
    else:
        print(Fore.RED + "Unknown Option")
    return True


def user_input(prompt):

    user_input = input(prompt)
    return user_input


# test()
running = True
while running:
    selection = user_input(Fore.GREEN +
                           "Press C to add to list, R to Read from list and P to display list, A to mark as complete, U to unmark: ")
    select(selection)
