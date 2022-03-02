

def print_sorted(x):
    if type(x) == dict:
        sorted_data = [i for i in x]
        sorted_data = sorted(sorted_data, key=lambda kv: str(kv)) # sort and make string

        for j in sorted_data:
            if type(x[j]) == tuple or type(x[j]) == list or type(x[j]) == set or type(x[j]) == dict: # go deeper
                print(j, ":")
                print_sorted(x[j])
            else:
                print(j, ":", x[j])


    if type(x) == tuple or type(x) == list or type(x) == set:
        sorted_data = sorted(x, key=lambda x: str(x)) # sort and make string
        print("[")
        for j in sorted_data:
            if type(j) == tuple or type(j) == list or type(j) == set or type(j) == dict: # go deeper
                print_sorted(j)
            else:
                print(j, " ")
        print("]")

# Tests and examples:

x1 = {"a": 5, "c": 6, "b": [1, 3, 2, 4]}
x2 = [(10, 'c'), (40, 'b'), (20, 'a')]
x3 = {"a": 5, "c": 6, "b": [1, 3, 2, [5, 7, 1]]}
print_sorted(x1)
print_sorted(x2)
print_sorted(x3)
