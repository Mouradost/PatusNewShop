from datetime import datetime


def time_it(f):
    def time_it_wrapper(*args, **kwargs):
        start = datetime.now()
        results = f(*args, **kwargs)
        print(f"Took {datetime.now() - start}")
        return results

    return time_it_wrapper


@time_it
def do_work(n):
    for i in range(n):
        yield i * i


@time_it
def do_work_list(n):
    return [i * i for i in range(n)]


def try_catch(test):
    def decorate(f):
        def try_catch_wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as e:
                print(f"{test}: {e}")

        return try_catch_wrapper

    return decorate


@try_catch(test="Me")
def raise_exception(t):
    assert t == True, "Wow"


if __name__ == "__main__":
    # for j in do_work(50000):
    #     print(j)
    raise_exception(t=True)
