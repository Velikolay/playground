class MyQueue(object):
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def peek(self):
        self._update_outbox()
        if self.outbox:
            return self.outbox[-1]
        else:
            None

    def pop(self):
        self._update_outbox()
        if self.outbox:
            return self.outbox.pop()
        else:
            None

    def put(self, value):
        self.inbox.append(value)

    def _update_outbox(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
