
import string

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

def count_vowels_consonants(tekst):
    
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    char_list = []

    rjecnik = {}

    vowels_list = []

    cons_list = []

    clean_text = (tekst.translate(str.maketrans('', '',
                                    string.punctuation))).lower()
    clean_text = "".join(clean_text.split())
    
    print(clean_text)

    vow_count = 0
    cons_count = 0

    for char in clean_text:
        char_list.append(char)
        
    for c in char_list:
        if c in vowels and c.isalpha():
            vowels_list.append(c)
            vow_count += 1
        elif c.isalpha():
            cons_list.append(c)
            cons_count += 1
    

    rjecnik.update({"vowels": vow_count, "cons": cons_count})
        
    return rjecnik
print(count_vowels_consonants(tekst))

# {'vowels': 30, 'consonants': 48}