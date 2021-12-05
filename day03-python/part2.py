
def most_frequent_in_position(s, pos):    
    count_of_one = sum([1 for x in s if x[pos] == '1'])
    count_of_zero = sum([1 for x in s if x[pos] == '0'])
    return 1 if count_of_one >= count_of_zero else 0
    
def least_frequemt_in_position(s, pos):
    return 0 if most_frequent_in_position(s, pos) else 1
    
def filter_list_by_position(l, position, method):
    most_frequent = method(l, position)
    results = []
    for item in l:
        print(f"{item} {item[position]} {most_frequent}")
        if int(item[position]) == int(most_frequent):
            results.append(item)
    return results

def main():
    
    # presumably a list copy would be ideal here
    oxy = [x.strip() for x in open("../inputs/day03.txt", "r").readlines()]
    co2 = [x.strip() for x in open("../inputs/day03.txt", "r").readlines()]

    for x in range(len(oxy[0])):
        if len(oxy)>1:
            oxy = filter_list_by_position(oxy, x, most_frequent_in_position)

    for x in range(len(co2[0])):
        if len(co2)>1:
            co2 = filter_list_by_position(co2, x, least_frequemt_in_position)
            
    print(oxy, co2)
    print(int(oxy[0],2), int(co2[0],2))
    print(int(oxy[0],2)*int(co2[0],2))

def test_most_frequent_in_position():
    x = ['1101', '1101', '0000', '1001']
    assert most_frequent_in_position(x, 0) == 1
    assert most_frequent_in_position(x, 1) == 1
    assert most_frequent_in_position(x, 2) == 0
    
if __name__ == "__main__":
    main()