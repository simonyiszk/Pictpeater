from pictpeater.base import Backend
from tempfile import mkstemp

class BackendSave(Backend):
	def tx(self, im, cfg):
		cfgSave=cfg["backends"]["save"]
		suffix="jpeg"
		fd, name=mkstemp(suffix="."+suffix, dir=cfgSave["image_dir"])
		im.save(name, format=suffix, delete=False)
