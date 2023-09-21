

def time_logged_function(func:callable):    
    from time import time

    
    def inner(*args,**kwargs):
        
        
        start = time()
        output = func(*args,**kwargs)
        end = time()
        print(f"\nFinished {func.__name__} in {end-start} seconds\n")
        with open("time_log.txt","a") as file:
            file.write(f"Finished {func.__name__} in {end-start} seconds\n")
            

        return output

    return inner
