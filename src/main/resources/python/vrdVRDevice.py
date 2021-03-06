'''
vrdVRDevice
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
Represents a VR device like a controller or a tracker. This can be created before the actual device is connected with the system. When a device connects, VRED will map the physical device to the already created object. This allows to define mappings in advance.
'''

from typing import List


class QMatrix4x4():
    pass


class vrdButtonState():
    pass


class vrdNode():
    pass


class vrdRayIntersection():
    pass


class vrdVirtualTouchpadButton():
    pass


def addVirtualButton(button: vrdVirtualTouchpadButton, physicalButton: str):
    '''
    Adds a virtual button to the controller that maps a position of a button to a new signal.
    '''
    pass


def disableRay():
    '''
    Disables the currently activated pointing ray.
    '''
    pass


def enableRay(axis: str):
    '''
    Enables a pointing ray out of the controller.
    '''
    pass


def getButtonState(button: str) -> vrdButtonState:
    '''
    Gets the state of the current button.
    '''
    return None


def getName() -> str:
    '''
    Gets the name of the device
    '''
    return None


def getNode() -> vrdNode:
    '''
    Gets a node under the origin of the VR device. This node is not part of the scenegraph. If some geometry should be attached to the device, a constraint (see         vrConstraintService.createParentConstraint(targetNodes, constrainedNode, maintainOffset)) should be used. Example: vr/attachToController.py.
    '''
    return None


def getSerialNumber() -> str:
    '''
    Gets the serial number of the device.
    '''
    return None


def getTrackingMatrix():
    '''
    Documentation missing
    '''
    pass


def getVisualizationMode() -> int:
    '''
    Gets the current visualization mode.
    '''
    return None


def getVisualizationNode() -> vrdNode:
    '''
    Gets the root node of the controller visualization. If the controller is currently not visible or not detected by the tracking system, this function will return an empty node.
    '''
    return None


def isVisible() -> bool:
    '''
    Gets the visibility of the device.
    '''
    return None


def pick() -> vrdRayIntersection:
    '''
    Tries to pick the object in the scene at the intersection point of the pointing ray with the scene.
    '''
    return None


def removeVirtualButton(button: vrdVirtualTouchpadButton, physicalButton: str):
    '''
    Removes a virtual button that is related to a physical button.
    '''
    pass


def removeVirtualButton(virtualButton: str, physicalButton: str):
    '''
    Removes a virtual button that is related to a physical button.
    '''
    pass


def setButtonPressed(state: bool, button: str):
    '''
    Simulate a button press.
    '''
    pass


def setButtonTouched(state: bool, button: str):
    '''
    Simulate a button press.
    '''
    pass


def setTrackingMatrix(matrix: QMatrix4x4):
    '''
    Simulate a tracking position change.
    '''
    pass


def setVisible(visible: bool):
    '''
    Sets the VR device visible or invisible.
    '''
    pass


def setVisualizationMode(mode: int):
    '''
    Sets the visualization mode.
    '''
    pass


def signal():
    '''
    Documentation missing
    '''
    pass


def vibrate(milliseconds: int, axisId: int):
    '''
    Triggers the vibration functionality of the device if available.
    '''
    pass

