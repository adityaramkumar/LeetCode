// Runtime: 0 ms, faster than 100.00% of C online submissions for Number of 1 Bits.
// Memory Usage: 6.7 MB, less than 22.86% of C online submissions for Number of 1 Bits.

int hammingWeight(uint32_t n) {
    int count = 0;
    while (n != 0)  {
        if (n & 1U) count++;
        n >>= 1;
    }
    return count;
}
