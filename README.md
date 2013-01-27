Korine
=========

Interesting data structures in python. 


Dependencies 
---------------- 

Testify - testing framework by Yelp
bitarray - fast bitarrays in python
pyhash - fast hashing algorithms(murmur, fnv) for python 

``` bash
   cd korine/
   pip install -r requirements.txt
```

Data Structures 
-----------------

 * Binary Indexed Tree with sum operation. 

    * Cumulative sum at any index - O(logn)
    * Updating any value in the original array -  O(logn)
    * Actual value in the original array - O(logn)
    
 * Bloom Filters
    
    * Uses murmur and fnv along with double hashing to generate k hash functions
    * Paritions the overall space into k different space, corresponding to each hash function


Coming Soon
----------------

 * Skip List 
 * Hyperloglog
 * Quotient Filters
 * Treaps
