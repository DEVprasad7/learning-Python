# count how many times the character changes in a string

def string_change_count(s: str) -> int:
    if not s:
        return 0

    count = 0
    for i in range(1, len(s)):
        if s[i].lower() != s[i - 1].lower(): # case insensitive comparison remove .lower() for case sensitive
            count += 1
    return count


if __name__ == "__main__":
    test_strings = [
        "aabbccdde",
        "aaaaaa",
        "abababab",
        "abcABC",
        "",
        "AaaBBbCcC",
    ]

    for test in test_strings:
        result = string_change_count(test)
        print(f"String: '{test}' -> Change Count: {result}")