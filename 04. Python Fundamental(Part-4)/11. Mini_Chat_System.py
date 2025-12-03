# Message class
class Message:
    message_counter = 1
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter +=1

    def __str__(self):
        return f"({self.id}) {self.sender.username}:{self.content}"
    

    