class FourCal:
    #__init__ 생성자다
    def __init__(self,first,second):
        self.first = first
        self.second = second

    
    def add(self):#전역변수 받기
        return self.first + self.second

    def mul(self):
        return self.first * self.second

    def sub(self):
        return self.first - self.second

    def div(self):
        return self.first / self.second
