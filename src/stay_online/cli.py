from stay_online.stay_online import stay_online

def run_cli():
    stop_hhmm:str='', 
    min_delay_seconds:int=120, 
    max_delay_seconds:int=180, 
    min_num_words:int=1, 
    max_num_words:int=10,
    show_timestamp:bool=False
    
    app = stay_online(stop_hhmm,min_delay_seconds,max_delay_seconds,min_num_words,max_num_words,show_timestamp)
    app.run()