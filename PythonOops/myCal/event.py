from datetime import datetime
from user import User
from invitation import Invitation

class Event(object):
    ID = 1
    def __init__(self, title=None, owner=None, start_time=None, end_time=None, location=None):
        self.id = Event.ID
        self.title = title
        self.owner = owner
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.user_list = [owner]
        Event.ID += 1

    def send_invite(self):
        for u in self.user_list:
            invite = Invitation(from_user=self.owner, to_user=u, event=self)
            invite.send()

    def display(self):
        print(f"Name: {self.title}")
        print(f"Host: {self.owner}")
        print(f"From: {self.start_time} To:{self.end_time}")
        print(f"Where: {self.location}")
        print(f"Attendees: {self.user_list}")

class ReminderEvent(Event):
    def __init__(self, snooze=5, **kwargs):
        super().__init__(**kwargs)
        self.snooze = snooze
    
    def display(self):
        super().display()
        print(f"Snooze: {self.snooze}")
    


if __name__ == '__main__':
    u1 = User(name='A')
    u2 = User(name='B')
    u3 = User(name='C')

    e1 = ReminderEvent(snooze=10, title="Assignment", owner=u1, start_time=datetime.now(), end_time=datetime.now(), location="Office")
    e1.display()
    