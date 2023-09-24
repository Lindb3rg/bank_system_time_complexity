from time import time

def time_logged_function(func:callable):

    def inner(*args,**kwargs):
        
        
        
        start = time()
        output = func(*args,**kwargs)
        end = time()
        elapsed_time = end-start
        seconds,remainder = divmod(elapsed_time,1)
        micro_seconds = remainder * 1e6
        print(f"\nFinished {func.__name__} in {seconds} seconds and {micro_seconds} micro seconds\n")


        return output

    return inner

