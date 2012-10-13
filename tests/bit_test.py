import testify as T
#from korine import bit

class TestBit(T.TestCase):

    @T.setup
    def setup_bit(self):
        self.array = [1, 2, -1, 0, 3]
        self.bit = BIT(self.array)


    def test_initialization(self):

        expected_init = [0, 1, 3, -1, 2, 3]
        
        for i in xrange(0, 5):
            assert self.bit.bit[i + 1] == expected_init[i]


    def test_cumulative_frequency(self):
        expected_frequency = [1, 3, 2, 2, 5]
        for i in xrange(0, 5):
            assert self.bit.read_frequency(0) == self.expected_frequency


   # def test_update_frequency(self):
        


if __name__ == '__main__':
    T.run()