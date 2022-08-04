import sys

def chomp(string):
    if string[-1] == "\n":
        return string[:-1]
    else:
        return string

def qw(string):
    return string.split()

def die(message):
    sys.stderr(f"{sys.argv[0]}: Error: {message}\n")
    print(sys.argv[0], "Error", message, sep=": ", file=sys.stderr)
    sys.exit(1)
