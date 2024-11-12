#! /usr/bin/python3

def algo(veces):
    print("algo: begin")
    while veces:
        print("algo!")
        veces -= 1
    print("algo: end")

# - [ ] break vs continue vs return

if __name__ == "__main__":

    algo(5)