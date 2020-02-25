'''
Module only used for illustrating the intended class behaviour in the exercise section
'''


class Count_to_10():

    def __init__(self, start=0, step=1):
        self.num = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.num += self.step
        if self.num > 10:
            print('I can only count to 10! :(')
            raise(StopIteration)
        return self.num

    def set_step(self, step):
        self.step = step


class Accumulator():

    def __init__(self, start=0):
        self._sum = start

    def __call__(self, x):
        self._sum += x
        print(f"I've now added {x} to my sum")

    @property
    def current_sum(self):
        return self._sum
