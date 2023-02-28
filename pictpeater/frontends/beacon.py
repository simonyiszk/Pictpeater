from pathlib import Path
from pictpeater.base import Frontend
from PIL import Image
from threading import Timer

class FrontendBeacon(Frontend):
	def register(self, cb_submit_im, cfg):
		cfgBeacon=cfg["frontends"]["beacon"]
		self.submit=cb_submit_im
		self.period=600
		self.images=list(Path(cfgBeacon["image_dir"]).iterdir())
		self.image_idx=0
		self.timer_init()
	
	def timer_init(self):
		Timer(self.period, self.send_pic).start()
	
	def send_pic(self):
		with Image.open(self.images[self.image_idx]) as im:
			self.submit(im)
			self.image_idx+=1
			if self.image_idx>=len(self.images):
				self.image_idx=0
		self.timer_init()
