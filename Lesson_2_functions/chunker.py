# Quiz: Chunker If you have an iterable that is too large to fit in memory in full (e.g., when dealing with large
# files), being able to take and use chunks of it at a time can be very valuable.
#
# Implement a generator function, chunker, that takes in an iterable and yields a chunk of a specified size at a time.

# Calling the function like this:

# for chunk in chunker(range(25), 4):
#     print(list(chunk))

# should output:

# 1: [0, 1, 2, 3]
# 2: [4, 5, 6, 7]
# 3: [8, 9, 10, 11]
# 4: [12, 13, 14, 15]
# 5: [16, 17, 18, 19]
# 6: [20, 21, 22, 23]
# 7: [24]

def chunker(iterable, size):
    i = 0
    while i < len(list(iterable)):
        yield iterable[i:i + size]
        i += size


for chunk in chunker(range(25), 4):
    print(list(chunk))