# Source id: 3 # Personal reference.
# You are given a list of words and a string containing letters to filter by.
# The output must be a list of the input words that contain one or more letters in the string.
# Example:
# words = ["the", "dog", "bat", "change"]
# filter = "ae"
# output = ["the", "bat", "change"]

type Words = list[str]
type FilterDict = set[str]

def filter_words(words: Words, filter: str) -> Words:
    if len(filter) == 0:
        return words  # This is assumed behavior. I don't remember seeing any clarification on this in the assessment.
    result = []
    filter_set = {char for char in filter}
    for word in words:
        for char in word:
            if char in filter_set:
                result.append(word)
                break

    return result



# def reset_dict(filter: str) - FilterDict:
#     {}

if __name__ == "__main__":
    print("Example 1:")
    words = ["the", "dog", "bat", "change"]
    filter = "ae"
    expected_output = ["the", "bat", "change"]
    print(f"{words=}")
    print(f"{filter=}")
    print(f"{expected_output=}")
    assert filter_words(words, filter) == expected_output

    print("\nExample 2:")
    words = []
    filter = "ae"
    expected_output = []
    print(f"{words=}")
    print(f"{filter=}")
    print(f"{expected_output=}")
    print(f"{filter_words(words, filter)=}")
    assert filter_words(words, filter) == expected_output

    print("\nExample 3:")
    words = ["the", "dog", "bat", "change"]
    filter = ""
    expected_output = ["the", "dog", "bat", "change"]
    print(f"{words=}")
    print(f"{filter=}")
    print(f"{expected_output=}")
    print(f"{filter_words(words, filter)=}")
    assert filter_words(words, filter) == expected_output

    print("\nExample 4:")
    words = ["the", "dog", "bat", "change"]
    filter = " "
    expected_output = []
    print(f"{words=}")
    print(f"{filter=}")
    print(f"{expected_output=}")
    print(f"{filter_words(words, filter)=}")
    assert filter_words(words, filter) == expected_output