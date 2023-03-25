#!/usr/bin/env python3
"""
Pictpeater main module
"""

from pictpeater.config import get_config as Config
from pictpeater import middleware
from pictpeater.backends import *
from pictpeater.frontends import *

def main():
    with open("config.json") as configFile:
    	cfg=Config(configFile.read())
	    middleware.register_frontends([FrontendBeacon()], [BackendSSTV().set_rig(RigHamlib()), BackendSave()], cfg)

if __name__=="__main__":
	main()
