"""
## 5. Longest Palindrome in the File  *(Hard)*

=================================================
LONGEST PALINDROME
=================================================

Problem Statement:
Read the text file `sowpods.txt` and find the
LONGEST PALINDROME word in the file.

If multiple palindromes share the maximum
length, print ALL of them.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
noon
civic
deified
racecar
rotator
malayalam

Output Example:
Longest palindrome length: 9
malayalam

-------------------------------------------------
Explanation:
Lengths of the palindromes in the sample:
   level    -> 5
   radar    -> 5
   noon     -> 4
   civic    -> 5
   deified  -> 7
   racecar  -> 7
   rotator  -> 7
   malayalam -> 9
The longest is "malayalam" with 9 characters.
=================================================

"""
def find_longest_palindromes(file_path):
    longest_palindromes = []
    max_length = 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                
                word = line.strip()
                if not word:
                    continue
                
                normalized_word = word.lower()
                if normalized_word == normalized_word[::-1]:
                    word_len = len(word)
                    
                    if word_len > max_length:
                        max_length = word_len
                        longest_palindromes = [word] 
                        
                    elif word_len == max_length:
                        longest_palindromes.append(word)
                        
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return
        
    print(f"Longest palindrome length: {max_length}")
    for palindrome in longest_palindromes:
        print(palindrome)


# --- Driver and Verification Code ---
_name_ = " "
if _name_ == "_main_":
   
    sample_filename = "sowpods.txt"
    sample_data = [
        "level", "radar", "noon", "civic", 
        "deified", "racecar", "rotator", "malayalam"
    ]
    
    with open(sample_filename, "w", encoding="utf-8") as f:
        f.write("\n".join(sample_data))
        
    # Execute function
    find_longest_palindromes(sample_filename)
