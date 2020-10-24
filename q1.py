def main(str1, str2):
    incorrect_count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            incorrect_count += 1
    
    return f"There are {incorrect_count} differences" # only return answer on submission


if __name__ == "__main__":
    print(
        main( 
            input("Enter first word: "),
            input("Enter second word: ")
        )
    )