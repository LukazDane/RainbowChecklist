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
    print(checklist[index])

# Update


def update(index, item):
    checklist[int(index)] = str(item)

# Destroy


def destroy(index):
    checklist.pop(int(index))
