import unittest

class BIT(object):
    """ Binary indexed trees in python.    
    """
    
    def __init__(self, array):
        if len(array) < 1:
            raise RuntimeError
        self.bit = [sum(array[k - (k & -k):k]) for k in xrange(0, len(array) + 1)]


    def read_frequency(self, idx):
        """ Read the cumulative sum upto index idx
        """
        bit_idx = idx + 1
        sum = 0
        while (bit_idx > 0):
            sum += self.bit[bit_idx]
            bit_idx -= (bit_idx & -bit_idx)

        return sum


    def actual_frequency(self, idx):
        """ Read the actual frequency of at the index idx
        """

        bit_idx = idx + 1
        sum = self.bit[bit_idx]

        if (bit_idx > 0):
            z = bit_idx - (bit_idx & -bit_idx)
            bit_idx -= 1
            
            while(bit_idx != z) :
                sum -= self.bit[bit_idx]
                bit_idx -= bit_idx & -bit_idx

        return sum

    def update_frequency(self, idx, value):
        """ Update the frequency at the index idx by value
        """

        bit_idx = idx + 1
        max_value += len(self.bit) - 1

        while(bit_idx <= max_value):
            tree[bit_idx] += value
            bit_idx += bit_idx & (-bit_idx)
        