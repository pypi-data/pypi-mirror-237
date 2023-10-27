"""
Medical image reader

Extensions:
    - DICOM
    - NIFTI
    - MHA
    
"""

from pathlib import Path
from typing import Tuple, Union

import nibabel as nib
import numpy as np
import pydicom as dicom
import SimpleITK as sitk

from .custom_type import MedicalImage, PathMedicalImage, PathNpType
from .helper_path import path_in


def reader(path: PathMedicalImage) -> PathMedicalImage:
    """
    Read the medical image based on its file extension.

    This function supports various medical image file formats, including
    but not limited to NIfTI (`.nii`, `.nii.gz`), DICOM (`.dcm`), MHA (`.mha`),
    and NumPy arrays (`.npy`, `.npz`).

    Parameters:
        path (PathMedicalImage): Path to the medical image file or an already loaded image object.
                                 Expected types include str, Path, or specific medical image objects
                                 like MedicalImage.

    Returns:
        object: Loaded medical image object.

    Raises:
        TypeError: If the provided file format is unsupported.
    """
    if isinstance(path, MedicalImage):
        return path

    path = path_in(path)
    if path.suffix in [".nii", ".nii.gz"]:
        return nib.load(path)
    elif path.suffix == ".dcm":
        return dicom.dcmread(path)
    elif path.suffix == ".mha":
        return sitk.ReadImage(str(path))
    elif path.suffix == ".npy":
        return np.load(path)
    elif path.suffix == ".npz":
        return np.load(path)["arr_0"]
    else:
        raise TypeError(f"Unsupported file type: {path.suffix}")


def reader(*paths: Union[str, Path]) -> Union[object, Tuple[object]]:
    """
    Read one or more medical images based on their file extensions.

    This function supports various medical image file formats, including
    but not limited to NIfTI (`.nii`, `.nii.gz`), DICOM (`.dcm`), MHA (`.mha`),
    and NumPy arrays (`.npy`, `.npz`).

    Parameters:
        *paths (Union[str, Path]): Paths to the medical image files or already loaded image objects.

    Returns:
        Union[object, Tuple[object]]: If a single path is provided, returns a single loaded medical image object.
                                      If multiple paths are provided, returns a tuple of loaded medical image objects.

    Raises:
        TypeError: If the provided file format is unsupported.
    """

    def load_image(path: Union[str, Path]) -> object:
        if isinstance(path, MedicalImage):
            return path

        path_obj = path_in(path)

        if path_obj.suffix in [".nii", ".nii.gz"]:
            return nib.load(path_obj)
        elif path_obj.suffix == ".dcm":
            return dicom.dcmread(path_obj)
        elif path_obj.suffix == ".mha":
            return sitk.ReadImage(str(path_obj))
        elif path_obj.suffix == ".npy":
            return np.load(path_obj)
        elif path_obj.suffix == ".npz":
            return np.load(path_obj)["arr_0"]
        else:
            raise TypeError(f"Unsupported file type: {path_obj.suffix}")

    images = tuple(load_image(path) for path in paths)
    if len(images) == 1:
        return images[0]
    return images


# def im2arr(path: PathNpType) -> np.ndarray:
#     """
#     Convert the medical image to a numpy array based on its file extension.

#     Parameters:
#         path (Union[str, Path]): Path to the image.

#     Returns:
#         Image data as a numpy array.
#     """

#     if isinstance(path, np.ndarray):
#         return path

#     path = path_in(path)

#     if path.suffix in [".nii", ".nii.gz"]:
#         return nib.load(path).get_fdata()
#     elif path.suffix == ".dcm":
#         return dicom.dcmread(path).pixel_array
#     elif path.suffix == ".mha":
#         sitk_image = sitk.ReadImage(
#             str(path)
#         )  # SimpleITK python wrapper has no support for pathlib.Path
#         return sitk.GetArrayFromImage(sitk_image)
#     elif path.suffix == ".npy":
#         return np.load(path)

#     elif path.suffix == ".npz":
#         return np.load(path)["arr_0"]
#     else:
#         raise TypeError(f"Unsupported file type: {path.suffix}")


def im2arr(*paths: PathNpType) -> Union[np.ndarray, Tuple[np.ndarray]]:
    """
    Convert one or more medical images to numpy arrays based on their file extensions.

    Parameters:
        *paths (Union[str, Path]): Paths to the medical image files or already loaded numpy arrays.

    Returns:
        Union[np.ndarray, Tuple[np.ndarray]]: If a single path is provided, returns the image data as a numpy array.
                                             If multiple paths are provided, returns a tuple of numpy arrays.

    Raises:
        TypeError: If the provided file format is unsupported.
    """

    def load_image_as_array(path: Union[str, Path]) -> np.ndarray:
        if isinstance(path, np.ndarray):
            return path

        path_obj = Path(path)
        if path_obj.suffix in [".nii", ".nii.gz"]:
            return nib.load(path_obj).get_fdata()
        elif path_obj.suffix == ".dcm":
            return dicom.dcmread(path_obj).pixel_array
        elif path_obj.suffix == ".mha":
            sitk_image = sitk.ReadImage(
                str(path_obj)
            )  # SimpleITK python wrapper has no support for pathlib.Path
            return sitk.GetArrayFromImage(sitk_image)
        elif path_obj.suffix == ".npy":
            return np.load(path_obj)
        elif path_obj.suffix == ".npz":
            return np.load(path_obj)["arr_0"]
        else:
            raise TypeError(f"Unsupported file type: {path_obj.suffix}")

    arrays = tuple(load_image_as_array(path) for path in paths)
    if len(arrays) == 1:
        return arrays[0]
    return arrays


def image_preprocess(input, norm: bool):
    if isinstance(input, (str, Path)):
        data = im2arr(input)
    elif isinstance(input, np.ndarray):
        data = input
    else:
        raise ValueError(
            "Unsupported input type. Expected path (str or Path) or numpy ndarray."
        )

    data = data.astype(np.float64)

    if norm:
        min_value = np.min(data)
        max_value = np.max(data)
        data = (data - min_value) / (max_value - min_value)

    return data


def mask_preprocess(input):
    if isinstance(input, (str, Path)):
        data = im2arr(input)
    elif isinstance(input, np.ndarray):
        data = input
    else:
        raise ValueError(
            "Unsupported input type. Expected path (str or Path) or numpy ndarray."
        )

    data = data.astype(np.int8)

    return data


def read_image_mask(
    image: Union[str, Path, np.ndarray],
    mask: Union[str, Path, np.ndarray],
    norm: bool = False,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Read the medical image and mask based on their file extension.

    Parameters:
        image (Union[str, Path, np.ndarray]): Path to the image or image data.
        mask (Union[str, Path, np.ndarray]): Path to the mask or mask data.

    Returns:
        Tuple[numpy.ndarray, numpy.ndarray]: Loaded image and mask as numpy arrays.
    """

    image = image_preprocess(image, norm)
    mask = mask_preprocess(mask)

    if image.shape != mask.shape:
        raise ValueError("Image and mask shape mismatch")

    print("Shape:", image.shape)

    return image, mask
