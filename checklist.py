checklist = list()

# create


def create(item):
    checklist.append(item)

# read


def read(index):
    return checklist[index]

# update


def update(index, item):
    checklist[index] = item

# delete


def destroy(index):
    checklist.pop(index)

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
# list all items


def list_all_items():
    index = 0
    for list_item in checklist:
        #print(str(index) + list_item)
        print("{} {}".format(index, list_item))
        index += 1

# stretch challange: Mark as completed Hint: add character to checklist


def mark_completed(index):
    checklist[int(index)] = "√" + checklist[index]


def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Catch all
    else:
        print("Unknown Option")


def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input


test()
