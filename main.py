# function that will take text from the book as string and return the number of words in the string
def count_words(text):
    words = text.split()
    return len(words)


# function that will read the book, lowercase text and return the number of times each character appears in the text
def count_characters(text):
    text = text.lower()
    result = {}
    for char in text:
        if char.isalpha():
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
    return result

# function that will open and read the book from the directory and filename
def read_book(dir, filename):
    with open(dir + filename) as f:
        return f.read()

# function that will return the directory/filename of the book
def get_filename(dir, filename):
    return dir + filename


# function that will create a report of the number of words and characters in the book
def create_report(filename, words, characters):
    report = f"--- Begin report of {filename} ---" + "\n"
    report += str(words) + " words found in the document " +  "\n" + "\n"
    # turn characters into a list and interate over it
    characters = list(characters.items())
    
    # sort by occurence
    characters.sort(key=lambda x: x[1], reverse=True)
    for char, count in characters:
        report += f"The '{char}' character was found {count} times\n"
    report += "--- End report ---"
    return report

def main():
    book = read_book("books/", "frankenstein.txt")
    words = count_words(book)
    characters = count_characters(book)
    filename = get_filename("books/", "frankenstein.txt")
    report = create_report(filename, words, characters)
    print(report)


main()
