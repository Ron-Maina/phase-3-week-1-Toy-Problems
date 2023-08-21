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
def substring_value(substring):
    for character in substring: 
        value = alphabets[character]
        global consonant_value
        consonant_value += value

    consonant_value_list.append(consonant_value)
    consonant_value = 0

    # print(f"Highest consonant substring value: {max(consonant_value_list)}")

def get_consonants(string):
    if " " in string:
        print("No spaces")

    else:
        filtered_vowels = list(filter(lambda character: character in vowels, string))
        if filtered_vowels == []:
            consonants_substrings.append(string)
            for character in string:
                substring_value(character)
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
        print(f"Highest consonant substring value: {max(consonant_value_list)}")

        for substring in consonants_substrings:
            substring_value(substring)
           
get_consonants(input("Enter: "))
 
