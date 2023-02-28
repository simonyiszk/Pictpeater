#!/usr/bin/env python3
"""
Pictpeater main module
"""

from config import get_config as Config
import middleware
from backends import *
from frontends import *

"""
Version string
"""
PictpeaterVersion="Pictpeater v0.1alpha"
"""
Operation mode. Can be "Repeater" or "Beacon"
"""
PictpeaterMode="Beacon"

if __name__=="__main__":
	cfg=Config({"callsign": "HA5KFU"})
	middleware.register_frontends([FrontendBeacon()], [BackendSSTV()], cfg)
