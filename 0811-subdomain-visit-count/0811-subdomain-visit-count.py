class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # create the object to  be returned
        answer = []
        counter = defaultdict(int)
        # for every cpdomain, find each domain and amount of time visited
        for item in cpdomains:
            visit_count, domain = item.split()
            visit_count = int(visit_count)
            while domain:
                counter[domain] += visit_count
                try:
                    domain = domain[domain.index('.') + 1:]
                except ValueError:
                    break
        # return the solution
        for key, value in counter.items():
            answer.append(str(value) + " " + key)
        return answer
        