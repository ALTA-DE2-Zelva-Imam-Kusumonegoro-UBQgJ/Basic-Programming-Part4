def ubah_huruf(sentence):

    result = ""
    for char in sentence:
        
        if char.isupper():
            result += chr((ord(char) - 55) % 26 + 65)
        else:
            result += " "
 
    return result

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB