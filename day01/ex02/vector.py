class Vector:
    def __init__(self, values):
        self.values = values
        self.length = len(values)

    def __add__(self, i):
        if not isinstance(i, Vector):
            return Vector([v + i for v in self.values])
        else:
            return Vector([z[0] + z[1] for z in zip(self.values, i.values)])
        
    def __radd__(self, i):
        return self.__add__(i)

    def __mul__(self, i):
        if not isinstance(i, Vector):
            return Vector([v * i for v in self.values])
        else:
            return Vector([z[0] * z[1] for z in zip(self.values, i.values)])

    def __rmul__(self, i):
        return self.__mul__(v)

    def __truediv__(self, i):
        if not isinstance(i, Vector):
            return Vector([v / i for v in self.values])
        else:
            return Vector([z[0] / z[1] for z in zip(self.values, i.values)])
    
    def __rtuediv__(self, i):
        return self.__truediv__(i)
    
    def __sub__(self, i):
        if not isinstance(i, Vector):
            return Vector([v - i for v in self.velues])
        else:
            return Vector([z[0] - z[1] for z in zip(self.values, i.values)])
    def __rsub__(self, i):
        return self.__sub__(i)
    
    def __str__(self):
        return str(self.values)
    
    def __repr__(self):
        return 'array({})'.format(str(self.values))

    