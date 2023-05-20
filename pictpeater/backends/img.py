from pictpeater.base import Backend
from tempfile import mkstemp
from queue import Queue
from threading import Thread
from time import sleep

class BackendSave(Backend):
    queue = Queue()
    run = True
    suffix="jpeg"

    def __init__(self):
        super().__init__()
        consumer = Thread(target=self.consume)
        consumer.daemon=True
        consumer.start()

    def tx(self, im, cfg):
        cfgSave=cfg["backends"]["save"]
        fd, name=mkstemp(suffix="."+self.suffix, dir=cfgSave["image_dir"])
        self.queue.put((im, name))

    def consume(self):
        while self.run:
            if self.queue.empty():
                sleep(2)
                return
            im, name = self.queue.get()
            im.save(name, format=self.suffix, delete=False)
