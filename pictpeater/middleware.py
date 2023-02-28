"""
Pictpeater watermarking and processing module
"""

from PIL import Image, ImageDraw, ImageFont
from pictpeater import PictpeaterVersion, PictpeaterMode

"""
Watermark the image
"""
def watermark(im, cfg):
	draw=ImageDraw.Draw(im)
	(imW, imH)=im.size
	if cfg["topBannerSize"] > 0:
		bannerH=imH*cfg["topBannerSize"]//100
		draw.rectangle([0, 0, imW, bannerH], fill=cfg["topBannerColor"])
		draw.text([0, 0], cfg["callsign"], fill=cfg["topTextColor"], font=ImageFont.truetype("DejaVuSerif", size=bannerH))
		draw.text([0, 0], PictpeaterMode, fill=cfg["topTextColor"], font=ImageFont.truetype("DejaVuSerif", size=bannerH), anchor="rt")
	if cfg["bottomBannerSize"] > 0:
		bannerH=imH*cfg["bottomBannerSize"]//100
		draw.rectangle([imH-bannerH, 0, imW, imH], fill=cfg["bottomBannerColor"])
		draw.text([imH, 0], PictpeaterVersion, fill=cfg["bottomTextColor"], font=ImageFont.truetype("DejaVuSerif", size=bannerH), anchor="lb")
		draw.text([imH, imW], cfg["callsign"], fill=cfg["bottomTextColor"], font=ImageFont.truetype("DejaVuSerif", size=bannerH), anchor="rb")

def _dispatch(im, backends, cfg):
	watermark(im, cfg)
	for bk in backends:
		bk.tx(im, cfg)

"""
Register the given frontends and connect them to the backends
"""
def register_frontends(frontends, backends, cfg):
	dispatcher=lambda im: _dispatch(im, backends, cfg)
	for fe in frontends:
		fe.register(dispatcher, cfg)
