class NumberList:
    def __init__(self, numbers):
        self.numbers = numbers

    def __iter__(self):
        return NumberIterator(self.numbers)


class NumberIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __next__(self):
        if self.index >= len(self.numbers):
            return "Error: last iterator already been."
            raise StopIteration
        number = self.numbers[self.index]
        self.index += 1
        return number
    
numbers = NumberList([1, 2, 3, 4, 5])
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) 