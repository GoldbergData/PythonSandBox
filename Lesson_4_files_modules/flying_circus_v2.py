def create_cast_list(filename):
    cast_list = []
    cast_list_actors = []
    # use with to open the file filename
    # use the for loop syntax to process each line
    # and add the actor name to cast_list
    with open(filename) as f:
        for line in f:
            cast_list.append(line.strip())
    for cast in cast_list:
        cast_list_actors.append(cast.split(",")[0])
    return cast_list_actors


cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
