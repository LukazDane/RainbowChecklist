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
        print("{} {}".format(index, list_item))
        index += 1

# stretch challange: Mark as completed Hint: add character to checklist


def mark_completed(index):
    checklist[int(index)] = "√ " + checklist[index]


# test()
running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list: ")
    select(selection)
