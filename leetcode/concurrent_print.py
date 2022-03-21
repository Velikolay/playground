from typing import List, Callable, Any
import threading


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i = 1
        self.cond = threading.Condition()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        with self.cond:
            while self.i <= self.n:
                if self.i % 3 == 0 and self.i % 5 != 0:
                    printFizz()
                    self.i += 1
                    self.cond.notify_all()
                else:
                    self.cond.wait()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        with self.cond:
            while self.i <= self.n:
                if self.i % 3 != 0 and self.i % 5 == 0:
                    printBuzz()
                    self.i += 1
                    self.cond.notify_all()
                else:
                    self.cond.wait()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        with self.cond:
            while self.i <= self.n:
                if self.i % 3 == 0 and self.i % 5 == 0:
                    printFizzBuzz()
                    self.i += 1
                    self.cond.notify_all()
                else:
                    self.cond.wait()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        with self.cond:
            while self.i <= self.n:
                if self.i % 3 != 0 and self.i % 5 != 0:
                    printNumber(self.i)
                    self.i += 1
                    self.cond.notify_all()
                else:
                    self.cond.wait()


class ThreadA(threading.Thread):
    def __init__(self, fizzbuzz: FizzBuzz, output: List[Any]):
        threading.Thread.__init__(self)
        self.fizzbuzz = fizzbuzz
        self.output = output

    def print(self):
        print("fizz")
        self.output.append("fizz")

    def run(self):
        self.fizzbuzz.fizz(self.print)


class ThreadB(threading.Thread):
    def __init__(self, fizzbuzz: FizzBuzz, output: List[Any]):
        threading.Thread.__init__(self)
        self.fizzbuzz = fizzbuzz
        self.output = output

    def print(self):
        print("buzz")
        self.output.append("buzz")

    def run(self):
        self.fizzbuzz.buzz(self.print)


class ThreadC(threading.Thread):
    def __init__(self, fizzbuzz: FizzBuzz, output: List[Any]):
        threading.Thread.__init__(self)
        self.fizzbuzz = fizzbuzz
        self.output = output

    def print(self):
        print("fizzbuzz")
        self.output.append("fizzbuzz")

    def run(self):
        self.fizzbuzz.fizzbuzz(self.print)


class ThreadD(threading.Thread):
    def __init__(self, fizzbuzz: FizzBuzz, output: List[Any]):
        threading.Thread.__init__(self)
        self.fizzbuzz = fizzbuzz
        self.output = output

    def print(self, i: int):
        print(i)
        self.output.append(i)

    def run(self):
        self.fizzbuzz.number(self.print)


if __name__ == '__main__':
    output = []
    fizzbuzz = FizzBuzz(15)
    ta = ThreadA(fizzbuzz, output)
    tb = ThreadB(fizzbuzz, output)
    tc = ThreadC(fizzbuzz, output)
    td = ThreadD(fizzbuzz, output)

    ta.start()
    tb.start()
    tc.start()
    td.start()

    ta.join()
    tb.join()
    tc.join()
    td.join()

    print(output)
