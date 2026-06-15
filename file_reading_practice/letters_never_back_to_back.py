"""
## 2. Alphabets That Never Appear Back-to-Back  *(Medium)*

=================================================
ALPHABETS NEVER IN SEQUENCE
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every alphabet letter that:
   - APPEARS at least once in the words of
     the file, AND
   - NEVER appears TWICE IN A ROW (back-to-back)
     in ANY word of the file.

Letters that never appear in the file at all
should NOT be in the answer. Letters that
appear back-to-back at least once (like the
'u' in "vacuum") should also be excluded.

-------------------------------------------------
Input Example (sowpods.txt sample):
aardvark
hello
buzz
moon
puppy

Output Example:
Letters that never appear back-to-back:
['b', 'd', 'e', 'h', 'k', 'm', 'n', 'r', 'u', 'v', 'y']

-------------------------------------------------
Explanation:
Letters seen anywhere in the sample:
   aardvark -> a, r, d, v, k
   hello    -> h, e, l, o
   buzz     -> b, u, z
   moon     -> m, o, n
   puppy    -> p, u, y
   seen    = {a, b, d, e, h, k, l, m, n, o,
              p, r, u, v, y, z}

Letters that ever appear back-to-back:
   aa (aardvark), ll (hello), zz (buzz),
   oo (moon),     pp (puppy)
   doubled = {a, l, z, o, p}

Answer = seen - doubled
       = {b, d, e, h, k, m, n, r, u, v, y}
Sorted -> ['b', 'd', 'e', 'h', 'k', 'm', 'n',
           'r', 'u', 'v', 'y']
=================================================

"""
def find_non_consecutive_letters(file_path):

    seen_letters = set()
    doubled_letters = set()
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                
                word = line.strip().lower()
                if not word:
                    continue
                
                for i, char in enumerate(word):
                    if char.isalpha():
                        seen_letters.add(char)
                        
                        if i < len(word) - 1 and word[i] == word[i + 1]:
                            doubled_letters.add(char)
                            
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []

    
    valid_letters = seen_letters - doubled_letters
    
    return sorted(list(valid_letters))


# --- Simulation/Driver Code ---
_name_ = " "
if _name_ == "_main_":
    
    mock_filename = "sowpods.txt"
    sample_words = ["aardvark", "hello", "buzz", "moon", "puppy"]
    
    with open(mock_filename, "w", encoding="utf-8") as f:
        f.write("\n".join(sample_words))
        
    result = find_non_consecutive_letters(mock_filename)
    
    print("Letters that never appear back-to-back:")
    print(result)
