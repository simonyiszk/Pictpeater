from pictpeater.base import Backend
from pysstv.color import MODES as ColorModes
from pysstv.grayscale import MODES as GreyModes
from queue import Queue
import simpleaudio as sa
from threading import Thread
from time import sleep

def get_mode(mode):
	for cls in ColorModes:
		if cls.__name__==mode:
			return cls
	for cls in GreyModes:
		if cls.__name__==mode:
			return cls
	raise ValueError("No SSTV mode: '{}'".format(mode))

class BackendSSTV(Backend):
	queue = Queue()
	samp_rate=48000
	bits=8
	run = True
	comsumer = None
	def __init__(self):
		super().__init__()
		self.consumer = Thread(target=self.consume)
		self.consumer.daemon=True
		self.consumer.start()

	def tx(self, im, cfg):
		cfgSSTV=cfg["backends"]["sstv"]
		Mode=get_mode(cfgSSTV["mode"])
		sstv=Mode(im.resize((Mode.WIDTH, Mode.HEIGHT)), self.samp_rate, self.bits)
		sstv.vox_enabled=True
		if "fsk_id" in cfgSSTV:
			sstv.add_fskid_text(cfgSSTV["fsk_id"])
		self.queue.put((sstv, cfg))

	def consume(self):
		while self.run:
			if self.queue.empty():
				sleep(2)
				continue
			sstv, cfg = self.queue.get()
			self.rig.ptt(True, cfg)
			play_obj=sa.play_buffer(bytes(i+128 for i in sstv.gen_samples()), 1, self.bits//8, self.samp_rate)
			play_obj.wait_done()
			self.rig.ptt(False, cfg)
