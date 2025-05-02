from greeting import print_hi as hi
import greeting as hello

def main():
    hello.print_hi("Frank")
    hi("Freda")

if __name__ == "__main__":
    main()