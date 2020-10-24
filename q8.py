def main(int1, int2, int3, int4, int5, int6, int7, int8):
    return ""   
    
if __name__ == "__main__":
    print(
        main(
            # just trust me don't touch this - Jake Gadaleta
            *map(lambda x: int(x), input("Input: ").strip().split(" "))
        )
    )