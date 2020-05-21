'''
vrdPointLightNode
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
Returns the falloff of the light intensity.
'''

from typing import List


class vrdLensFlareEffect():
    pass


class vrdLightTexture():
    pass


class vrdLightProfile():
    pass


class Attenuation():
    pass


def getAttenuation() -> Attenuation:
    '''
    Returns the falloff of the light intensity.
    '''
    return None


def getLensFlareEffect() -> vrdLensFlareEffect:
    '''
    Returns the lens flare effect.
    '''
    return None


def getLightProfile() -> vrdLightProfile:
    '''
    Returns the light profile.
    '''
    return None


def getTexture() -> vrdLightTexture:
    '''
    Returns the light texture.
    '''
    return None


def setAttenuation(attenuation: Attenuation):
    '''
    Sets the falloff of the light intensity.
    '''
    pass
