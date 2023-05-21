from collections import defaultdict, deque
#User function Template for python3

class Solution:
    @staticmethod
    def buildGraph(list_of_words, n):
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        
        for index in range(n - 1):
            word1, word2 = list_of_words[index], list_of_words[index + 1]
    
            i = 0
            while i < len(word1) and i < len(word2) and word1[i] == word2[i]:
                i += 1
            
            if i < len(word1) and i < len(word2):
                graph[word1[i]].append(word2[i])
                in_degree[word1[i]] += 0
                in_degree[word2[i]] += 1
            
            j = i
            while i < len(word1):
                in_degree[word1[i]] += 0
                i += 1
                
            while j < len(word2):
                in_degree[word2[j]] += 0
                j += 1
        
        return graph, in_degree
        
    def findOrder(self,alien_dict, N, K):
        graph, in_degree = self.buildGraph(alien_dict, N)
        queue = deque([char for char, degree in in_degree.items() if not degree])
        answer = []
        
        while queue:
            char = queue.popleft()
            
            answer.append(char)
            
            for child in graph[char]:
                in_degree[child] -= 1
                
                if not in_degree[child]:
                    queue.append(child)
        
        return answer



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends
