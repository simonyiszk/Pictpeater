"""
Pictpeater module base classes
"""

"""
A class representing a specific transmission mode and modulation
"""
class Backend:
	def __init__(self):
		self.rig=RigDummy()
	
	"""
	Send the image
	"""
	def tx(self, im, cfg):
		raise NotImplementedError("Backend has no `tx()` method!")
	
	def set_rig(self, rig):
		self.rig=rig
		return self

"""
A wrapper for controlling the radio hardware
"""
class Rig:
	"""
	Engage/disengage the radio transmitter
	"""
	def ptt(self, ptt, cfg):
		raise NotImplementedError("Rig does not support PTT")

"""
A no-op dummy rig
"""
class RigDummy(Rig):
	def ptt(self, ptt, cfg):
		pass

"""
A class for the various receivers/decoders and other image sources
"""
class Frontend:
	"""
	Register this frontend
	@param cb_submit_im is a function taking a (newly received) Image
	"""
	def register(self, cb_submit_im, cfg):
		raise NotImplementedError("Frontend has no `register()` method!")
