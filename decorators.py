
def time_logged_function(func:callable):    
    from time import time

    
    def inner(*args,**kwargs):
        
        
        start = time()
        output = func(*args,**kwargs)
        end = time()
        elapsed_time = end-start
        seconds,remainder = divmod(elapsed_time,1)
        micro_seconds = remainder * 1e6
        print(f"\nFinished {func.__name__} in {seconds} seconds and {micro_seconds}\n")
        with open("time_log.txt","a") as file:
            file.write(f"Finished {func.__name__} in {seconds} seconds and micro_seconds\n")
            

        return output

    return inner