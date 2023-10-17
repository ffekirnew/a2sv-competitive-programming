def palindrome_pad(s):
    """
    Transforms a string such that all palindrome substrings have odd length:
    * 'aa' -> 'a!a'
    * 'abba' -> 'a!b!b!a'
    * 'aba' -> 'a!b!a'
    """
    assert '!' not in s
    return '!'.join(s)

def palindrome_unpad(padded):
    return padded.replace('!', '')

def unpadded_length(padded):
    if not padded:
        return 0
    if padded[0] == '!':
        return (len(padded) - 1) / 2
    return (len(padded) + 1) / 2

def longest_palindrome(s):
    s = palindrome_pad(s)
    best = ''
    best_right = -1
    best_center = -1
    # radius[center] = best expansion radius found for that center
    radius = [0] * len(s)

    for center in range(len(s)):
        if center <= best_right:
            # Manacher's optimization:
            # The new center is inside a bigger palindrome expansion
            # from earlier. We can skip the first steps of the expansion,
            # since they are equivalent to what we have already computed
            # for the center's mirror.
            mirror = best_center - (center - best_center)
            radius[center] = min(best_right - center, radius[mirror])
        else:
            # Normal case when we do not have any prior knowledge
            radius[center] = 1

        # Expand symetrically as long as the palindrome property holds
        left = center - radius[center]
        right = center + radius[center]
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            radius[center] += 1
        # The last move broke the palindrome property, undo it
        left += 1
        right -= 1
        radius[center] -= 1
        palindrome = s[left:right+1]
        # Record the palindrome if longest
        if unpadded_length(palindrome) > unpadded_length(best):
            best = palindrome
        # Manacher's optimization:
        # Keep track of the rightmost palindrome seen so far
        if right > best_right:
            best_right = right
            best_center = center

    return palindrome_unpad(best)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return longest_palindrome(s)