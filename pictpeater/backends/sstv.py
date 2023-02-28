from pictpeater.base import Backend
from pysstv.color import MODES as ColorModes
from pysstv.grayscale import MODES as GreyModes
import simpleaudio as sa

def get_mode(mode):
	for cls in ColorModes:
		if cls.__name__==mode:
			return cls
	for cls in GreyModes:
		if cls.__name__==mode:
			return cls
	raise ValueError("No SSTV mode: '{}'".format(mode))

class BackendSSTV(Backend):
	def tx(self, im, cfg):
		samp_rate=48000
		bits=8
		cfgSSTV=cfg["backends"]["sstv"]
		Mode=get_mode(cfgSSTV["mode"])
		sstv=Mode(im.resize((Mode.WIDTH, Mode.HEIGHT)), samp_rate, bits)
		sstv.vox_enabled=True
		if "fsk_id" in cfgSSTV:
			sstv.add_fskid_text(cfgSSTV["fsk_id"])
		self.rig.ptt(True, cfg)
		play_obj=sa.play_buffer(bytes(i+128 for i in sstv.gen_samples()), 1, bits//8, samp_rate)
		play_obj.wait_done()
		self.rig.ptt(False, cfg) 
