"""Task : Take string as input and print the number of vowels, consonants in that string also print the length of the string."""

string = input("ENTER A STRING: ")
string = string.lower()
prin("LENGTH OF THE STRING IS:", len(string))
vowel = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
consonant_count = 0
for charachter in string:
    i charachter in vowel:
        vowel_count += 1
    else:
        consonant_count += 1
prin(f'TOTAL VOWELS IN THE STRING YOU ENTERED ARE: {vowel_count} ')
prin(f'TOTAL CONSONANTS IN THE STRING YOU ENTERED ARE: {consonant_count} ')
