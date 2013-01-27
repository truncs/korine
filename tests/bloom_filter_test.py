import testify as T
from korine.bloom_filter import BloomFilter 


class BloomFilterTest(T.TestCase):
    
    @T.setup
    def setup_bloom_filter(self):
        self.b = BloomFilter()


    def test_insert_check(self):
        self.b.insert('aditya')
        assert self.b.check('aditya')


    def test_check_false(self):
        assert not self.b.check('adity')
