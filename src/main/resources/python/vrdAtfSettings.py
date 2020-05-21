'''
vrdAtfSettings
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
Encapsulates the configuration properties for a particular     vrCADFileTypes.FileType. Some of the properties only have an effect on certain file formats. Please have a look at the import dialog that changes its content with respect to the vrCADFileTypes.FileType of the imported files.
'''

from typing import List


class SourceReferenceBehavior():
    pass


class SmartReferenceBehavior():
    pass


def getChordDeviation() -> float:
    '''
    Get maximum deviation of tessellated mesh to the NURBS surface in mm.
    '''
    return None


def getCreateLayerGroups() -> bool:
    '''
    Query if creating group nodes from layer information is enabled..
    '''
    return None


def getFixSurfaceOrientation() -> bool:
    '''
    Query if orienting surface normals is enabled.
    '''
    return None


def getFlushTransformations() -> bool:
    '''
    Query if transformations should be flushed into the vertex coordinates.
    '''
    return None


def getImportAsSmartReference() -> bool:
    '''
    Query if smart references should be created for imported vpb files.
    '''
    return None


def getImportAssociativeMeshes() -> bool:
    '''
    Query if import of associative meshes is enabled.
    '''
    return None


def getImportCameras() -> bool:
    '''
    Query if import of cameras is enabled.
    '''
    return None


def getImportCoordSystems() -> bool:
    '''
    Query if import of coordinate system nodes is enabled.
    '''
    return None


def getImportCurves() -> bool:
    '''
    Query if import of curves and poly lines is enabled.
    '''
    return None


def getImportEmptyLayers() -> bool:
    '''
    Query if import of empty layers is enabled.
    '''
    return None


def getImportInvisibleCurves() -> bool:
    '''
    Query if import of curves and poly lines, that are invisible in CAD data, is enabled.
    '''
    return None


def getImportInvisibleInstances() -> bool:
    '''
    Query if import of invisible instance nodes is enabled.
    '''
    return None


def getImportInvisibleMeshes() -> bool:
    '''
    Query if import of polygon meshes, that are invisible in the CAD file, is enabled.
    '''
    return None


def getImportInvisibleSurfaces() -> bool:
    '''
    Query if import of surfaces, that are invisible in the CAD file, is enabled.
    '''
    return None


def getImportLights() -> bool:
    '''
    Query if import of light sources is enabled.
    '''
    return None


def getImportMeshes() -> bool:
    '''
    Query if import of polygon meshes is enabled.
    '''
    return None


def getImportMeshLODs() -> int:
    '''
    Query which mesh LODs should be imported.
    '''
    return None


def getImportReferencedFiles() -> bool:
    '''
    Query if import of part files referenced by an assembly is enabled.
    '''
    return None


def getImportSurfaces() -> bool:
    '''
    Query if import of surfaces is enabled.
    '''
    return None


def getImportTemplateGeometries() -> bool:
    '''
    Query if import of template geometries is enabled.
    '''
    return None


def getImportVariants() -> bool:
    '''
    Query if import of variants is enabled.
    '''
    return None


def getJtToolkit() -> int:
    '''
    Query which Jt toolkit is used for import.
    '''
    return None


def getKeepNurbs() -> bool:
    '''
    Query if NURBS data should be kept alongside with tessellation result.
    '''
    return None


def getMaxChordLength() -> float:
    '''
    Get maximum length of a triangle edge in mm.
    '''
    return None


def getMergeGeometries() -> bool:
    '''
    Query if tessellated meshes of adjacent NURBS surfaces with same material should be merged.
    '''
    return None


def getMergeSubReferenceMaterials() -> bool:
    '''
    Query if duplicate materials, referenced in different files, should be merged into one single material. Materials with same name and identical properties are regarded as duplicates.
    '''
    return None


def getNormalTolerance() -> float:
    '''
    Get the normal tolerance of adjacent triangles in degrees.
    '''
    return None


def getReduceKeyframes() -> bool:
    '''
    Query if reducing the number of keyframes is enabled.
    '''
    return None


def getRemoveEmptyGroups() -> bool:
    '''
    Query if groups without children should be removed.
    '''
    return None


def getSmartReferenceBehavior() -> SmartReferenceBehavior:
    '''
    Query how references to VRED native files are treated in import.
    '''
    return None


def getSourceReferenceBehavior() -> SourceReferenceBehavior:
    '''
    Query how references to files of import file types are treated in import.
    '''
    return None


def getStitchingTolerance() -> float:
    '''
    Get the stitching tolerance of adjacent edges in mm.
    '''
    return None


def getUnshareNodes() -> bool:
    '''
    Query if shared node instances should be converted to independent nodes.
    '''
    return None


def getUseLegacyLoader() -> bool:
    '''
    Query if using legacy importer is enabled.
    '''
    return None


def getUseStitching() -> bool:
    '''
    Query if stitching is enabled.
    '''
    return None


def setChordDeviation(chordDeviation: float):
    '''
    Set maximum allowed distance from the NURBS surface to the tessellated surface in mm. Lower values result in more accurate polygon models but also increase the number of triangles.
    '''
    pass


def setCreateLayerGroups(create: bool):
    '''
    Enable / Disable creation of group nodes for objects organized in layers. In case the parents of the objects in one layer have different transformations this might cause an unexpected scenegraph structure since it is required to preserve the transformations.
    '''
    pass


def setFixSurfaceOrientation(fix: bool):
    '''
    Enable orienting the normals of all surfaces, so they point in the same general direction.
    '''
    pass


def setFlushTransformations(flush: bool):
    '''
    Enable / Disable moving transformation data of the scene graph hierarchy to the vertices. This means, that every transformation node will contain only a unit matrix.
    '''
    pass


def setImportAsSmartReference(create: bool):
    '''
    Determine if smart references should be created for imported vpb files.
    '''
    pass


def setImportAssociativeMeshes(import_: bool):
    '''
    Enable import of meshes associated with the surfaces.
    '''
    pass


def setImportCameras(import_: bool):
    '''
    Enable import of cameras from CAD data. (Only Alias wire files)
    '''
    pass


def setImportCoordSystems(import_: bool):
    '''
    Enable import of coordinate system nodes from CAD data.
    '''
    pass


def setImportCurves(import_: bool):
    '''
    Enable import of curves and poly lines from CAD files.
    '''
    pass


def setImportEmptyLayers(import_: bool):
    '''
    Enable import of empty leyers. (Only Alias wire files)
    '''
    pass


def setImportInvisibleCurves(import_: bool):
    '''
    Enable import of curves and poly lines, that are invisible in the CAD data.
    '''
    pass


def setImportInvisibleInstances(import_: bool):
    '''
    Enable import of invisible instance nodes instead of excluding them.
    '''
    pass


def setImportInvisibleMeshes(import_: bool):
    '''
    Enable import of polygon meshes, that are invisible in the CAD file.
    '''
    pass


def setImportInvisibleSurfaces(import_: bool):
    '''
    Enable import of NURBS surfaces, that are invisible in the CAD file.
    '''
    pass


def setImportLights(import_: bool):
    '''
    Enable import of light sources from CAD data. (Only Alias wire files)
    '''
    pass


def setImportMeshes(import_: bool):
    '''
    Enable import of polygon meshes.
    '''
    pass


def setImportMeshLODs(lodOption: int):
    '''
    Select which mesh LODs should be imported.
    '''
    pass


def setImportReferencedFiles(import_: bool):
    '''
    Enable import of part files referenced by an assembly. If option is disabled a file reference node is created that can be used to import the referenced part later.
    '''
    pass


def setImportSurfaces(import_: bool):
    '''
    Enable import of NURBS surfaces.
    '''
    pass


def setImportTemplateGeometries(import_: bool):
    '''
    Enable import of template geometries instead of excluding them. (Only Alias wire files)
    '''
    pass


def setImportVariants(import_: bool):
    '''
    Enable import of variants from CAD data. (Only Alias wire files)
    '''
    pass


def setJtToolkit(toolkit: int):
    '''
    Select which Jt toolkit should be used for import.
    '''
    pass


def setKeepNurbs(keep: bool):
    '''
    Enable / disable keeping NURBS data instead of deleting it. This option will increase memory usage.
    '''
    pass


def setMaxChordLength(chordLength: float):
    '''
    Set maximum length of a triangle edge in mm. Lower values result in more accurate polygon models but also increase the number of triangles.
    '''
    pass


def setMergeGeometries(merge: bool):
    '''
    Enable / disable merging adjacent surfaces with same material into shells.
    '''
    pass


def setMergeSubReferenceMaterials(optimize: bool):
    '''
    Determine if duplicate materials, referenced in different files, should be merged into one single material. Materials with same name and identical properties are regarded as duplicates.
    '''
    pass


def setNormalTolerance(tolerance: float):
    '''
    Set the normal tolerance of adjacent triangles in degrees. Lower values result in more accurate polygon models but also increase the number of triangles.
    '''
    pass


def setReduceKeyframes(reduce: bool):
    '''
    Enable reducing the number of keyframes by removing adjacent keyframes with identical value.
    '''
    pass


def setRemoveEmptyGroups(remove: bool):
    '''
    Enable / disable removing of groups without children.
    '''
    pass


def setSmartReferenceBehavior(behavior: SmartReferenceBehavior):
    '''
    Determine how references to VRED native files are treated in import.
    '''
    pass


def setSourceReferenceBehavior(behavior: SourceReferenceBehavior):
    '''
    Determine how references to files of import file types are treated in import.
    '''
    pass


def setStitchingTolerance(tolerance: float):
    '''
    Set tolerance in mm where two adjacent edges are considered to be touching and where they should be stitched together.
    '''
    pass


def setUnshareNodes(unshare: bool):
    '''
    Enable / Disable conversion of shared node instances to independent nodes.
    '''
    pass


def setUseLegacyLoader(useLegacy: bool):
    '''
    Use legacy importer. Enabling this option is not recommended since the legacy importers only support quite old file versions and a reduced feature set. Legacy importer are only available for JT and Rhino files.
    '''
    pass


def setUseStitching(stitch: bool):
    '''
    Enable / disable stitching of adjacent edges.
    '''
    pass


def vrdAtfSettings():
    '''
    Default constructor.
    '''
    pass


def vrdAtfSettings():
    '''
    Documentation missing
    '''
    pass
