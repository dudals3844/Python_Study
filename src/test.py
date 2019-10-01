#Class

#diff JAVA
# class FourCal{
#     int first, second;
#     public Forcal(int first, int second){
#         this.first = first;
#         this.second = second;
#     }

#     public int add(){
#         return first+second
#     }

# }


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

class MoreFourCal(FourCal):
    def pow(self):
        return self.first ** self.second


#make obj
# a = FourCal(4,2)
#a.setdata(4,2)
a = MoreFourCal(4,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.sub())
print(a.pow())

#method overriding
class SafeFourCal(FourCal):
    #overriding
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


a = SafeFourCal(4,0)
print(a.div())


#Class variable
class Family:
    lastname = "Choi"

print(Family.lastname)

