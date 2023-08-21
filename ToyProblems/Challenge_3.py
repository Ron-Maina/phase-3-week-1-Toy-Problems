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
consonants = []

def substring_value(character):
        highest = 0
        value = alphabets[character]
        highest += value
        print(highest)

def get_consonants(string):
    if " " in string:
        print("No spaces")

    else:
        filtered_vowels = list(filter(lambda character: character in vowels, string))
        if filtered_vowels == []:
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
                        consonants.append(string)
        print(consonants)
        for substring in consonants:
            if len(substring) == 1:
                substring_value(substring)
            else:
                for characters in substring:
                    substring_value(characters)




                            # for vowel in filtered_vowels:
            #     if string.find(f"{vowel}") == 0 or string.find(f"{vowel}") == len(string) - 1:
            #         string = string.replace(f"{vowel}", "")
            #         if any(char in filtered_vowels for char in string) == True:
            #             substrings = (word for word in string.split(f"{vowel}"))
            #             for x in substrings:
            #                 print(x)
            #     else:
            #         substrings = (word for word in string.split(f"{vowel}"))
            #         for substring in substrings:
            #             string = substring
            #             print(string)
        




            # if vowel in string[0] or string[-1]:
            #     print(vowel)
                # string = string.replace(f"{vowel}", "")
                # print(string)
            # substrings = (word for word in string.split(f"{vowel}"))
        
        # for character in vowels:
        #     print(character)
        #     substrings = (word for word in string.split(f"{character}"))
        #     for substring in substrings:
        #         string = substring
        #         print(string)

                
                
               
            
get_consonants(input("Enter: "))
 
