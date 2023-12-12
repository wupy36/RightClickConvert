import bpy
from pathlib import Path
import os

OBJ_EXTENSION = ".obj"
STL_EXTENSION = ".stl"
FBX_EXTENSION = ".fbx"


def getModelInfo(model):
    modelname = Path(model).stem
    modeltype = Path(model).suffix
    modelpath = Path(model).parent
    return modelname, modeltype, modelpath


def blendFile(model):
    modelname, modeltype, modelpath = getModelInfo(model)

    print('File Selected :  ', model)
    print('File Name:   ', modelname)
    print('File extension:   ', modeltype)
    print('Directory Name:   ', modelpath)

    new_folder_path = modelpath / "BlendFiles"

    if not new_folder_path.exists():
        new_folder_path.mkdir()

    blendtype = modelname + ".blend"
    new_file_path = new_folder_path / str(blendtype)

    for obj in bpy.data.objects:
        bpy.data.objects.remove(obj)

    file_loc = bpy.path.abspath(model)
    print('Converted file path to Absolute: ', file_loc)

    if STL_EXTENSION == modeltype:
        bpy.ops.import_mesh.stl(filepath=file_loc)
    elif OBJ_EXTENSION == modeltype:
        bpy.ops.import_scene.obj(filepath=file_loc)
    elif FBX_EXTENSION == modeltype:
        bpy.ops.import_scene.fbx(filepath=file_loc)
    else:
        print("Not a valid FileType OBJ, STL and FBX Only")
        print("******************************ENDING******************************")
        exit()

    for obj_object in bpy.data.objects:
        print('Imported name: ', obj_object.name)

    if not new_file_path.exists:
        bpy.ops.wm.save_as_mainfile(filepath=str(new_file_path))

    print("BlendFile Save Path: " + str(new_file_path))
    bpy.ops.wm.save_mainfile(filepath=str(new_file_path))


def blendSave(model):

    modelname, _, modelpath = getModelInfo(model)

    # Define the new folder path
    new_folder_path = modelpath / "BlendFiles"

    # Create the new folder if it doesn't exist
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

    # blend file naming and saving
    blendtype = modelname + ".blend"
    new_file_path = new_folder_path / str(blendtype)

    # save the work we have done
    bpy.ops.wm.save_mainfile(filepath=str(new_file_path))


def blendExportSingle(model):

    modelname, modeltype, modelpath = getModelInfo(model)
    print(f"Processing {modelname}...")

    # Get the opposite file extension
    opposite_extension = STL_EXTENSION if modeltype == OBJ_EXTENSION else OBJ_EXTENSION

    # Define the new folder path
    new_folder_path = modelpath / "ChangeFileTypes"

    # Create the new folder if it doesn't exist
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

    # ChangeFileType naming and saving
    filetypeopposite = modelname + opposite_extension

    # Define the new file path
    new_file_path = new_folder_path / filetypeopposite

    print(f"Exporting {modelname} to {new_file_path}...")

    # Run the export operator
    export_function = EXPORT_FUNCTIONS.get(opposite_extension)

    if not export_function:
        print('Invalid Export function: ', export_function)
        exit()

    # Convert the new_file_path to a string
    new_file_path_str = str(new_file_path)

    export_function(filepath=new_file_path_str, use_selection=True)

    print(f"Finished exporting {modelname}.\n")
