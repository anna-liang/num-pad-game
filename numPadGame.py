# Given s, starting location, and n, # of steps to take
# Output all possibilities in sequential order
# s = 1, n = 1 --> [
#                   [1, 2], 
#                   [1, 4], 
#                   [1, 5]
#                   ]
# s = 1, n = 2 --> [
#                   [1, 2, 1], [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 6],
#                   [1, 4, 1], [1, 4, 2], [1, 4, 5], [1, 4, 7], [1, 4, 8],
#                   [1, 5, 1], [1, 5, 2], [1, 5, 3], [1, 5, 4], [1, 5, 6], [1, 5, 7], [1, 5, 8], [1, 5, 9]
#                   ]

directions = {
                1:[2, 4, 5],
                2:[1, 3, 4, 5, 6],
                3:[2, 5, 6],
                4:[1, 2, 5, 7, 8],
                5:[1, 2, 3, 4, 6, 7, 8, 9],
                6:[2, 3, 5, 8, 9],
                7:[4, 5, 8, 0],
                8:[4, 5, 6, 7, 9, 0],
                9:[5, 6, 8, 0],
                0:[7, 8, 9]
            }

def numPadGame(s, n):
    result = []
    if n == 1:
        result = numPadGameRecurse(s, n)
    else:
        # Get all directions for the initial starting number
        subDirections = directions[s]
        for d in subDirections:
            subRecurse = numPadGameRecurse(d, n-1)
            for i in subRecurse:
                result.append([s] + i)
    return result

def numPadGameRecurse(s, n):
    subResult = []
    # Base case of n = 0
    if n == 0:
        return [s]
    # Otherwise, recurse with n-1
    else:
        subDirections = directions[s]
        for d in subDirections:
            subNumPad = numPadGameRecurse(d, n-1)
            for i in range(len(subNumPad)):
                l = [s]
                if len(subNumPad) == 1:
                    l.append(subNumPad[i])
                else:
                    l += subNumPad[i]
                subResult.append(l)
    return subResult


# Parse cmdline input
if __name__ == "__main__":
    import os, sys, getopt
    def usage():
       print ('Usage:	' + os.path.basename(__file__) + ' start steps')
       sys.exit(2)
    # extract parameters
    try:
         opts, args = getopt.getopt(sys.argv[1:],"hc:",["help"])
    except getopt.GetoptError as err:
         print(err)
         usage()
         sys.exit(2)
    start = int(args[0]) if len(args) > 0 else None
    steps = int(args[1]) if len(args) > 1 else None
    for opt in opts:
        if opt in ("-h", "--help"):
           usage()
    if (start is None):
        print('start is missing\n')
        usage()
    elif (steps is None):
        print('steps is missing\n')
        usage()
    print(numPadGame(start, steps))