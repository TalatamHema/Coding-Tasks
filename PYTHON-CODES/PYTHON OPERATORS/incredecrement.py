class Counter:
    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1
        return self.value

    def decrement(self):
        self.value -= 1
        return self.value

# Example usage:
counter = Counter(5)
print(counter.increment()) 
print(counter.decrement())  