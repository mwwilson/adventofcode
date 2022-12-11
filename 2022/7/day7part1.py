f = open("day7input.txt", "r")
filestring = f.readlines()

class file:
    def __init__(self, size, name):
        self.size = size
        self.name = name

class dir:
    def __init__(self, name, parent):
        self.name = name
        self.files = []
        self.subdirs = {}
        self.parent = parent

    def size(self):
        size = 0
        for f in self.files:
            size = size + f.size
        for key in self.subdirs:
            size = size + self.subdirs[key].size()
        self.size = size
        return size
    
    def sumSmallSizes(self):
        size = 0
        for key in self.subdirs:
            size = size + self.subdirs[key].sumSmallSizes()
        if self.size <= 100000:
            size = size + self.size
        return size
        

root = dir('/', None)
current_dir = root
for line in filestring:
    parts = line.split()
    
    # special case for cd to root
    if line == "$ cd /\n":
        current_dir = root
        continue
    # special case for cd to parent
    if line == "$ cd ..\n":
        current_dir = current_dir.parent
        continue
    if parts[0] == '$' and parts[1] == 'cd':
        current_dir = current_dir.subdirs[parts[2]]
        continue
    if parts[0] == '$' and parts[1] == 'ls':
        continue

    # parsing 'ls' command
    if parts[0] == 'dir':
        current_dir.subdirs[parts[1]] = dir(parts[1], current_dir)
        continue

    current_dir.files.append(file(int(parts[0]), parts[1]))

root.size()
print(root.sumSmallSizes())