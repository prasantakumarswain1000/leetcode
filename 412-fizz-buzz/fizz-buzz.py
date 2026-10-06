class Solution:
    def fizzBuzz(self, n):
        noko = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                noko.append("FizzBuzz")
            elif i % 3 == 0:
                noko.append("Fizz")
            elif i % 5 == 0:
                noko.append("Buzz")
            else:
                noko.append(str(i))
        return noko