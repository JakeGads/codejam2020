def main(str1, str2, int1, int2):
    return "return"

if __name__ == "__main__":
    print(
        main(
            input("Enter the start time of train A: "),
            input("Enter the start time of train B: "),
            int(input("Enter the speed of train A: ")),
            int(input("Enter the speed of train B: "))
        )
    )