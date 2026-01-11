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
    

# -------------------------------# User Class# -------------------------------
class User:
def __init__(self, username):
    self.username = username
    self.chatroom = None
    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom.")
            else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")
            def leave_chatroom(self):
                if not self.chatroom:
            