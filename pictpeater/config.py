"""
Pictpeater config handling
"""

import json

def loadCfg(cfg):
	if cfg is None:
		return dict()
	elif isinstance(cfg, dict):
		return cfg
	elif isinstance(cfg, str):
		return json.loads(cfg)
	else:
		return json.load(cfg)

defaultConfig={
	"topBannerSize": 10,
	"topBannerColor": "#0000FF",
	"topTextColor": "#00FFFF",
	"bottomBannerSize": 8,
	"bottomBannerColor": "#00FF00",
	"bottomTextColor": "#FF0000",
	"callsign": ""
}

def get_config(cfg=None):
	try:
		cfgDict = open("config.json", "r")
	except FileNotFoundError:
		cfgDict=defaultConfig
	for k, v in loadCfg(cfg).items():
		cfgDict[k]=v
	return cfgDict
