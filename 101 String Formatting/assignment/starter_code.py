# Rules:
#   - All letters before the initial vowel are placed at the end of the word
#   - If the word begins with multiple constinants, then all of them are placed
#     at the back of the word
#   - If the word begins with a vowel, it is ignored
#   - After moving (or not moving) the letters, "ay" is added to the end of the 
#     word.
# Examples:
#   - fix => ixfay
#   - smile => ilesmay
#   - omlet => omletay

vowels = list("aeiouAEIOU")

def convert_line_pig_latin(line):
    # Given a line of type String with words separated by spaces, return a
    # String with each word converted to pig latin
    pass

def convert_word_pig_latin(word):
    # Given a word of type String, return the word translated to pig latin
    pass

if __name__ == "__main__":
    input_string = "Python String Formatting is fun"

    pig_latin_string = convert_line_pig_latin(input_string)

    print(pig_latin_string)
