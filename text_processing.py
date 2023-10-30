"""
    CS051P Lab Assignments: Text Processing

    Name: YOUR-NAME-HERE
          YOUR-PARTNER-NAME-HERE, if pair programming

    Date:   WHEN YOU COMPLETED IT

    The goal of this assignment is to familiarize you with processing strings,
    sequences and files, through exercises on looping over contents in string,
    reading and writing files, etc.
"""
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters


def every_fourth_char(string):
    #   1. write a complete docstring for this method
    #   2. write code to return every fourth char in string
    return string[:len(string):4]


def copy_parts_of_file(old_filename, new_filename):
    #   1. write a complete docstring for this method
    #   2. write code to
    #      read the specified old file
    #      for each line, create a new line w/every 4th char
    #      write the to the specified new file
    writing = open(new_filename, "w")
    reading = open(old_filename, "r")
    for line in reading:
        writing.write(every_fourth_char(line))
    reading.close()
    writing.close()
    return new_filename


def num_characters(string):
    #   1. write a complete docstring for this method
    #   2. write code to
    #      count and return the number of non-whitespace chars
    count = 0
    for char in string:
        if char in whitespace:
            count = count
        else:
            count = count + 1
    return count


def count_characters(filename):
    #   1. write a complete docstring for this method
    #   2. write code to
    #      open and read the specified file
    #      count the number of non-whitespace chars
    #      return the total number of non-whitespace chars
    reading = open(filename, "r")
    out_int = 0

    for line in reading:
        out_int = out_int + num_characters(line)
    reading.close()
    return out_int


def count_char(string, char):
    count = 0
    for letter in string:
        if letter in ascii_lowercase:
            if letter == char.lower():
                count = count + 1
        if letter in ascii_uppercase:
            if letter == char.upper():
                count = count + 1
    return count


def num_words(string):
    count = 0
    start = 0
    is_counting = True

    for char in string:
        if char not in whitespace:
            if is_counting:
                count = count + 1
                is_counting = False
        else:
            is_counting = True
    return count


def main():
    """
    """

    char = input("single letter to count:\n\t")

    while char in ascii_uppercase:
        print("you must enter a single letter!")
        char = input("single letter to count:\n\t")

    file_or_int = int(input("Please type 1 for a file mode and 0 for an interactive mode:\n\t"))

    if file_or_int == 1:
        input_file = input("filename?:\n\t")
        reading = open(input_file, "r")
        num_line = 0
        file_words = 0
        file_characters = 0
        spec_characters = 0

        for line in reading:
            num_line += 1
            file_words += num_words(line)
            file_characters += num_characters(line)
            spec_characters += count_char(line, char)
        reading.close

        print("******** statistics ********")
        print(str(num_line) + " lines")
        print(str(file_words) + " words")
        print(str(file_characters) + " non-whitespace characters")
        print(str(spec_characters) + " " + char + "'s")
        print("average word length is: " + str(file_characters / file_words))
        print("percentage " + str(char) + "'s: " + str(spec_characters / file_characters * 100))

    # interactive mode
    if file_or_int == 0:
        total_line = ""
        input_line = ""
        line_counter = 0
        total_words = 0

# if the input isn't "-1" adds inputs to a total line, keeps a counter for the # of inputs, tracks words per each line
        while input_line != "-1":
            input_line = input("input line or -1 to stop:\n")
            if input_line == "-1":
                total_line = total_line
            else:
                total_line += input_line + "\n"
                line_counter += 1
                total_words += num_words(input_line)

        # prints all statistics
        print("******** statistics ********")
        print(str(line_counter) + " lines")
        print(str(total_words) + " words")
        print(str(num_characters(total_line)) + " non-whitespace characters")
        print(str(count_char(total_line, char)) + " " + char + "'s")
        print("average word length is: " + str(num_characters(total_line) / num_words(total_line)))
        print("percentage " + str(char) + "'s: " + str((count_char(total_line, char) / num_characters(total_line)) * 100))


if __name__ == '__main__':
    main()
