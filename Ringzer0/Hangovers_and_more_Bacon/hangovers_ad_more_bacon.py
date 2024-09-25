#WRITE UP BY DAROCH
import re

def bacon_decrypt(ciphertext):
    # bacon Dictionary 
    bacon_dict = {
        'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D', 'AABAA': 'E',
        'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H', 'ABAAA': 'I', 'ABAAB': 'J',
        'ABABA': 'K', 'ABABB': 'L', 'ABBAA': 'M', 'ABBAB': 'N', 'ABBBA': 'O',
        'ABBBB': 'P', 'BAAAA': 'Q', 'BAAAB': 'R', 'BAABA': 'S', 'BAABB': 'T',
        'BABAA': 'U', 'BABAB': 'V', 'BABBA': 'W', 'BABBB': 'X', 'BBAAA': 'Y',
        'BBAAB': 'Z'
    }

    # delete non-letter characters
    clean_text = re.sub(r'[^a-zA-Z]', '', ciphertext)

    # transforms the text to beacon ciphering using A and B
    bacon_text = ''
    for char in clean_text:
        if char.isupper():
            bacon_text += 'B'  # upper -> B
        elif char.islower():
            bacon_text += 'A'  # lower -> A
    
    # group into block of 5 chars
    groups = [bacon_text[i:i+5] for i in range(0, len(bacon_text), 5)]

    #decode using bacon dictionary
    decrypted_message = ''
    for group in groups:
        if group in bacon_dict:
            decrypted_message += bacon_dict[group]
    
    return decrypted_message

ciphertext = "VoiCI unE SUpeRbe reCeTtE cONcontee pAR un GrouPe d'ArtistEs culinaiRe, dONT le BOn Gout et lE SeNs de LA cLasSe n'est limIteE qUe par LE nombre DE cAlOries qU'ils PeUVEnt Ingurgiter. Ces virtuoses de la friteuse vous presente ce petit clip plein de gout savoureux !!"
# run the decoding function
decrypted_message = bacon_decrypt(ciphertext)
print("Decoded message:", decrypted_message)

#FLAG: BACONANDJACKDANIELS

