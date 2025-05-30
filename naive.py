#!/usr/bin/env python3

def naive_string_matching(text, pattern):
    """
    Naive String Matching Algorithm
    
    Time Complexity: O(n*m) where n is text length and m is pattern length
    Space Complexity: O(1)
    
    This algorithm checks every possible position in the text by comparing
    characters of the pattern with corresponding characters in the text.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
        
    Returns:
        list: List of starting indices where pattern is found
    """
    # Input validation
    if not text or not pattern:
        print("Invalid input: Text or pattern is empty")
        return []
    
    matches = []
    n = len(text)
    m = len(pattern)
    
    # Edge case: pattern longer than text
    if m > n:
        print("Pattern is longer than text.")
        return []
    
    # Try every starting position in the text
    for i in range(n - m + 1):
        # Check if pattern matches at position i
        match_found = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match_found = False
                break  # Mismatch found, break inner loop
        
        if match_found:
            matches.append(i)
    
    # Output results
    if matches:
        print(f"Pattern found at {len(matches)} position(s):")
        for pos in matches:
            print(f"  Index {pos}: '{text[pos:pos+m]}'")
    else:
        print("Pattern not found in the text.")
    
    return matches

def main():
    """Main function to handle user input and display results"""
    print("Naive String Matching Algorithm")
    print("-------------------------------")
    
    text = input("Enter the text: ")
    pattern = input("Enter the pattern: ")
    
    print("\nSearching for pattern in text...")
    naive_string_matching(text, pattern)

if __name__ == "__main__":
    main() 