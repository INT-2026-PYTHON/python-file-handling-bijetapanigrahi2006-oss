"""
## 6. Words in sonnet_words.txt but NOT in sowpods.txt  *(Hard)*

=================================================
WORDS UNIQUE TO THE SONNET
=================================================

Problem Statement:
Read the text files `sowpods.txt` and
`sonnet_words.txt`. PRINT every word that
appears in `sonnet_words.txt` but does NOT
appear in `sowpods.txt`.

This problem is about CHOOSING THE RIGHT DATA
STRUCTURE. If you check each sonnet word
against the SOWPODS list with a nested loop,
the work is O(N*M). Using SETS turns the
membership check into O(1), giving you an
overall O(N + M) algorithm.

-------------------------------------------------
Input Example:
sowpods.txt sample:
   thee
   love
   summer
   day
   eyes
   shall
   more

sonnet_words.txt sample:
   shall
   i
   compare
   thee
   to
   a
   summer
   day

Output Example:
Words in sonnet but not in sowpods:
['a', 'compare', 'i', 'to']
Total: 4

-------------------------------------------------
Explanation:
sonnet words -> {'shall', 'i', 'compare',
                 'thee', 'to', 'a', 'summer',
                 'day'}
sowpods set   -> {'thee', 'love', 'summer',
                  'day', 'eyes', 'shall',
                  'more'}
Difference (sonnet - sowpods)
              -> {'i', 'compare', 'to', 'a'}
After sorting -> ['a', 'compare', 'i', 'to'].
=================================================

"""
def find_subsequence_words(file_path, target):
    matching_words = []
    
    target_lower = target.lower()
    target_len = len(target_lower)
    
    if target_len == 0:
        return matching_words

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip()
                if not word:
                    continue
                
                word_lower = word.lower()
                
            
                word_ptr = 0
                target_ptr = 0
                word_len = len(word_lower)
                
                while word_ptr < word_len and target_ptr < target_len:
                    if word_lower[word_ptr] == target_lower[target_ptr]:
                        target_ptr += 1
                    word_ptr += 1 
                
                if target_ptr == target_len:
                    matching_words.append(word)
                    
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []

    print(f"Words containing '{target}' in order:")
    print(matching_words)
    return matching_words

