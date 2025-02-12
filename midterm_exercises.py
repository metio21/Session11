def find_words(filename):
    #name of function is find_words and it take a single parameter "filename" which is going to be the name of the file
    #dog tags are needed and are made by putting 2 exclamation marks and making a space inbetween them
    """
    prints the 3 letter words starting with b
    :param filename: the name of the file
    :return: nothing
    """
    with open(filename, "r") as f: #r stands for reading mode as nothing is going to be edited and with makes sure the file will be closed properly after reading it
        for line in f:
            for p in punctuation:
                line = line.replace(p," ")
            #need to break down the line into words
            words = line.split() # by default splits by space
            #check each word
            for word in words:
                if len(word) == 3 and word.upper()[0] == "Bb":
                    print(word)

find_words("input.txt")




