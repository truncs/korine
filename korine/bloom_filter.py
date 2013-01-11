import math
import hashlib

try:
    from bitarray import bitarray
except ImportError:
    raise ImportError("requires bitarray")

try:
    import pyhash
except ImportError:
    raise ImportError("requires pyhash")


class BloomFilter(object):
    
    def __init__(self, capacity=100000, error_rate=0.001):
        """ BloomFilter is a probabilistic datastructure which are helpful in
        approximate membership queries. They only suffer from type 1 false
        positive errors and the error rate can be tuned to specific requirements.
        """
        self.total_size = 20000
        self.size = 2000
        self.k = 10
        self.bitarrays = []
        self.h1 = pyhash.fnv1a_64()
        self.h2 = pyhash.murmur2_x86_64b()
        for i in xrange(self.k):
            b = bitarray(self.size, endian='little')
            b.setall(False)
            self.bitarrays.append(b)

    def insert(self, element):
        unicode_element = unicode(element)
        element_hash1 = self.h1(unicode_element)
        element_hash2 = self.h2(unicode_element)
        for i in xrange(self.k):
            bit_no = (element_hash1 + i*element_hash2) % self.size
            self.bitarrays[i][bit_no] = True
        
        
    def check(self, element):
        unicode_element = unicode(element)
        element_hash1 = self.h1(unicode_element)
        element_hash2 = self.h2(unicode_element)
        
        return all([self.bitarrays[i][(element_hash1 + i*element_hash2) % self.size] for i in xrange(self.k)])
