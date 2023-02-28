"""
Pictpeater config handling
"""

import tomllib

def loadCfg(cfg):
	if cfg is None:
		return dict()
	elif type(cfg) is dict:
		return cfg
	elif type(cfg) is str:
		return tomllib.loads(cfg)
	else:
		return tomllib.load(cfg)

defaultConfig={
	"topBannerSize": 5,
	"topBannerColor": "# 0000FF",
	"topTextColor": "# 00FFFF",
	"bottomBannerSize": 5,
	"bottomBannerColor": "# 00FF00",
	"bottomTextColor": "# FFFF00",
	"callsign": ""
}

def get_config(cfg=None):
	cfgDict=defaultConfig
	for k, v in loadCfg(cfg).items():
		cfgDict[k]=v
	return cfgDict
