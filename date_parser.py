import datetime

month = {
    'January': 1,
    'February':2,
    'March' : 3, 	
    'April' : 4,	
    'May' : 5,
    'June':6,
    'July':7,
    'August':8,
    'September':9,
    'October':10,
    'November':11,
    'December':12
}


def parse_date(date_time_str): 
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S.%fZ') 
    return date_time_obj.date()
    
            