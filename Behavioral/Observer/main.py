class Customer():
    def __init__(self,name) -> None:
        self.__name = name

    def getName(self):
        return self.__name

    def notify(self,message):
        return f" Notify user {self.__name} about {message} "
        

