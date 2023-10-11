
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
                if len(segment) != len(str(number)) or not (0 <= number < 256):
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
        
        
        