
lines = []

with open("Loomad.txt", 'r') as fp:
    lines = fp.readlines()

with open("Loomad.txt", 'w') as fp:
    for number, line in enumerate(lines):
        if number not in [1,2,3]:
            fp.write(line)
