def vowel_count(string_1):
    count = 0
    vowels = ("a","e","i","o","u")
    for alphabet in string_1:
        if alphabet in vowels:
            count += 1
    print(count)

vowel_count("Soooooo many Vooooowweeeeelllls")

