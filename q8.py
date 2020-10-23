def main(int1: int, int2: int, int3: int, int4: int, int5:int, int6:int, int7:int, int8:int):
    return ""   
    
if __name__ == "__main__":
    print(
        main(
            # just trust me don't touch this - Jake Gadaleta
            *map(lambda x: int(x), input("Input: ").strip().split(" "))
        )
    )