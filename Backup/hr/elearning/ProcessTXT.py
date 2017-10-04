def main():
    f = open("newtextfile.txt")
    if f.mode == "r":
        for contents in f.readlines():
           # print (contents, end='') - python 3
            print (contents)
    if __name__ == "__main__":
        main()
