"""
Note:
    - Amount exceeds $1000, invalid by it's own
    - Happened inside 60 minutes of another transaction with the same name

Solution Steps:
1. Clean up the transaction so that it's easily usable
2. Traverse the transactions and find the invalid ones
    2.1. Invalid transaction if amount > 1000, remove it
    2.2. Invalid transaction if close to another transaction, record it, but keep it.
3. Return the results
"""

class InvalidTransactions:
    def __init__(self, transactions: List[str]):
        """No side-effects."""
        self.transactions = transactions
    
    def _set_up(self) -> None:
        for index, transaction in enumerate(self.transactions):
            name, time, amount, city = transaction.split(",")
            self.transactions[index] = [name, int(time), int(amount), city, index]

        self.transactions.sort()
        
    
    def solve(self) -> List[str]:
        self.transactions.sort()
        
        # clean-up
        self._set_up()
        
        invalid_transactions = set()
        buffer = []
        for index, transaction in enumerate(self.transactions):
            if transaction[2] > 1000:
                buffer.append(transaction)
                invalid_transactions.add(index)

            for other_index in range(index - 1, -1, -1):
                prev_transaction = self.transactions[other_index]
                
                if transaction[0] != prev_transaction[0]:
                    break

                if transaction[1] - prev_transaction[1] <= 60 and transaction[3] != prev_transaction[3]:
                    
                    if other_index not in invalid_transactions:
                        invalid_transactions.add(other_index)
                        buffer.append(prev_transaction)
                    
                    if index not in invalid_transactions:
                        invalid_transactions.add(index)
                        buffer.append(transaction)
                
        
        # formulate the result
        result = []
        for transaction in buffer:

            result.append(",".join([
                transaction[0],
                str(transaction[1]),
                str(transaction[2]),
                transaction[3]
            ]))
        
        return result


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        solution = InvalidTransactions(transactions)
        return solution.solve()
        