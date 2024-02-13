import ctypes

class TestCase():
    def __init__(self, shared_file) -> None:
        self.shared_file = shared_file 
        try:
            self.lib = ctypes.CDLL(self.shared_file)
            self.lib.top_k_frequent.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_int)), ctypes.POINTER(ctypes.c_int)]
            self.lib.top_k_frequent.restype = ctypes.c_int
        except Exception as e:
            print(e)
    
    def run(self):
        score = 0
        try:
            self.lib.top_k_frequent
        except Exception as err:
            err = str(err).split(':', 1)[-1].strip()
            return err, 0

        # Test Cases
        nums1 = [1, 1, 1, 2, 2, 3]
        k1 = 2
        output1 = (ctypes.POINTER(ctypes.c_int) * k1)()
        output_size1 = ctypes.c_int(0)
        self.lib.top_k_frequent((ctypes.c_int * len(nums1))(*nums1), len(nums1), k1, output1, ctypes.byref(output_size1))
        output1 = [output1[i].contents.value for i in range(output_size1.value)]
        if output1 == [1, 2]:
            score += 1

        nums2 = [1]
        k2 = 1
        output2 = (ctypes.POINTER(ctypes.c_int) * k2)()
        output_size2 = ctypes.c_int(0)
        self.lib.top_k_frequent((ctypes.c_int * len(nums2))(*nums2), len(nums2), k2, output2, ctypes.byref(output_size2))
        output2 = [output2[i].contents.value for i in range(output_size2.value)]
        if output2 == [1]:
            score += 1

        nums3 = [1, 2]
        k3 = 2
        output3 = (ctypes.POINTER(ctypes.c_int) * k3)()
        output_size3 = ctypes.c_int(0)
        self.lib.top_k_frequent((ctypes.c_int * len(nums3))(*nums3), len(nums3), k3, output3, ctypes.byref(output_size3))
        output3 = [output3[i].contents.value for i in range(output_size3.value)]
        if output3 == [1, 2]:
            score += 1

        return False, score
