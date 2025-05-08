"""
Session 4 - Day Challenge: MemoryMatrix and Buffer Protocol Exercises

Implement the TODOs to complete the tasks.

DO NOT change the method signatures or function names.
"""

import array


# ---------------- MemoryMatrix Class ----------------
# A 2D matrix implemented using a flat buffer (array.array)
# Supports row/column views via memoryview without copying data
class MemoryMatrix:
    def __init__(self, rows, cols, typecode='d', fill=0):
        """
        Initialize a 2D matrix with given dimensions and default value.

        Args:
            rows (int): Number of rows
            cols (int): Number of columns
            typecode (str): Type of elements ('d' = float, 'i' = int, etc.)
            fill (numeric): Initial value for all elements
        """
        self.rows = rows
        self.cols = cols
        self.typecode = typecode
        # Internal flat buffer storing all elements in row-major order
        self._buf = array.array(typecode, [fill] * (rows * cols))

    def __getitem__(self, key):
        """
        Access element like m[i, j]
        TODO: Implement indexing logic
        """
        print("TODO: __getitem__ not implemented")
        return None

    def __setitem__(self, key, value):
        """
        Set element like m[i, j] = value
        TODO: Implement assignment logic
        """
        print("TODO: __setitem__ not implemented")

    def row_view(self, r):
        """
        Return a memoryview of the r-th row
        TODO: Implement without copying data
        """
        print("TODO: row_view not implemented")
        return memoryview(self._buf)[0:0]

    def col_view(self, c):
        """
        Return a memoryview of the c-th column
        TODO: Implement without copying data
        """
        print("TODO: col_view not implemented")
        return memoryview(self._buf)[0:0]

    def tolist(self):
        """
        Convert matrix to a list of lists
        [[row0], [row1], ...]
        TODO: Implement
        """
        print("TODO: tolist not implemented")
        return []

    def __iter__(self):
        """
        Iterate over all elements in row-major order
        TODO: Implement
        """
        print("TODO: __iter__ not implemented")
        return iter([])

    def __repr__(self):
        return f"MemoryMatrix({self.rows}x{self.cols})"


# ---------------- Utility Functions ----------------
def sum_even_bytes(buf):
    """
    Sum every even byte (index 0, 2, 4...) from a buffer-supporting object
    TODO: Implement using the buffer protocol (no .tobytes())
    """
    print("TODO: sum_even_bytes not implemented")
    return 0


def negate_ints_inplace(arr):
    """
    Negate each integer in-place in a mutable buffer-supporting object
    Assumes signed integers (e.g., 'i' or 'l')
    TODO: Implement using memoryview
    """
    print("TODO: negate_ints_inplace not implemented")


def alias_detect(view_a, view_b):
    """
    Detect if two memoryviews share the same underlying memory
    TODO: Implement
    """
    print("TODO: alias_detect not implemented")
    return False


# ---------------- Demo Tests --------------------------
if __name__ == "__main__":
    # Test sum_even_bytes
    data = bytes(range(10))  # b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t'
    print("Sum even bytes (stub):", sum_even_bytes(data))

    # Test negate_ints_inplace
    ints = array.array('i', [1, -2, 3])
    negate_ints_inplace(ints)
    print("After negate stub    :", list(ints))

    # Test alias detection
    buf = bytearray(b"hello")
    v1 = memoryview(buf)
    v2 = v1[1:]
    print("Alias detect (stub)  :", alias_detect(v1, v2))

    # Test MemoryMatrix
    m = MemoryMatrix(3, 4)
    print("Matrix stub repr     :", m)
    print("Matrix tolist stub   :", m.tolist())

    # Optional: More tests here after implementing