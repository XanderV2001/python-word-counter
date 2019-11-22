while True:
    readFile = input("Read string from a file? [y/n]: ")
    count = 0
    if(readFile == 'y' or readFile == 'Y'):
        filePath = input("Path to file: ")
        f = open(filePath, 'r')
        string = f.read()
        words = string.split(' ')
        for x in words:
            count += 1

        print("That file has '{}' words.".format(count))
    elif(readFile == 'n' or readFile == "N"):
        inputString = input("Input a string you want to count: ")
        inputWords = inputString.split(' ')
        for word in inputWords:
            count += 1

        print("The string you've entered has '{}' words.".format(count))
    else:
        print("'{}' is not a valid option. Please choose 'y' or 'n'".format(readFile))
