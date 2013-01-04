import testify as T
from korine.bit import BIT

class TestBit(T.TestCase):

    @T.setup
    def setup_bit(self):
        self.array = [1, 0, 2, 1, 1, 3, 0, 4, 2, 5, 2, 2, 3, 1, 0, 2]
        self.expected_bit = [0, 1, 1, 2, 4, 1, 4, 0, 12, 2, 7, 2, 11, 3, 4, 0, 29]
        self.bit = BIT(self.array)


    def test_initialization(self):

        assert len(self.bit.array) == len(self.array) + 1

        for i in xrange(1, len(self.expected_bit)):
            T.assert_equal(self.bit.array[i], self.expected_bit[i])

    def test_cumulative_sum(self):
        expected_sum = [1, 1, 3, 4, 5, 8, 8, 12, 14, 19, 21, 23, 26, 27, 27, 29]

        for i, val in enumerate(expected_sum):
            T.assert_equal(val, self.bit.get_sum(i))

if __name__ == '__main__':
    T.run()
