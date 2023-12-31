# Assigning each letter to a value
alphabets = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}
vowels = "a,e,i,o,u"
consonants_substrings = []
consonant_value = 0
consonant_value_list = []

# Calculates the values of the consonant substrings and returns the highest value
def substring_value(consonants_substrings):
    for substring in consonants_substrings:
        if len(substring) == 1:
            value = alphabets[substring]
            global consonant_value
            consonant_value += value
            consonant_value_list.append(consonant_value)
            consonant_value = 0
        else:
            for character in substring:
                value = alphabets[character]
                consonant_value += value
            consonant_value_list.append(consonant_value)
            consonant_value = 0

    print(f"Highest consonant substring value: {max(consonant_value_list)}")

# Splits a word and removes the vowels to get consonant substrings
def get_consonants(string):
    if " " in string:
        print("No spaces")

    else:
        filtered_vowels = list(filter(lambda character: character in vowels, string))
        if filtered_vowels == []:
            consonants_substrings.append(string)
            substring_value(consonants_substrings)
        else: 
            filtered_vowels = list(filter(lambda character: character in vowels, string))
            for vowel in filtered_vowels:
                if string.find(f"{vowel}") == 0 or string.find(f"{vowel}") == len(string) - 1:
                    string = string.replace(f"{vowel}", "")
                substrings = (word for word in string.split(f"{vowel}"))
                for substring in substrings:
                    string = substring
                    if any(vowel in filtered_vowels for vowel in string) == False:
                        consonants_substrings.append(string)

        print(f"Consonant substrings: {consonants_substrings}")
        substring_value(consonants_substrings)
        
# Takes a string input         
get_consonants(input("Enter: "))
 
