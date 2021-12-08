

class Determiner():
    """
    1 = 2
    4 = 4
    7 = 3
    8 = 8
    """
    def __init__(self, entries):
        one = entries[1] ## will have two letters
        four = entries[4] ## will have four letters
        seven = entries[7] ## will have three letters
        eight = entries[8] ## will have eight letters
        
        self.position_one = set(seven)-set(one)
        print(f"position_one: {self.position_one}, {set(seven)}, {set(one)}")
        self.position_three_six = set(one)
        self.position_two_four = set(four)-set(one)
        self.four = set(four)
    def determine(self, entry):
        # entry might be abcefg
        #print(f"entry: {entry}, {len(entry)}")
        # 1,2,3,5, 6,9, 0
        if len(entry) == 2:
            return 1
        
        
        # len 6 is 0 or 6 or 9
        if len(entry) == 6:
            print(f"entry: {entry}, {len(entry)}")
            print(f"{self.position_one}")
            if self.four.issubset(entry):
                return 9
            if self.position_two_four.issubset(entry):
                return 6
            
            return 0
        if len(entry) == 5:
            # 2 or 3 or 5
            #print(f"entry: {entry}, {self.position_three_six}")
            if self.position_three_six.issubset(entry):
                return 3
            #print(f"entry: {entry}, {self.position_two_four}")
            if len(entry - set(self.position_two_four) )== 3:
                return 5
            return 2
        
        # four and seven
        if len(entry) == 3:
            return 7
        
        if len(entry)== 7:
            return 8
        
        if entry.isset(self.four):
            return 4
        
        raise Exception(f"entry: {entry}")
        
        

ct = 0


# import sys
# for line in open(sys.argv[1],"r").readlines():
#     inputs = line.split("|")[1].split()
#     for i in inputs:
#         if len(i) == 2 or len(i) == 4 or len(i) == 3 or len(i) == 7:
#             ct += 1

# print(ct)

from os import name
import pytest
def test_one():
    inputs = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    i  = inputs.split("|")[0].split()
    res = {}
    for x in i:
        res[len(x)] = x
    d = Determiner({1: res[2], 4: res[4], 7: res[3], 8 : res[7]})
    #d.determine(inputs.split("|")[1].split())
    print("x")
    numbers = ""
    for entry in inputs.split("|")[1].split():
        r = entry, d.determine(set(list(entry)))
        #print(r)
        numbers += str(r)
        
    
#if __name__ == "__main__":
    #test_one()
import sys
t= 0
for line in open(sys.argv[1],"r").readlines():
    #print(line)
    inputs = line.split("|")[1].split()
    values = line.split("|")[0].split()
    res = {}
    for x in values:
        res[len(x)] = x
    res = int("".join(map(lambda x: str(x), [x for x in map(lambda x: Determiner({1: res[2], 4: res[4], 7: res[3], 8 : res[7]}).determine(set(list(x))), inputs)])))
    print(res)
    t += res
print(t)
    