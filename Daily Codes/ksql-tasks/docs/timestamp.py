from datetime import datetime

def convert_To_human_readable(epoch_time):
    readable_time = datetime.fromtimestamp(epoch_time / 1000).strftime('%Y-%m-%d %H:%M:%S')
    return readable_time

window_start1 = 1736222400000
window_end1 = 1736226000000
window_start2 = 1736222700000
window_end2 = 1736226300000

print("First Window starts at : ",convert_To_human_readable(window_start1))
print("First Window ends at : ",convert_To_human_readable(window_end1))
print("Second Window starts at : ",convert_To_human_readable(window_start2)) 
print("Second Window ends at : ",convert_To_human_readable(window_end2))