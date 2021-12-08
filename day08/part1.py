

class Determiner():
    """
    1 = 2
    4 = 4
    7 = 3
    8 = 8
    """
    def addknown(self, entries):
        one = entries[1] ## will have two letters
        four = entries[4] ## will have four letters
        seven = entries[7] ## will have three letters
        eight = entries[8] ## will have eight letters
        
        self.position_one = set(seven)-set(one)
        self.position_three_six = set(one)
        self.position_two_four = set(four)-set(one)
    def determine(self, entry):
        # entry might be abcefg
        
        # 1,2,3,5, 6,9, 0
        if not(set(entry) - set(self.position_two_four)):
            return 1;
        # len 6 is 0 or 6 or 9
        if len(entry) == 6:
            if not self.position_two_four in entry:
                return 6
            if not self.position_one in entry:
                return 9
            return 0
        if len(entry) == 5:
            # 2 or 3 or 5
            if self.position_three_six in entry:
                return 3
            if set(entry) - set(self.position_two_four) == 3:
                return 5
            return 2
        
        # four and seven
        if len(entry) == 3:
            return 7
        return 4
        
        

ct = 0


import sys
for line in open(sys.argv[1],"r").readlines():
    inputs = line.split("|")[1].split()
    for i in inputs:
        if len(i) == 2 or len(i) == 4 or len(i) == 3 or len(i) == 7:
            ct += 1

print(ct)