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

# list all items


def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1


test()
