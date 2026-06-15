"""
## 4. Find All Palindrome Words  *(Medium)*

=================================================
PALINDROME WORDS
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every PALINDROME word (a word that reads the
same forwards and backwards).

Write a helper FUNCTION called `is_palindrome`
that takes a single word and returns True if
it is a palindrome, else False. Pass every
word in the file to this function ONE AT A
TIME.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
hello
noon
civic
python
deified
racecar
banana

Output Example:
level
radar
noon
civic
deified
racecar
Total palindromes: 6

-------------------------------------------------
Explanation:
- "level"    reversed -> "level"   -> palindrome
- "radar"    reversed -> "radar"   -> palindrome
- "hello"    reversed -> "olleh"   -> not
- "noon"     reversed -> "noon"    -> palindrome
- "civic"    reversed -> "civic"   -> palindrome
- "python"   reversed -> "nohtyp"  -> not
- "deified"  reversed -> "deified" -> palindrome
- "racecar"  reversed -> "racecar" -> palindrome
- "banana"   reversed -> "ananab"  -> not
=================================================

"""
def find_vowel_heavy_words(file_path):
    
    target_vowels = {'a', 'e', 'i', 'o', 'u'}
    all_vowel_words = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip()
                if not word:
                    continue
                
            
                word_chars = set(word.lower())
                
            
                if target_vowels.issubset(word_chars):
                    all_vowel_words.append(word)
                    
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []
        
    print("Words containing all five vowels:")
    print(all_vowel_words)
    return all_vowel_words



