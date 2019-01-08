def translator(pharse):
    translation = ""

    for letter in pharse:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translator(input("Enter the pharse: ")))
