def read_file(filename):
    ''' Read file with filename
            Read one line as one string and return a list of string.

        :param filename: str
        :return: a list of string
        '''
    lines = open(filename).read().splitlines()
    return lines

def print_length(lines):
    ''' Display length of string (lines).
            Each line shows one string length and the string, separated by colon (:)
            and ended with comma (,).

        :param lines: a list of string

        >>> print_length(['an', 'be', 'co'])
        2 : an,
        2 : be,
        2 : co,
        >>> print_length(['an', 'ant', 'a'])
        2 : an,
        3 : ant,
        1 : a,
        >>> print_length(['be', 'b', ''])
        2 : be,
        1 : b,
        0 : ,

        '''
    for t in range(len(lines)):
        print(f"{len(lines[t])} : {lines[t]},")

def search_by_index(
                    text,
                    index):
    ''' Look for a character of string text at the given index

        :param text: str
        :param index: int
        :return: str

        >>> search_by_index('hello', 1)
        'e'
        >>> search_by_index('hello', 4)
        'o'
        >>> search_by_index('hi how are you', 2)
        ' '
        '''
    for i in range(len(text)):
        return text[index]

def count(
          text,
          char):
    ''' Count a number of character char inside string text

        :param text: str
        :param char: str
        :return: int

        >>> count('hello', 'l')
        2
        >>> count('hello', 's')
        0
        >>> count('banana', 'a')
        3
        '''
    for i in range(len(text)):
        return text.count(char)

def find_char(
              text,
              char):
    ''' Find indexes of all character char found inside string text

        :param text: str
        :param char: str
        :return: a list of int

        >>> find_char('hello', 'l')
        [2, 3]
        >>> find_char('hello', 's')
        []
        >>> find_char('banana', 'a')
        [1, 3, 5]
        '''
    list1 = []
    for i in range(len(text)):
        if text[i] == char:
            list1.append(i)
    return list1

def find_word(
              text,
              word):
    ''' Look for string word inside string text
            If word is found, return True and a list of first index of each word
            If word is not found, return False and empty list

        :param text: str
        :param word: str
        :return: a list of int

        >>> find_word('banana', 'na')
        (True, [2, 4])
        >>> find_word('car care', 'car')
        (True, [0, 4])
        >>> find_word('banana', 'boat')
        (False, [])
        '''
    if word.lower() in text.lower():
        list1 = []
        for i in range(len(text)):
            if word.lower() == text.lower()[i:i + len(word)]:
                list1.append(i)
        return True, list1
    else:
        return False, " "

def operate(
            lines,
            choice):
    ''' Receive a list of string and user's choice
            Perform action corresponding to the choice

            :param lines: a list of string
            :param choice: int
        '''
    if choice == 1:
        print_length(lines)
    elif choice == 2:
        index = int(input("Enter index: "))
        for i in range(len(lines)):
            print(f"{search_by_index(lines[i], index)} : {lines[i]}")
    elif choice == 3:
        char = str(input("Enter character: "))
        for i in range(len(lines)):
            print(f"{count(lines[i], char)} : {lines[i]}")
    elif choice == 4:
        char = str(input("Enter character: "))
        for i in range(len(lines)):
            print(f"{find_char(lines[i], char)} : {lines[i]}")
    else:
        word = str(input("Enter a word: "))
        for i in range(len(lines)):
            print(f"{find_word(lines[i], word)[1]} : {lines[i]}")

# Main
filename = "quotes.txt"
lines = read_file(filename)
print(lines)      # Uncomment this line to see what lines look like
print('1. Print length')
print('2. Show character by index')
print('3. Count character')
print('4. Find character')
print('5. Find word')
choice = int(input('Enter choice: '))
operate(lines, choice)


if __name__ == "__main__":
    import doctest
    doctest.testmod()


