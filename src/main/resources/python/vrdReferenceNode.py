'''
vrdReferenceNode
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
Reference node.
'''

from typing import List


class State():
    pass


class ExportLocation():
    pass


def createSmartPath(location: ExportLocation, customPath: str) -> str:
    '''
    Constructs the path to the smart file.
    '''
    return None


def createSmartReference(useSourcePath: bool):
    '''
    Creates a smart file reference for this reference.
    '''
    pass


def createSourceReference():
    '''
    Creates a source file reference for this reference.
    '''
    pass


def getSmartCreationDate():
    '''
    Documentation missing
    '''
    pass


def getSmartFileState():
    '''
    Documentation missing
    '''
    pass


def getSmartLastModified():
    '''
    Documentation missing
    '''
    pass


def getSmartOwner():
    '''
    Documentation missing
    '''
    pass


def getSmartPath():
    '''
    Documentation missing
    '''
    pass


def getSmartRevision():
    '''
    Documentation missing
    '''
    pass


def getSmartRevisionPath():
    '''
    Documentation missing
    '''
    pass


def getSmartRevisions():
    '''
    Documentation missing
    '''
    pass


def getSourceFileState():
    '''
    Documentation missing
    '''
    pass


def getSourceImportDate():
    '''
    Documentation missing
    '''
    pass


def getSourceLastModified():
    '''
    Documentation missing
    '''
    pass


def getSourceOwner():
    '''
    Documentation missing
    '''
    pass


def getSourcePath():
    '''
    Documentation missing
    '''
    pass


def getSourceRevision():
    '''
    Documentation missing
    '''
    pass


def getSourceRevisionPath():
    '''
    Documentation missing
    '''
    pass


def getSourceRevisions():
    '''
    Documentation missing
    '''
    pass


def getState() -> State:
    '''
    Get the current status of the reference node.
    '''
    return None


def hasSmartReference():
    '''
    Documentation missing
    '''
    pass


def hasSourceReference():
    '''
    Documentation missing
    '''
    pass


def isChanged():
    '''
    Documentation missing
    '''
    pass


def isLoaded():
    '''
    Documentation missing
    '''
    pass


def isRootNode():
    '''
    Documentation missing
    '''
    pass


def isSelfOrSubReferenceChanged():
    '''
    Documentation missing
    '''
    pass


def isSubReferenceChanged():
    '''
    Documentation missing
    '''
    pass


def load():
    '''
    Loads the reference content.
    '''
    pass


def loadSmartReference():
    '''
    Loads the reference content, if this reference contains a source reference.
    '''
    pass


def loadSourceReference():
    '''
    Loads the reference content, if this reference contains a smart reference.
    '''
    pass


def removeSmartReference():
    '''
    Removes the smart reference information from this reference.
    '''
    pass


def removeSourceReference():
    '''
    Removes the source reference information from this reference.
    '''
    pass


def saveSmartReference():
    '''
    Save changes to the referenced project file.
    '''
    pass


def saveSmartReferenceAs(path: str, unshare: bool):
    '''
    Save content of the reference to a new project file.
    '''
    pass


def setSmartPath(path: str):
    '''
    Change the path to the smart reference file.
    '''
    pass


def setSourcePath(path: str):
    '''
    Change the path to the source file.
    '''
    pass


def unload():
    '''
    Remove all children of this node and mark as not loaded.
    '''
    pass

