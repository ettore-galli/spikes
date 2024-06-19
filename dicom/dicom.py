from PIL import Image
import pydicom
import numpy as np


def convert_dicom(source: str, target: str):
    ds = pydicom.dcmread(source)

    new_image = ds.pixel_array.astype(float)

    scaled_image = (np.maximum(new_image, 0) / new_image.max()) * 255.0

    scaled_image = np.uint8(scaled_image)

    final_image = Image.fromarray(scaled_image)

    final_image.save(target)
    final_image.show()


if __name__ == "__main__":
    source_name = "00001"
    source = f"source/{source_name}"
    target = f"target/{source_name}.jpg"

    convert_dicom(source=source, target=target)
