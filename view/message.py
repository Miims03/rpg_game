ERROR,SUCCESS,MSG = range(3)

WRONG_INPUT = "WRONG INPUT"


class Message():
    def __init__(self,message="",status=MSG) -> None:
        self.message = message
        self.STATUS = status
        
    def bordered_message(self, width=40):
        border = "-" * width
        #padded_message = f"{border}\nPriority: {self.priority}, Message: {self.message}\n"
        padded_message = f"{border}\nSTATUS: {self.STATUS}{self.message.center(width)}\n{border}"
        return padded_message
        
    def __str__(self) -> str:
        return self.message
    

# def test():
#     msg = Message("coucou")
#     print(msg)
# test()