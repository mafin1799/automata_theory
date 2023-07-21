import unittest
from course_project.api.math.BinaryCode import BinaryCode

def GetBits(number : int, bitness : int) -> str:
    bits = f'{number:0{bitness}b}' 
    return  bits[int(len(bits) - bitness):]

def InverseBits(bits : str) -> str:
    return ''.join('1' if bit == '0' else '0' for bit in bits)


def GetDirectCode(number : int, bitness : int) -> str:
    bitRange = (2 ** (bitness - 1)) - 1
    if(number < -bitRange or number > bitRange):
        return "ПЕРЕПОЛНЕНИЕ"
    bits = GetBits(abs(number), bitness - 1)
    if number >= 0:
        return "0" + bits
    else:
        return "1" + bits

def GetInverseCode(number : int, bitness : int) -> str:
    bitRange = (2 ** (bitness - 1)) - 1
    if(number < -bitRange or number > bitRange):
        return "ПЕРЕПОЛНЕНИЕ"
    bits = GetBits(abs(number), bitness - 1)
    print(bits)
    if number > 0:
        return "0" + bits
    else:
        return "1" + InverseBits(bits)

def GetComplementCode(number : int, bitness : int) -> str:
    bitRange = (2 ** (bitness - 1))
    if(number < -bitRange or number > bitRange - 1):
        return "ПЕРЕПОЛНЕНИЕ"
    bits = GetBits(abs(number), bitness - 1)
    if number >= 0:
        return "0" + bits
    else:
        bits = GetBits(abs(number) - 1, bitness - 1)
        return "1" + InverseBits(bits) 

class TestBinaryCode(unittest.TestCase):
    __MAX_BITNESS = 8

    def setUp(self):
        pass

    def test_init(self):
        t = BinaryCode(0, 1)
        self.assertRaises(ValueError, BinaryCode.__init__, t, 1, -1)
        self.assertRaises(ValueError, BinaryCode.__init__, t, 1, 0)
        self.assertRaises(ValueError, BinaryCode.__init__, t, 34, -1)
        self.assertRaises(ValueError, BinaryCode.__init__, t, -12, 0)
        self.assertRaises(ValueError, BinaryCode.__init__, t, -34, -1)
        self.assertRaises(ValueError, BinaryCode.__init__, t, 12, 0)

        self.assertEqual(BinaryCode(1).number, 1)
        self.assertEqual(BinaryCode(-5).number, -5)

        self.assertEqual(BinaryCode(-5).bitness, 8)
        self.assertEqual(BinaryCode(1, 5).bitness, 5)
        self.assertEqual(BinaryCode(-5, 10).bitness, 10)

    def test_add(self):
        self.assertEqual((BinaryCode(10) + BinaryCode(10)).number, 20)
        self.assertEqual((BinaryCode(10) + BinaryCode(20)).number, 30)
        self.assertEqual((BinaryCode(-30) + BinaryCode(20)).number, -10)
        self.assertEqual((BinaryCode(-30) + BinaryCode(-20)).number, -50)

        self.assertEqual((BinaryCode(-30) + BinaryCode(-20)).bitness, 8)
        self.assertEqual((BinaryCode(-30, 10) + BinaryCode(-20)).bitness, 10)
        self.assertEqual((BinaryCode(-30, 2) + BinaryCode(-20)).bitness, 2)

        self.assertNotEqual((BinaryCode(-30, 2) + BinaryCode(-20, 4)).bitness, 4)
        self.assertNotEqual((BinaryCode(-30, 2) + BinaryCode(-20, 7)).bitness, 7)

    def test_lshift(self):
        self.assertEqual((BinaryCode(10) << 1).number, 10 << 1)
        self.assertEqual((BinaryCode(10) << 5).number, 10 << 5)

        self.assertEqual((BinaryCode(-10) << 1).number, -10 << 1)
        self.assertEqual((BinaryCode(-10) << 5).number, -10 << 5)

        self.assertEqual((BinaryCode(-10) << 1).bitness, 8)
        self.assertEqual((BinaryCode(4) << 5).bitness, 8)

        self.assertEqual((BinaryCode(-10, 11) << 1).bitness, 11)
        self.assertEqual((BinaryCode(4, 33) << 5).bitness, 33)   

    def test_rshift(self):
        self.assertEqual((BinaryCode(10) >> 1).number, 10 >> 1)
        self.assertEqual((BinaryCode(10) >> 5).number, 10 >> 5)

        self.assertEqual((BinaryCode(-10) >> 1).number, -10 >> 1)
        self.assertEqual((BinaryCode(-10) >> 5).number, -10 >> 5)

        self.assertEqual((BinaryCode(-10) >> 1).bitness, 8)
        self.assertEqual((BinaryCode(4) >> 5).bitness, 8)

        self.assertEqual((BinaryCode(-10, 11) >> 1).bitness, 11)
        self.assertEqual((BinaryCode(4, 33) >> 5).bitness, 33)       

    def test_get_direct_code(self):

        self.assertEqual(BinaryCode(1).get_direct_code(), "00000001")   
        self.assertEqual(BinaryCode(2).get_direct_code(), "00000010")
        self.assertEqual(BinaryCode(65).get_direct_code(), "01000001") 
        self.assertEqual(BinaryCode(0).get_direct_code(), "00000000") 

        self.assertEqual(BinaryCode(-33).get_direct_code(), "10100001")
        self.assertEqual(BinaryCode(-65).get_direct_code(), "11000001") 
        self.assertEqual(BinaryCode(-0).get_direct_code(), "00000000")  


        self.assertEqual(BinaryCode(1, 7).get_direct_code(), "0000001")     
        self.assertEqual(BinaryCode(2, 7).get_direct_code(), "0000010")  
        self.assertEqual(BinaryCode(65, 7).get_direct_code(), "ПЕРЕПОЛНЕНИЕ") 
        self.assertEqual(BinaryCode(0, 7).get_direct_code(), "0000000") 

        self.assertEqual(BinaryCode(-33, 7).get_direct_code(), "1100001") 
        self.assertEqual(BinaryCode(-65, 7).get_direct_code(), "ПЕРЕПОЛНЕНИЕ") 
        self.assertEqual(BinaryCode(-0, 7).get_direct_code(), "0000000")  

    def test_get_inverse_code(self):
        self.assertEqual(BinaryCode(1).get_inverse_code(), "00000001")     
        self.assertEqual(BinaryCode(2).get_inverse_code(), "00000010")  
        self.assertEqual(BinaryCode(65).get_inverse_code(), "01000001")  
        self.assertEqual(BinaryCode(0).get_inverse_code(), "00000000") 

        self.assertEqual(BinaryCode(-33).get_inverse_code(), "11011110") 
        self.assertEqual(BinaryCode(-65).get_inverse_code(), "10111110")  
        self.assertEqual(BinaryCode(-0).get_inverse_code(), "00000000") 


        self.assertEqual(BinaryCode(1, 7).get_inverse_code(), "0000001")    
        self.assertEqual(BinaryCode(2, 7).get_inverse_code(), "0000010")  
        self.assertEqual(BinaryCode(65, 7).get_inverse_code(), "ПЕРЕПОЛНЕНИЕ") 
        self.assertEqual(BinaryCode(0, 7).get_inverse_code(), "0000000")  

        self.assertEqual(BinaryCode(-33, 7).get_inverse_code(), "1011110") 
        self.assertEqual(BinaryCode(-65, 7).get_inverse_code(), "ПЕРЕПОЛНЕНИЕ")  
        self.assertEqual(BinaryCode(-0, 7).get_inverse_code(), "0000000")

    def test_get_complement_code(self):
        self.assertEqual(BinaryCode(1).get_complement_code(), "00000001")     
        self.assertEqual(BinaryCode(2).get_complement_code(), "00000010")  
        self.assertEqual(BinaryCode(65).get_complement_code(), "01000001")  
        self.assertEqual(BinaryCode(0).get_complement_code(), "00000000") 

        self.assertEqual(BinaryCode(-33).get_complement_code(), "11011111") 
        self.assertEqual(BinaryCode(-65).get_complement_code(), "10111111")  
        self.assertEqual(BinaryCode(-0).get_complement_code(), "00000000") 


        self.assertEqual(BinaryCode(1, 7).get_complement_code(), "0000001")    
        self.assertEqual(BinaryCode(2, 7).get_complement_code(), "0000010")  
        self.assertEqual(BinaryCode(65, 7).get_complement_code(), "ПЕРЕПОЛНЕНИЕ") 
        self.assertEqual(BinaryCode(0, 7).get_complement_code(), "0000000")  

        self.assertEqual(BinaryCode(-33, 7).get_complement_code(), "1011111") 
        self.assertEqual(BinaryCode(-65, 7).get_complement_code(), "ПЕРЕПОЛНЕНИЕ")  
        self.assertEqual(BinaryCode(-0, 7).get_complement_code(), "0000000")

    def test_like_quartus_directCode(self):
        r = 2 ** self.__MAX_BITNESS
        for i in range(-r, r):
            self.assertEqual(BinaryCode(i, self.__MAX_BITNESS).get_direct_code(), GetDirectCode(i,self.__MAX_BITNESS),
                            f'Number is {str(i)}, bitness is {self.__MAX_BITNESS}  range:[{-r / 2 + 1}, {r / 2 - 1}]')

    def test_like_quartus_inverseCode(self):
        r = 2 ** self.__MAX_BITNESS
        for i in range(-r, r):
            self.assertEqual(BinaryCode(i, self.__MAX_BITNESS).get_inverse_code(), GetInverseCode(i, self.__MAX_BITNESS),
                            f'Number is {str(i)}, bitness is {self.__MAX_BITNESS}  range:[{-r / 2 + 1}, {r / 2 - 1}]')

    
    def test_like_quartus_ComplementCode(self):
        r = 2 ** self.__MAX_BITNESS
        for i in range(-r, r):
            self.assertEqual(BinaryCode(i, self.__MAX_BITNESS).get_complement_code(), GetComplementCode(i, self.__MAX_BITNESS), 
                            f'Number is {str(i)}, bitness is {self.__MAX_BITNESS}  range:[{-r / 2}, {r / 2 - 1}]')

if __name__ == "__main__":
    unittest.main()
