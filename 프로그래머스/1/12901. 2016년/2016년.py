from datetime import datetime
def solution(a, b):
    days_of_week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    
    print(datetime(2016, a, b).weekday())
    return days_of_week[datetime(2016, a, b).weekday()]