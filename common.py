def pair(arg):
    return {arg.split(":")[i]: arg.split(":")[i + 1] for i in range(0, len(arg.split(":")), 2)}