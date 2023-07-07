class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # create the object to be returned
        answer = 0

        # do it to make max consec T's ones and then F's
        for current_protagonist in ['T', 'F']:
            # set up the sliding window
            s, ops = 0, 0
            for e in range(len(answerKey)):
                ops += answerKey[e] != current_protagonist # operation needed
                while ops > k:
                    ops -= answerKey[s] != current_protagonist # operation cleared
                    s += 1

                answer = max(answer, e - s + 1)

        # return the solution
        return answer
        