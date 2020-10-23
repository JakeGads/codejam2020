def main(int1: int, int2: int):
   return "Your return here"

if __name__ == "__main__":
    print(
        main(
            int(input("Enter numerator: ")),
            int(input("Enter denominator: "))
        )
    )