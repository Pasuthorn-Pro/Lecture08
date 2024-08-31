def main():
    #Open a file named philosophers.txt.
    outfile = open("philosophers", "w")

    outfile.write("John Lorke\n")
    outfile.write("David Hume\n")
    outfile.write("Emund Burke\n")

    outfile.close()

main()