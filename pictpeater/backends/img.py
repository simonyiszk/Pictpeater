from pictpeater.base import Backend
from tempfile import mkstemp
from queue import Queue
from threading import Thread
from time import sleep

class BackendSave(Backend):
    queue = Queue()
    run = True
    suffix="jpeg"
    consumer = None

    def __init__(self):
        super().__init__()
        self.consumer = Thread(target=self.consume)
        self.consumer.daemon=True
        self.consumer.start()

    def tx(self, im, cfg):
        cfgSave=cfg["backends"]["save"]
        fd, name=mkstemp(suffix="."+self.suffix, dir=cfgSave["image_dir"])
        self.queue.put((im, name))

    def consume(self):
        while self.run:
            if self.queue.empty():
                sleep(2)
                continue
            im, name = self.queue.get()
            im.save(name, format=self.suffix, delete=False)
