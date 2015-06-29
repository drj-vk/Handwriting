# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pamImage', [dirname(__file__)])
        except ImportError:
            import _pamImage
            return _pamImage
        if fp is not None:
            try:
                _mod = imp.load_module('_pamImage', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pamImage = swig_import_helper()
    del swig_import_helper
else:
    import _pamImage
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class RGBPixel(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RGBPixel, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RGBPixel, name)
    __repr__ = _swig_repr
    __swig_setmethods__["r"] = _pamImage.RGBPixel_r_set
    __swig_getmethods__["r"] = _pamImage.RGBPixel_r_get
    if _newclass:r = _swig_property(_pamImage.RGBPixel_r_get, _pamImage.RGBPixel_r_set)
    __swig_setmethods__["g"] = _pamImage.RGBPixel_g_set
    __swig_getmethods__["g"] = _pamImage.RGBPixel_g_get
    if _newclass:g = _swig_property(_pamImage.RGBPixel_g_get, _pamImage.RGBPixel_g_set)
    __swig_setmethods__["b"] = _pamImage.RGBPixel_b_set
    __swig_getmethods__["b"] = _pamImage.RGBPixel_b_get
    if _newclass:b = _swig_property(_pamImage.RGBPixel_b_get, _pamImage.RGBPixel_b_set)
    __swig_setmethods__["m"] = _pamImage.RGBPixel_m_set
    __swig_getmethods__["m"] = _pamImage.RGBPixel_m_get
    if _newclass:m = _swig_property(_pamImage.RGBPixel_m_get, _pamImage.RGBPixel_m_set)
    def __init__(self): 
        this = _pamImage.new_RGBPixel()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pamImage.delete_RGBPixel
    __del__ = lambda self : None;
RGBPixel_swigregister = _pamImage.RGBPixel_swigregister
RGBPixel_swigregister(RGBPixel)

NO_IMAGE = _pamImage.NO_IMAGE
BW_IMAGE = _pamImage.BW_IMAGE
GRAY_IMAGE = _pamImage.GRAY_IMAGE
RGB_IMAGE = _pamImage.RGB_IMAGE
INT_IMAGE = _pamImage.INT_IMAGE
class PamImage(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PamImage, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PamImage, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pamImage.new_PamImage(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pamImage.delete_PamImage
    __del__ = lambda self : None;
    def clear(self): return _pamImage.PamImage_clear(self)
    def loadImage(self, *args): return _pamImage.PamImage_loadImage(self, *args)
    def save(self, *args): return _pamImage.PamImage_save(self, *args)
    def convert(self, *args): return _pamImage.PamImage_convert(self, *args)
    def getFileName(self): return _pamImage.PamImage_getFileName(self)
    def getWidth(self): return _pamImage.PamImage_getWidth(self)
    def getHeight(self): return _pamImage.PamImage_getHeight(self)
    def getFormat(self): return _pamImage.PamImage_getFormat(self)
    def getGrayPixels(self): return _pamImage.PamImage_getGrayPixels(self)
    def getRGBPixels(self): return _pamImage.PamImage_getRGBPixels(self)
    def getIntPixels(self): return _pamImage.PamImage_getIntPixels(self)
    def get_minval(self): return _pamImage.PamImage_get_minval(self)
    def get_maxval(self): return _pamImage.PamImage_get_maxval(self)
    def getImageType(self): return _pamImage.PamImage_getImageType(self)
    def getPixelGray(self, *args): return _pamImage.PamImage_getPixelGray(self, *args)
    def getPixelRGB(self, *args): return _pamImage.PamImage_getPixelRGB(self, *args)
    def getPixelInt(self, *args): return _pamImage.PamImage_getPixelInt(self, *args)
    def printAsciiArt(self): return _pamImage.PamImage_printAsciiArt(self)
    def putPixel(self, *args): return _pamImage.PamImage_putPixel(self, *args)
PamImage_swigregister = _pamImage.PamImage_swigregister
PamImage_swigregister(PamImage)

# This file is compatible with both classic and new-style classes.


