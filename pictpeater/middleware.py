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
	fontFace="DejaVuSerif-Bold"
	if cfg["topBannerSize"] > 0:
		bannerH=imH*cfg["topBannerSize"]//100
		font=ImageFont.truetype(fontFace, size=bannerH)
		draw.rectangle([0, 0, imW, bannerH], fill=cfg["topBannerColor"])
		draw.text([0, 0], cfg["callsign"], fill=cfg["topTextColor"], font=font)
		draw.text([imW, 0], PictpeaterMode, fill=cfg["topTextColor"], font=font, anchor="ra")
	if cfg["bottomBannerSize"] > 0:
		bannerH=imH*cfg["bottomBannerSize"]//100
		font=ImageFont.truetype(fontFace, size=bannerH)
		draw.rectangle([0, imH-bannerH, imW, imH], fill=cfg["bottomBannerColor"])
		draw.text([0, imH], PictpeaterVersion, fill=cfg["bottomTextColor"], font=font, anchor="ld")
		draw.text([imW, imH], cfg["callsign"], fill=cfg["bottomTextColor"], font=font, anchor="rd")

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
