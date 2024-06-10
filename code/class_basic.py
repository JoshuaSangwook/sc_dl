import numpy as np

class Variable:
    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data    


input = np.array([1, 2, 3])
data = Variable(input)
print("data:", data.get_data())

new_input = np.array([4, 5, 6])
data.set_data(new_input)
print("new_data:", data.get_data())
