"""
Solution Steps:
1. Check if the string is an ipv4, ipv6 or neither candidate just by using the charachters '.' and ':'
2. Run the respective checks
    2.1. If IPv4, check using the rules
    2.2. If IPv6, check using the rules
3. Return the results

Complexity Analysis:
- Time Complexity: O(n)
- Space complexity: O(n)
    where: n = length of string
"""


class ValidateIpAddress:
    def __init__(self, query_ip: str):
        self.query_ip = query_ip
    
    def _check_ipv4(self, query_ip: str):
        segments = query_ip.split('.')

        if len(segments) != 4:
            return "Neither"

        for segment in segments:
            try:
                number = int(segment)
                if not(len(segment) == len(str(number)) and 0 <= number < 256):
                    return "Neither"
            except:
                return "Neither"

        return "IPv4"

    def _check_ipv6(self, query_ip: str):
        segments = query_ip.split(':')

        if len(segments) != 8:
            return "Neither"

        for segment in segments:
            if not 1 <= len(segment) <= 4:
                return "Neither"

            for char in segment:
                if not ('0' <= char <= '9' or 'a' <= char <= 'f' or 'A' <= char <= 'F'):
                    return "Neither"

        return "IPv6"

    
    def run(self):
        ipv4_candidate = '.' in self.query_ip
        ipv6_candidate = ':' in self.query_ip
        
        if ipv4_candidate and ipv6_candidate:
            return "Neither"
        elif ipv4_candidate:
            return self._check_ipv4(self.query_ip)
        elif ipv6_candidate:
            return self._check_ipv6(self.query_ip)
        else:
            return "Neither"


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        solution = ValidateIpAddress(queryIP)
        return solution.run()
        
        
        