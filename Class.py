class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.model=model
        self.speed_limit=speed_limit
        self.company=company
    
    def start(self):
        print("started")
        

    def stop(self):
        print("stopped")

        
    def accelarate(self):
        print ("accelerated")


car1= Car("s-class 350d","sky blue","mercedes-benz","250km/h")
print()

