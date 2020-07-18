class Observer():
    def register(self, listener):
        raise NotImplementedError("Must subclass me")

    def deregister(self, listener):
        raise NotImplementedError("Must subclass me")

    def notify_listeners(self, event):
        raise NotImplementedError("Must subclass me")


class Listener():
    def __init__(self, name, Object):
        self.name = name
        Object.register(self)

    def notify(self, event):
        print(self.name, "received event", event)


class Object(Observer):
    def __init__(self):
        self.listeners = []
        self.data = None

    def Action(self,Event):
        self.data = Event
        return self.data

    def register(self, listener):
        self.listeners.append(listener)

    def deregister(self, listener):
        self.listeners.remove(listener)

    def notify_listeners(self, event):
        for listener in self.listeners:
            listener.notify(event)

def Test():
    print('Hello Observer')

if __name__ == "__main__":
    Object = Object()

    listenerA = Listener("<listener A>", Object)
    listenerB = Listener("<listener B>", Object)

    Object.notify_listeners("<event 1>")

    action = Object.Action(Test)
    Object.notify_listeners(action)


