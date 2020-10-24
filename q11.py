def main(str1, str2):
    return str1.count(str2) + str1[::-1].count(str2)

if __name__ == "__main__":
    print(
        main(
            input("Input string: "),
            input("Input substring: ")
        )
    )