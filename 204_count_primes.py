'''
204. Count Primes
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''


class Solution(object):
    '''
    Sieve of Eratosthenes 
        alg for finding all prime numbers up to a given limit
        marks the multiples of each prime starting w first number 
    '''

    def countPrimes(self, n):
        if n < 3:
            return 0
        # no prime less than 3
        primes = [1] * n
        # create a list for making numbers less than n
        primes[0] = primes[1] = 0
        # 0 and 1 are not prime numbers
        m = 2
        while m*m < n:
            # only check a number(m) if its square is less than n
            if primes[m] == 1:
                # if m is already marked by 0, no need to check its multiples
                # if m is marked by 1, we mark all its multiples from m*m to n by 0
                # 1 + (n-m * m-1)//m is equal to the number of multiples of m from m*m to n
                primes[m*m:n:m] = [0] * (1+(n-m*m-1)//m)

                # if it is the first iteration, add 1 to m
                # which means m will be 3 in next iteration
                # otherwise m = m+2 (avoid checking even numbers again)
            m += 1 if m == 2 else 2
        return sum(primes)

        # alternative soln
        # if n <= 2:
        #     return 0
        # res = [True] * n
        # res[0] = res[1] = False
        # for i in range(2, n):
        #     if res[i] == True:
        #         for j in range(2, (n-1)//i+1):
        #             res[i*j] = False
        # return sum(res)


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.countPrimes(10))
