from collections import defaultdict


class Solution:
  def sortVowels(self, s: str) -> str:
    vowels = [ 'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u' ]
    vowels_set = set(vowels)

    vowels_counter = defaultdict(int)
    
    result = []
    for letter in s:
      if letter in vowels_set:
        vowels_counter[letter] += 1
        result.append(False)
      else:
        result.append(letter)
        
    best_vowel_index = 0
    for i, letter in enumerate(s):
      if not result[i]:
        while vowels_counter[vowels[best_vowel_index]] == 0:
          best_vowel_index += 1
        
        result[i] = vowels[best_vowel_index]
        vowels_counter[vowels[best_vowel_index]] -= 1
    
    return "".join(result)
      