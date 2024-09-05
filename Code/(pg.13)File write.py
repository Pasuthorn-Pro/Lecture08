def main():
    #Open a file named philosophers.txt.
    outfile = open("philosophers", "w")

    #Write names of three philosophers to the file.
    outfile.write("John Lorke\n")
    outfile.write("David Hume\n")
    outfile.write("Emund Burke\n")
    outfile.write("Pasuthorn\n")

    #Close the file.
    outfile.close()

main()