from datetime import date, datetime
import sys

class MyCalendar:
    def __init__(self, *args) -> None:
        self.datas = []
        self.add_holiday(*args)

    def add_holiday(self, *args) -> None:
        for data in args:
            a = self.validate_data(data)
            if a:
                self.datas.append(a)
        self.datas = list(set(self.datas))

    def check_holiday(self, data) -> bool:
        return self.validate_data(data) in self.datas

    def validate_data(self, data) -> date:

        if isinstance(data, date):
            return data
            
        elif isinstance(data, str):
            try:
                return datetime.strptime(data, '%d/%m/%Y').date()
            except:
                return None
           
       
        
        

       
        
        