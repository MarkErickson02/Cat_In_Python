import sys


class CatInPython:

    def __init__(self):
        self.line_number = 1

    def display(self, file, option):

        end_char = ""
        for line in file:
            if option == "-E":
                line = line.rstrip()
                end_char = "$\n"
            if option == "-n":
                line = "{0} {1}".format(self.line_number, line)
            self.line_number += 1
            print(line, end=end_char)


def main(argv):
    cat = CatInPython()
    file = None
    option = ""

    if len(argv) < 2:
        print("No file given via command line")
        exit(0)
    elif len(argv) == 2:
        file = argv[1]
    elif len(argv) == 3:
        file = argv[1]
        option = argv[2]
    with open(file, "r") as file_open:
        cat.display(file_open, option)


if __name__ == "__main__":
    main(sys.argv)


