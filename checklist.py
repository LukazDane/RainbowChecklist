checklist = list()
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)


# Create

def create(item):
    checklist.append(item)

# Read


def read(index):
    return checklist[index]

# UPDATE


def update(index, item):
    checklist[index] = item

# DESTROY


def destroy(index):
    checklist.pop(index)
