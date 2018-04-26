# characters read specified
with open("camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())

# line by line
camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)