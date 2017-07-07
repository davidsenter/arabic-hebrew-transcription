import numpy

def read_input_file(filename):
    word_list = []
    f = open(str(filename), "r")
    for word in f:
        word_list.append(word.replace("\n", ""))
    f.close()
    return word_list

def read_dictionary_file(filename):
    dictionary = {}
    f = open(str(filename), "r")
    for line in f:
        key_char = line.split("/")[0].replace(" ", "").replace("\t", "").strip()
        # print key_char
        # print len(key_char)
        if len(key_char) == 2:
            key = str(ord(key_char[0])) + "," + str(ord(key_char[1]))
        else:
            key = str(ord(key_char[0])) + "," + str(ord(key_char[1])) + "," + str(ord(key_char[2])) + "," + str(ord(key_char[3]))
        value = line.split("/")[1].replace(" ", "").replace("\t", "").strip()
        dictionary[tuple(key.split(","))] = value
    f.close()
    return dictionary

def get_unicode_points(word_list):
    point_list = []
    for i in range(len(word_list)):
        point_list.append([])
        for char in word_list[i]:
            point_list[i].append(str(ord(char)))
    return point_list

def transliterate(point_list, dictionary):
    trans_words = []
    for word in range(len(point_list)):
        trans_word = ""
        begin = True
        for i in range(len(point_list[word]) / 2):
            if i > 0:
                begin = False
            if i < len(point_list[word]) / 2 - 1:
                print point_list[word][2 * i]
                key_poss = tuple([point_list[word][2 * i], point_list[word][2 * i + 1], point_list[word][2 * i + 2], point_list[word][2 * i + 3]])
                if dictionary.has_key(key_poss):
                    trans_word += dictionary[key_poss]
                elif dictionary.has_key(key_poss[0:2]):
                    trans_word += dictionary[key_poss[0:2]]
                else:
                    trans_word += chr(int(point_list[word][2 * i])) + chr(int(point_list[word][2 * i + 1]))
                    print "character does not exist:", key_poss, "or", key_poss[0:2]
                    print chr(int(point_list[word][2 * i])) + chr(int(point_list[word][2 * i + 1])) + chr(int(point_list[word][2 * i + 2])) + chr(int(point_list[word][2 * i + 3]))
                    print chr(int(point_list[word][2 * i])) + chr(int(point_list[word][2 * i + 1]))
            else:
                key_poss = tuple([point_list[word][2 * i], point_list[word][2 * i + 1]])
                if dictionary.has_key(key_poss):
                    trans_word += dictionary[key_poss]
                else:
                    trans_word += chr(int(point_list[word][2 * i])) + chr(int(point_list[word][2 * i + 1]))
                    print "character does not exist:", key_poss
                    print chr(int(point_list[word][2 * i])) + chr(int(point_list[word][2 * i + 1]))
        trans_words.append(trans_word)
    return trans_words

def printdict(dicti):
	for key in dicti.keys():
		print key, ':', dicti[key]

dictionary = read_dictionary_file("dictionary_arb.txt")
word_list = read_input_file("test_list_arb.txt")
point_list = get_unicode_points(word_list)
printdict(dictionary)
print point_list
print transliterate(point_list, dictionary)
