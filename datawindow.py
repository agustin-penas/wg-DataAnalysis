

class DataWindow:
    def __init__(self, windowSize):
        self.data = []
        self.windowSize = windowSize
        self.index = 0
        self.length = 0

    def push(self, entry):
        if len(self.data) < self.windowSize:
            self.data.append(entry)
            self.length = len(self.data)
            return self
        self.data[self.index] = entry
        self.index = (self.index + 1) % self.windowSize
        return self

    def get(self, ind):
        return self.data[self.getTrueIndex(ind)]

    def getTrueIndex(self, ind):
        if len(self.data) < self.windowSize:
            return ind
        else:
            return (ind + self.index) % self.windowSize


if __name__ == '__main__':
    window = DataWindow(3)
    window.push(1)
    print('-')
    print(window.get(0))
    window.push(2)
    print('-')
    print(window.get(0))
    print(window.get(1))
    window.push(3)
    print('-')
    print(window.get(0))
    print(window.get(1))
    print(window.get(2))
    window.push(4)
    print('-')
    print(window.get(0))
    print(window.get(1))
    print(window.get(2))
    window.push(5)
    print('-')
    print(window.get(0))
    print(window.get(1))
    print(window.get(2))
