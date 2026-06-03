from typing import List
class Robot:
    def __init__(self, width: int, height: int):
       self.w=width
       self.h=height
       self.s=0 

    def step(self, num: int) -> None:
        self.s+=num

    def getPos(self) -> List[int]:
        a=(self.h+self.w)*2-4
        t=self.s%a
        if(0<=t<self.w):
            return [t,0]
        elif(self.w<=t<=self.w+self.h-2):
            return [self.w-1,t+1-self.w]
        elif(self.w+self.h-1<=t<=self.w+self.h+self.w-3):
            return [a-self.h-t+1,self.h-1]
        else:
            return [0,a-t]

    def getDir(self) -> str:
        a=(self.h+self.w)*2-4
        t=self.s%a
        if(self.s==0):
            return "East"
        else:
            if(0<t<self.w):
                return "East"
            elif(self.w<=t<=self.w+self.h-2):
                return "North"
            elif(self.w+self.h-1<=t<=self.w+self.h+self.w-3):
                return "West"
            else:
                return "South"

# Your Robot object will be instantiated and called as such:
obj = Robot(6,3)
obj.step(2)
obj.step(2)
print(obj.getPos())
print(obj.getDir())
obj.step(2)
obj.step(1)
obj.step(4)
print(obj.getPos())
print(obj.getDir())