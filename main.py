

def f1(x: int, y, z: float):
    return x + y + z

def f2(x: int, y: float, z: float):
    return x - y - z

def f3(x: int, y: int, z): # problem
    return x + y * z


def safe_call(ff, x, y, z):
    try:
        local_args = dict(locals())
        del local_args['ff']
        for i in local_args and ff.__annotations__: # go through all the args
            if type(local_args[i]) != ff.__annotations__[i]: # if the types not the same
                raise Exception("Problem")

        print(ff(x, y, z)) # run the function

    except:
        raise Exception("Problem")

    return 0

# Tests and examples:

safe_call(f1, 8, 1.0, 1.0)
safe_call(f2, 8, 1.0, 1.0)
safe_call(f3, 8, 1.0, 1.0)
