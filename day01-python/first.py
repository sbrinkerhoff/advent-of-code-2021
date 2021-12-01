

def read_inputs(f="input.txt"):
    inputs = open(f, 'r').readlines()
    inputs = [int(x.strip()) for x in inputs]
    return inputs

def calculate_increases(inputs):
    depth = inputs[0]
    increases = 0
    
    for i in inputs:
        if i > depth:
            increases += 1
        depth = i
    
    return increases

def main():
    # Read in the input file to a list
    inputs = read_inputs()
    increases = calculate_increases(inputs)
    
    print(increases)

if __name__ == "__main__":
    main()
    
def test_calculate_increases_increasing_linear():
    items = [1,2,3,4,5]
    assert calculate_increases(items) == 4

def test_calculate_increases_reset_in_middle():
    items = [1,2,3,4,5,0,1,2,3,4,5]
    assert calculate_increases(items) == 9
    
def test_calculate_increases_up_and_down():
    items = [0,1,2,1,2]
    assert calculate_increases(items) == 3
    