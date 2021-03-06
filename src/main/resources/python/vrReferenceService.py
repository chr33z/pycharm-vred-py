'''
vrReferenceService
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
The reference service provides functions for querying and managing reference nodes. Additionally, settings from the preferences can be queried.
'''

from typing import List


class NotificationMode():
    pass


class vrdReferenceNode():
    pass


class ExportLocation():
    pass


class vrdNode():
    pass


class LoadMode():
    pass


def convertToSmart(node: vrdNode, useSourcePath: bool) -> vrdNode:
    '''
    Converts the passed node into a smart reference.
    '''
    return None


def createSmart(parent: vrdNode) -> vrdReferenceNode:
    '''
    Creates a new smart reference below the given parent.
    '''
    return None


def createSource(path: str, parent: vrdNode) -> vrdReferenceNode:
    '''
    Creates a new source reference with the given path.
    '''
    return None


def getAllAvailableFileFormats() -> List[str]:
    '''
    Returns a list with all file endings used in the loaded references (source and smart).
    '''
    return None


def getChildReferences():
    '''
    Documentation missing
    '''
    pass


def getCustomExportPath() -> str:
    '''
    Queries the custom export path.
    '''
    return None


def getExportLocation() -> ExportLocation:
    '''
    Queries the default smart export location mode.
    '''
    return None


def getLoadMode() -> LoadMode:
    '''
    Queries the load mode for smart references.
    '''
    return None


def getNotificationMode() -> NotificationMode:
    '''
    Queries the current file change notification mode.
    '''
    return None


def getParentReferences():
    '''
    Documentation missing
    '''
    pass


def getReferences():
    '''
    Documentation missing
    '''
    pass


def getRevisionMonitoringEnabled():
    '''
    Documentation missing
    '''
    pass


def getRevisionMonitoringExpressions():
    '''
    Documentation missing
    '''
    pass


def getSceneReferences() -> List[vrdReferenceNode]:
    '''
    Get all references in the scene
    '''
    return None


def getShowConvertToSmartWarning() -> bool:
    '''
    Queries the convert to smart warning flag.
    '''
    return None


def getUpdateMonitoringEnabled() -> bool:
    '''
    Checks if update monitoring is currently enabled.
    '''
    return None


def getUpdateMonitoringInterval() -> int:
    '''
    Returns the current time between background update checks in miliseconds.
    '''
    return None


def getUpdateMonitoringPaused() -> bool:
    '''
    Queries if the background update monitoring is currently in pause mode.
    '''
    return None


def pauseUpdateMonitoring(state: bool):
    '''
    Temporarily pauses / unpauses the background update monitoring. This will suspend the asynchrounous update check but will not cancel it.
    '''
    pass


def reimportSmartReferences(references: List[vrdReferenceNode]):
    '''
    Reimports the list of given smart references.
    '''
    pass


def reimportSourceReferences():
    '''
    Documentation missing
    '''
    pass


def removeReference(node: vrdReferenceNode) -> vrdNode:
    '''
    Converts the passed node into a none reference node.
    '''
    return None


def setCustomExportPath(path: str):
    '''
    Sets the custom path for exported smart references. This path will be used, when the location is set to Custom.
    '''
    pass


def setExportLocation(value: ExportLocation):
    '''
    Changes the default location mode for unsaved smart references.
    '''
    pass


def setLoadMode(value: LoadMode):
    '''
    Sets the load mode for smart references. LoadedReferences -> preserve the load state saved in the project AllReferences -> load all smart references NoReferences -> Do not load any smart reference LoadedSkipLeafReferences -> Load all but the leafes of the reference tree.
    '''
    pass


def setNotificationMode(value: NotificationMode):
    '''
    Sets the file change notification monitoring mode.
    '''
    pass


def setRevisionMonitoringEnabled(value: bool):
    '''
    Enables revision number check for update monitoring.
    '''
    pass


def setRevisionMonitoringExpressions(expressions: List[str]):
    '''
    Sets the list of regular expressions used to detect revision numbers.
    '''
    pass


def setShowConvertToSmartWarning(value: bool):
    '''
    Enables or disables warnings on convert to smart.
    '''
    pass


def setUpdateMonitoringEnabled(value: bool):
    '''
    Starts / stops the background update monitoring.
    '''
    pass


def setUpdateMonitoringInterval(msecs: int):
    '''
    Sets the update monitoring interval in miliseconds.
    '''
    pass


def sortRevisions(revisions: List[str]) -> List[str]:
    '''
    Sorts a list of revisions from oldest to newest.
    '''
    return None


def referenceCreated(node: vrdReferenceNode):
    '''
    Signal is emitted when a reference has been created.
    '''
    pass


def referenceEditStateChagned():
    '''
    Signal is emitted when a reference has been edited or edit has been undone.
    '''
    pass


def referencesChanged(nodes: List[vrdReferenceNode]):
    '''
    Signal is emitted when references have internal changes. If the list of nodes is empty, then all nodes should be considered as changed.
    '''
    pass


def sceneHasReferences(state: bool):
    '''
    Signal is sent when the scene has references or the last one is deleted
    '''
    pass


def sceneSelectionChanged(nodes: List[vrdReferenceNode]):
    '''
    This signal is sent when the selection of reference nodes in the scene graph changes.
    '''
    pass


def updateMonitoringChanged(state: bool):
    '''
    Signal is emitted when update monitoring is turned on or off.
    '''
    pass

