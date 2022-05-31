def main():
    name_of_file = "numbers.txt"

    infile = open( "numbers.txt", 'r')
    
    line = infile.readline()

    total = 0

    while line != '':
      total += int(line)
      line = infile.readline()

    print(total)

    infile.close()
main()