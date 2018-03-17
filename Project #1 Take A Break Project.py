import time,webbrowser
count_break = 0
total_breaks = 3

print("The program is started at", time.ctime()) # Gives the current time
while total_breaks > count_break:
    time.sleep(5) # Mention seconds
    webbrowser.open("https://www.youtube.com/watch?v=9lNqiCr7LtA&index=24&list=PLAwxTw4SYaPnYajEbZvqtcVWQ6XGhvtOW")
    count_break = count_break + 1
    
print("The program is completed at", time.ctime())
    
    
