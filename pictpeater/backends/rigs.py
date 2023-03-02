import Hamlib
from pictpeater.base import Rig

class RigHamlib(Rig):
	def __init__(self):
		rig=Hamlib.Rig(Hamlib.RIG_MODEL_NETRIGCTL)
		rig.open()
		self.rig=rig
	
	def ptt(self, ptt, cfg):
		self.rig.set_ptt(Hamlib.RIG_VFO_CURR, ptt)
