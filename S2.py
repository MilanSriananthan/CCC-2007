def makenum(seq):
    new = []
    for i in seq:
        new.append(int(i))
    return new
numboxs = int(input())
boxes = []
for i in range(numboxs):
    hold = input()
    hold = hold.split(" ")
    hold = makenum(hold)
    boxes.append(hold)

numofpackages = int(input())
packages = []
for i in range(numofpackages):
    hold = input()
    hold = hold.split(" ")
    hold = makenum(hold)
    packages.append(hold)

save = []
for i in boxes:
    save.append(i[0]*i[1]*i[2])

newboxes = []
for i in range(len(save)):
    hold = save.index(min(save))
    newboxes.append(boxes[hold])
    save[hold] = 9999999999999999999999999999999999999999999
print(boxes)
print(newboxes)
print(packages)

for i in range(len(newboxes)):
    newboxes[i] = sorted(newboxes[i])

for i in range(len(packages)):
    packages[i] = sorted(packages[i])

print(packages)
