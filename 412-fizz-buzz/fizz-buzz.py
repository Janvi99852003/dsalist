

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        t = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                t.append("FizzBuzz")
            elif i % 3 == 0:
                t.append("Fizz")
            elif i % 5 == 0:
                t.append("Buzz")
            else:
                t.append(str(i))
        return t
