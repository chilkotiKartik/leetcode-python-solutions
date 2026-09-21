"""
Space-Efficient Probabilistic Bloom Filter with Double Hashing.
Time Complexity: O(k) for insertion and query
Space Complexity: O(m) bit array
"""
import math
import hashlib

class BloomFilter:
    def __init__(self, expected_elements: int, false_positive_rate: float = 0.01):
        self.n = expected_elements
        self.p = false_positive_rate
        # Optimal bit array size m = - (n * ln(p)) / (ln(2)^2)
        self.size = int(- (self.n * math.log(self.p)) / (math.log(2) ** 2))
        # Optimal number of hash functions k = (m / n) * ln(2)
        self.hash_count = int((self.size / self.n) * math.log(2))
        self.bit_array = [0] * self.size

    def _hashes(self, item: str):
        # Double hashing technique using MD5 and SHA256
        h1 = int(hashlib.md5(item.encode('utf-8')).hexdigest(), 16)
        h2 = int(hashlib.sha256(item.encode('utf-8')).hexdigest(), 16)
        for i in range(self.hash_count):
            yield (h1 + i * h2) % self.size

    def add(self, item: str):
        for bit_idx in self._hashes(item):
            self.bit_array[bit_idx] = 1

    def contains(self, item: str) -> bool:
        for bit_idx in self._hashes(item):
            if self.bit_array[bit_idx] == 0:
                return False
        return True

if __name__ == "__main__":
    bf = BloomFilter(1000, 0.01)
    bf.add("keploy-agent")
    bf.add("test-session-42")
    assert bf.contains("keploy-agent") == True
    assert bf.contains("test-session-42") == True
    assert bf.contains("non-existent-key") == False
    print("Bloom Filter operations validated successfully!")
