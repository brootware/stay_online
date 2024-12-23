# Simulate fake mouse movement and fake keyboard typing.

### How to use
```
# Default optional values
stay_online(
        stop_hhmm:str='', 
        min_delay_seconds:int=120, 
        max_delay_seconds:int=180, 
        min_num_words:int=1, 
        max_num_words:int=10,
        show_timestamp:bool=False
        )
```

stop_hhmm: Time to stop running the simulation in HHMM format, example '1700'.

min_delay_seconds: Minimum delay seconds.

max_delay_seconds: Maximum delay seconds.

min_num_words: Minimum number of words to type.

max_num_words: Maximum number of words to type.

show_timestamp: Type out the timestamp.