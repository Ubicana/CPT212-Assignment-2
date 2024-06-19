def boyer_moore(pattern, text):
    # Implement bad character heuristic function to find the bad character shift table
    def bad_character_heuristic(pattern, size):
        # Initialize all occurrences as -1 to indicate that the character does not occur in the pattern
        bad_char = [-1] * 256
        # Loop to fill the actual value of last occurrence of a character
        for i in range(size):
            # Use the ord() function returns the ASCII value of the character
            bad_char[ord(pattern[i])] = i
        # 'bad_char' represents for bad character shift table
        return bad_char

    # Implement good suffix heuristic function to find the good suffix shift table
    def good_suffix_heuristic(pattern, size):
        # Initialize all occurrences as -1 to indicate that there is no good suffix shift for the corresponding position in the pattern
        suffix = [-1] * size
        # Initialize all occurrences of shift as False
        prefix = [False] * size
        # loop to fill the actual value of last occurrence of a character
        for i in reversed(range(size)):
            # If the current character is the same as the first character of the pattern, then the pattern is a prefix
            if i == size - 1 or pattern[i] != pattern[i + 1]:
                prefix[i] = pattern[i] == pattern[0]
            else:
                prefix[i] = prefix[i + 1]
            j = i + 1
            # Do inner loop to find the longest suffix which is also a prefix of the pattern
            while j < size and pattern[i] != pattern[j]:
                if suffix[j] == -1:
                    suffix[j] = j - i
                j += 1

        # If the suffix is a prefix, then the shift is the length of the pattern minus the position of the suffix
        if suffix[size - 1] == -1:
            suffix[size - 1] = size
        j = 0
        # Use the reversed loop to fill the actual value of last occurrence of a character
        for i in reversed(range(size - 1)):
            if pattern[i] == pattern[j]:
                j += 1
            else:
                j = 0
            if suffix[i - 1] == -1:
                suffix[i - 1] = j
        # 'suffix' and 'prefix' represents for good suffix shift table
        return suffix, prefix

    # Implement search function to find the pattern in the text
    def search(pattern, text):
        m = len(pattern)
        n = len(text)
        # Call the bad character and good suffix heuristic functions
        bad_char = bad_character_heuristic(pattern, m)
        suffix, prefix = good_suffix_heuristic(pattern, m)
        s = 0  # 's' is the starting index of the pattern in the text
        indices = []  # List to store starting indices of the pattern
        # Loop to find the pattern in the text
        while s <= n - m:
            j = m - 1
            # Loop to compare the pattern with the text
            while j >= 0 and pattern[j] == text[s + j]:
                j -= 1
            # If the pattern is found in the text
            if j < 0:
                # Add the starting index of the pattern to the list
                indices.append(s)
                # If the pattern is found, shift the pattern to the right based on the good suffix shift table
                if m < n:
                    suffix_value = suffix[0]
                else:
                    suffix_value = 1
                # Calculate the shift based on the good suffix shift table and the bad character shift table when the pattern is found
                s += max(suffix_value, m - bad_char[ord(text[s])])
            else:
                if j != m - 1:
                    suffix_value = suffix[j]
                else:
                    suffix_value = 1
                # Calculate the shift based on the good suffix shift table and the bad character shift table when there is a mismatch
                s += max(suffix_value, j - bad_char[ord(text[s + j])])
        # 'indices' is the list of starting indices where pattern is found in text
        return indices

    # Call the search function to find the pattern in the text
    return search(pattern, text)

# Function to test the Boyer-Moore algorithm
def test_boyer_moore(pattern, text):
    # Call the Boyer-Moore algorithm
    indices = boyer_moore(pattern, text)
    if indices:  # If the pattern is found in the text
        print(f"The word '{pattern}' starts at index {indices} in the text.")
    else:  # If the pattern is not found in the text
        print(f"Failed to find the word '{pattern}' in the text.")

# main() function to call the test cases
def main():
    # Test Case #1
    text = "XXYXXWXXZXXYXXYX"
    pattern = "XXYX"
    print("\nTest Case #1")
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    test_boyer_moore(pattern, text)

    # Test Case #2
    text = "COMPUTER SCIENCE"
    pattern = "SCIENCES"
    print("\nTest Case #2")
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    test_boyer_moore(pattern, text)

# Call the main function
main()