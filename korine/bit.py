class BIT(object):
    """ Binary Index Tree is a datastructure that store
    cumulative information of the tree giving time complexity of
    O(logn) for doing cumulative operation accross a given range in
    an array.
    """
    
    def __init__(self, array=[]):
        """
        """
        self.array = [0]
        for elem in array:
            self.append(elem)

    def append(self, value):
        """
        
        Arguments:
        - `self`:
        - `value`:
        """

        self.array.append(value)
        start = len(self.array) - 1
        end = start - (-start & start) 
        cur = start - 1

        while cur > end:
            self.array[start] += self.array[cur]
            cur = cur - (cur & -cur)

        
    def update(self, index, value):
        """
        
        Arguments:
        - `self`:
        - `index`:
        - `value`:
        """
        
        pass


    def get_sum(self, index):
        """
        Get the cumulative operation applied
        from 0 to index.
        
        Arguments:
        - `self`:
        - `Index`:n
        """


        if index > len(self.array):
            raise IndexError

        index = index + 1
        cumulative = 0
        while index > 0:

            cumulative += self.array[index]
            index -= (index & -index)

        return cumulative
    
    def get(self, index):
        """
        Gets the actual value at the
        index
        """
        if index > len(self.array):
            raise IndexError

        index = index + 1
        end = index - (index & -index) + 1

        cur = index - 1
        value = self.array[index]

        while cur >= end:
            value -= self.array[cur]
            cur -= (cur & -cur)

        return value
