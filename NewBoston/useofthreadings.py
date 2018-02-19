import threading

class BuckysMessenger(threading.Thread):
    def run(self):
        for _ in range(100):#here we just want to loop 10 times and dont really
            print(threading.current_thread().getName())#care about variables

x = BuckysMessenger(name='Send out messeges')
y = BuckysMessenger(name='Recieve messeges')
x.start()
y.start()
