from text_processing import *


def main():

    # test num_characters
    print("*** testing num_characters ***")
    assert type(num_characters("")) == int
    assert num_characters("Happy haPpy      day!      !") == 15
    assert num_characters("   hello  Wednesday") == 14
    assert num_characters("Manchester United ") == 16
    assert num_characters("coding") == 6
    assert num_characters("p \n u \n r \n p \n l \n e") == 6
    print("num_characters passed")

    # test count_char
    print("*** testing count_char ***")
    assert type(count_char("", "")) == int
    assert count_char("Happy happy haPPY", "y") == 3  # check given testers
    assert count_char("HAPPY HAPPY HAPPY", "y") == 3  # check given testers
    assert count_char("HAPPY HAPPY HAPPY", "Y") == 3  # check given testers
    assert count_char("", "z") == 0  # check empty string
    assert count_char("Wayne Rooney", "B") == 0  # check letter not in string
    assert count_char("AaAa AaAaAa 203958235", "A") == 10  # check letters of the same + numbers
    print("count_char passed")

    # test num_words
    print("*** testing num_words ***")
    assert type(num_words("")) == int
    assert num_words("Happy haPpy     day!   !") == 4  # check given testers
    assert num_words("   Happy haPpy     day!   ") == 3  # check given testers
    assert num_words(" My name \n is Jay \n and \n Dylan  ") == 6  # check whitespace of new lines
    assert num_words("") == 0  # check empty string
    assert num_words("LeBronIsTheGOAT") == 1  # check one word with no whitespace
    assert num_words("Coders!   coding? code@ withcode  !") == 5  # check random
    print("num_words passed")


if __name__ == "__main__":
    main()
