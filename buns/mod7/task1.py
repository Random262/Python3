def validate_args(*args):
    def wrapped_func():
        if len(args) < 1:
            return "Not enough arguments"
        elif len(args) > 1:
            return "Too many arguments"
        elif not isinstance(*args, int) or isinstance(*args, bool):
            return "Wrong types"
        elif args[0] < 0:
            return "Negative argument"
        return args[0]
    return wrapped_func()


print(validate_args(5))
print(validate_args(-1))
print(validate_args(0))
print(validate_args('qw'))
print(validate_args(True))
print(validate_args([5]))
print(validate_args(5, -1))
print(validate_args(-1, 5))
print(validate_args(5, 5))
print(validate_args(5, 'hfh'))
