def is_locked(failed, max_tries=3):
    """return True if faild attempts reach or exceed the maximum"""
    return failed >= max_tries
def tries_left(failed, max_tries=3):
    """return the number of attempts remainng, or 0 if locked"""
    if is_locked(failed, max_tries):
        return 0
    return max_tries - failed
def status(failed):
    """return whether the account is locked or how many tries remain"""
    if is_locked(failed):
        return "locked"
    return f"active ({tries_left(failed)} tries left)"
print(is_locked(2))
print(is_locked(3))
print(is_locked(3, 5))
print(tries_left(1))
print(tries_left(7))
print(status(1))
print(status(4))
