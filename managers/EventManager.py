class EventManager:
    registeredCallback = {}

    EVENT_COLLISION = 1
    EVENT_GOAL_LEFT = 2
    EVENT_GOAL_RIGHT = 3

    def registerCallback(self, callback, event):
        self.registeredCallback[event] = callback

    def dispatchEvent(self, event):
        if event in self.registeredCallback:
            self.registeredCallback[event](event)