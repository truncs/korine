import math
import hashlib

try:
    import bitarray
except ImportError:
    raise ImportError("requires bitarray")

try:
    import pyhash
except ImportError:
    raise ImportError("requires pyhash")


class BloomFilter(object):
    
    def __init__(self, capacity, error_rate=0.001):
        """ BloomFilter is a probabilistic datastructure which are helpful in
        approximate membership queries. They only suffer from type 1 false
        positive errors and the error rate can be tuned to specific requirements.
        """
        
        
