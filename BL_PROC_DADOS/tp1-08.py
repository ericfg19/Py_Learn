def get_last_syllable(word):
    """
    Função que retorna a última sílaba de uma palavra em inglês.
    """
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    last_vowel_index = -1
    for i in range(len(word) - 1, -1, -1):
        if word[i].lower() in vowels:
            last_vowel_index = i
            break
    if last_vowel_index == -1:
        return word
    else:
        return word[last_vowel_index:].lower()

def classify_rhyme_scheme(poem):
    """
    Função que classifica a forma de rima de um poema.
    """
    last_syllables = [get_last_syllable(word) for line in poem for word in line.split()]
    if len(set(last_syllables)) == 1:
        return "perfeita"
    elif len(set(last_syllables[:2])) == 1 and len(set(last_syllables[2:])) == 1:
        return "par"
    elif len(set(last_syllables[::2])) == 1 and len(set(last_syllables[1::2])) == 1:
        return "cruzada"
    elif len(set(last_syllables[::3] + last_syllables[1::3])) == 1 and len(set(last_syllables[2::3])) == 1:
        return "concha"
    else:
        return "livre"

poem = ["Roses are red", "Violets are blue", "Sugar is sweet", "And so are you"]
print(classify_rhyme_scheme(poem))  # saída: "livre"