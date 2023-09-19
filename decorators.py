from time import time

def time_logged_function(func:callable):

    def inner(*args,**kwargs):
        
        
        
        start = time()
        output = func(*args,**kwargs)
        end = time()
        print(f"Finished {func.__name__} in {end-start} seconds\n")


        return output

    return inner

