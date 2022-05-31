class Counter:
    def __init__(self, val):
        self.__val = val

    def increment(self):
        self.__val += 1

    def get_value(self):
        return self.__val

def main():
    c1 = Counter(2)
    c2 = Counter(0)
    c1.increment()
    c2.increment()
    c1.increment()
    c1.increment()
    print(c1.get_value())
    print(c2.get_value())

main()


