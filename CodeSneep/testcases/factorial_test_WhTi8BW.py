import ctypes

class TestCase():
    def __init__(self,shared_file) -> None:
        self.shared_file = shared_file 
        try:
            self.lib = ctypes.CDLL(self.shared_file)
            self.lib.factorial.argtypes = [ctypes.c_longlong]
            self.lib.factorial.restype = ctypes.c_longlong
        except Exception as e:
            print(e)
    def run(self):
        score = 0
        try:
            self.lib.factorial
        except Exception as err:
            err = str(err).split(':', 1)[-1].strip()
            return err,0

        if self.lib.factorial(5) == 120:
            score+=1
        if self.lib.factorial(2) == 2:
            score+=1
        if self.lib.factorial(0) == 1:
            score+=1
        if self.lib.factorial(6) == 720:
            score+=1
        if self.lib.factorial(15) == 1307674368000:
            score+=1
        return False,score
