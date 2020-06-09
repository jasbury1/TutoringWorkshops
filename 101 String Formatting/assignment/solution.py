# Rules:
#   - All letters before the initial vowel are placed at the end of the word
#   - If the word begins with multiple constinants, then all of them are placed
#     at the back of the word
#   - If the word begins with a vowel, it is ignored
#   - After moving (or not moving) the letters, "ay" is added to the end of the 
#     word.

vowels = list("aeiouAEIOU")

def convert_line_pig_latin(line):
    # Given a line of type String with words separated by spaces, return a
    # String with each word converted to pig latin
    output = ""
    words = line.split()

    for word in words:
        output += convert_word_pig_latin(word) + " "

    return output

def convert_word_pig_latin(word):
    # Given a word of type String, return the word translated to pig latin
    i = 0

    while i < len(word) and not word[i] in vowels:
        i += 1

    return word[i:] + word[:i] + "ay"

if __name__ == "__main__":
    input_string = "Python String Formatting is fun"

    pig_latin_string = convert_line_pig_latin(input_string)

    print(pig_latin_string)
