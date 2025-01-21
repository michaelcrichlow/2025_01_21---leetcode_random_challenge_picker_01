import random


def leetcode_random_challenge_picker(easy: int, medium: int, hard: int) -> None:
    # NOTE: will raise ValueError if easy, medium or hard are larger than the length
    # of the corresponding list or negative

    easy_list = [1, 9, 13, 14, 20, 21, 26, 27, 28, 35, 58, 66, 67, 69, 70, 83, 88, 94,
                 100, 101, 104, 108, 110, 111, 112, 118, 119, 121, 125, 136, 141, 144,
                 145, 160, 168, 169, 171, 175, 181, 182, 183, 190, 191, 193, 195, 196,
                 197]

    medium_list = [2, 3, 5, 6, 7, 8, 11, 12, 15, 16, 17, 18, 19, 22, 24, 29, 31, 33, 34,
                   36, 38, 39, 40, 45, 46, 47, 48, 49, 50, 53, 54, 55, 56, 57, 59, 61, 62,
                   63, 64, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81]

    hard_list = [4, 10, 23, 25, 30, 32, 37, 41, 42, 44, 51, 52, 60, 65, 68, 76, 84, 85,
                 87, 115, 123, 124, 126, 127, 132, 135, 140, 149, 154, 174, 185, 188, 212,
                 214, 218, 220, 224, 233, 239, 262, 273, 282, 295, 297]

    easy_nums = random.sample(easy_list, easy)
    print("Easy:", easy_nums)

    medium_nums = random.sample(medium_list, medium)
    print("Medium:", medium_nums)

    hard_nums = random.sample(hard_list, hard)
    print("Medium:", hard_nums)


def main() -> None:
    leetcode_random_challenge_picker(easy=2, medium=2, hard=2)


if __name__ == '__main__':
    main()
