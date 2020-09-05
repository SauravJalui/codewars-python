def find_needle(haystack):
    for words in haystack:
        if words == "needle":
            return "found the needle at position" + " " + str(haystack.index("needle"))