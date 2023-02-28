#!/usr/bin/env python3
"""
Pictpeater main module
"""

from pictpeater.config import get_config as Config
from pictpeater import middleware
from pictpeater.backends import *
from pictpeater.frontends import *

def main():
	cfg=Config({"callsign": "HA5KFU"})
	middleware.register_frontends([FrontendBeacon()], [BackendSSTV()], cfg)

if __name__=="__main__":
	main()
