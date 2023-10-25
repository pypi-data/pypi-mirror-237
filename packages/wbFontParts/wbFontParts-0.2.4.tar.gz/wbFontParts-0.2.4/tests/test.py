from fontParts.test import testEnvironment
from wbFontParts.font import RFont
from wbFontParts.info import RInfo
from wbFontParts.groups import RGroups
from wbFontParts.kerning import RKerning
from wbFontParts.features import RFeatures
from wbFontParts.lib import RLib
from wbFontParts.layer import RLayer
from wbFontParts.glyph import RGlyph
from wbFontParts.contour import RContour
from wbFontParts.point import RPoint
from wbFontParts.segment import RSegment
from wbFontParts.bPoint import RBPoint
from wbFontParts.component import RComponent
from wbFontParts.anchor import RAnchor
from wbFontParts.guideline import RGuideline
from wbFontParts.image import RImage

classMapping = dict(
	font=RFont,
	info=RInfo,
	groups=RGroups,
	kerning=RKerning,
	features=RFeatures,
	layer=RLayer,
	glyph=RGlyph,
	contour=RContour,
	segment=RSegment,
	bPoint=RBPoint,
	point=RPoint,
	anchor=RAnchor,
	component=RComponent,
	image=RImage,
	lib=RLib,
	guideline=RGuideline,
)

def wbFontPartObjectGenerator(cls):
	unrequested = []
	obj = classMapping[cls]()
	return obj, unrequested

if __name__ == '__main__':
	import sys
	if {"-v", "--verbose"}.intersection(sys.argv):
		verbosity = 2
	else:
		verbosity = 1
	testEnvironment(wbFontPartObjectGenerator, verbosity=verbosity)
	