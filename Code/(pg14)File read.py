def main():
    #Open file philosopher.txt
    infile = open("philosophers", "r")

    #Read the file's contents.
    file_contents = infile.read()

    #Close the file
    infile.close()

    #Print the data that was read into memory.
    print(file_contents)

main()