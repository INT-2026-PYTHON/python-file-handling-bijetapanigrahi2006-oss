"""
## 3. Words Containing All Five Vowels  *(Medium)*

=================================================
WORDS WITH ALL VOWELS
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every word that contains ALL FIVE vowels
('a', 'e', 'i', 'o', 'u') at least once.
The order of the vowels does NOT matter, and
the check should be case-insensitive.


-------------------------------------------------
Input Example (sowpods.txt sample):
education
sequoia
facetious
hello
audio
unequivocal

Output Example:
education
sequoia
facetious
unequivocal
Total words with all vowels: 4

-------------------------------------------------
Explanation:
- "education" contains a, e, i, o, u -> yes
- "sequoia"   contains a, e, i, o, u -> yes
- "facetious" contains a, e, i, o, u -> yes
- "hello"     missing a, i, o, u     -> no
- "audio"     missing e               -> no
- "unequivocal" contains a,e,i,o,u   -> yes
=================================================

"""
def find_longest_words(file_path):
    longest_words = []
    max_length = 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:

                word = line.strip()
                if not word:
                    continue
                
                word_len = len(word)
                
                if word_len > max_length:
                    max_length = word_len
                    longest_words = [word] 
                    
                elif word_len == max_length:
                    longest_words.append(word)
                    
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []
        
    print(f"Longest word length: {max_length}")
    print("Longest words:")
    print(longest_words)
    
    return longest_words


# --- Simulation / Driver Code ---
_name_ = " "
if _name_ == "_main_":
    
    sample_filename = "sowpods.txt"
    sample_data = [
        "apple",
        "banana",
        "cherry",
        "date",
        "elderberry"
    ]
    
    with open(sample_filename, "w", encoding="utf-8") as f:
        f.write("\n".join(sample_data))
        
    find_longest_words(sample_filename)
