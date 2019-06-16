class Invitation:

    def __init__(self, from_user, to_user, event):
        self.from_user = from_user
        self.to_user = to_user
        self.event = event
    
    def accept(self):
        self.to_user.calendar[]
    
    def reject(self):
        pass
    
    def send(self):
        self.to_user.invitations.append(self)
