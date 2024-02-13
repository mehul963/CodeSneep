import ctypes

class TestCase():
    def __init__(self, shared_file) -> None:
        self.shared_file = shared_file 
        try:
            self.lib = ctypes.CDLL(self.shared_file)
            self.lib.two_sum.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
            self.lib.two_sum.restype = ctypes.c_int
        except Exception as e:
            print(e)

    def run(self):
        score = 0
        try:
            self.lib.two_sum
        except Exception as err:
            err = str(err).split(':', 1)[-1].strip()
            return err, 0

        # Test Cases
        nums = [2, 7, 11, 15]
        target = 9
        output = (ctypes.c_int * 2)()
        self.lib.two_sum((ctypes.c_int * len(nums))(*nums), len(nums), target, output)
        if list(output) == [0, 1]:
            score += 1

        nums = [3, 2, 4]
        target = 6
        output = (ctypes.c_int * 2)()
        self.lib.two_sum((ctypes.c_int * len(nums))(*nums), len(nums), target, output)
        if list(output) == [1, 2]:
            score += 1

        nums = [3, 3]
        target = 6
        output = (ctypes.c_int * 2)()
        self.lib.two_sum((ctypes.c_int * len(nums))(*nums), len(nums), target, output)
        if list(output) == [0, 1]:
            score += 1

        nums = [5, 25, 75]
        target = 100
        output = (ctypes.c_int * 2)()
        self.lib.two_sum((ctypes.c_int * len(nums))(*nums), len(nums), target, output)
        if list(output) == [1, 2]:
            score += 1

        nums = [0, 4, 3, 0]
        target = 0
        output = (ctypes.c_int * 2)()
        self.lib.two_sum((ctypes.c_int * len(nums))(*nums), len(nums), target, output)
        if list(output) == [0, 3]:
            score += 1

        return False, score
