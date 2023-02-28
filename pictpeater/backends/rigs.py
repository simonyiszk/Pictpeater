import Hamlib
from pictpeater.base import Rig

class RigHamlib(Rig):
	def ptt(self, ptt, cfg):
		rig=Hamlib.Rig(Hamlib.RIG_MODEL_NETRIGCTL)
		# TODO
		rig.open()
		rig.set_ptt(0, ptt)
