class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError(f"cant fit {self._size} cookies inside a {self._capacity} cookie jar")
        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("there are no cookies to withdraw")
        self._size -= n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

 
def main():
    jar = Jar()
    print(jar.capacity)
    jar.deposit(2)
    print(jar)
    jar.deposit(4)
    print(jar)
    jar.withdraw(5)
    print(jar)

    jar2 = Jar(10)
    print(jar2.capacity)



if __name__ == "__main__":
    main()