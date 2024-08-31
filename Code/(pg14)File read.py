def main():
    infile = open("philosophers", "r")

    file_contents = infile.read()

    infile.close()

    print(file_contents)

main()