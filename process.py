from pathlib import Path

from PIL import Image

# Crop to remove letter boxing
DEFAULT_COORDS = (
    0,  # left
    120,  # top
    0,  # right
    120  # bottom
)

def crop_image(path: Path, saved_location: Path, rel_coords: tuple[int, int, int, int] = DEFAULT_COORDS):
    """
    @param path: path to image
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(path)
    coords = (rel_coords[0], rel_coords[1], image_obj.width - rel_coords[2], image_obj.height - rel_coords[3])
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)


def crop_all(folder: Path, output: Path, glob: str = "*.png"):
    """
    Crop all images in a folder
    @param folder: Path to folder containing images
    @param output: Path to save cropped images
    @param glob: Glob pattern to match
    """
    if not output.exists():
        output.mkdir()
    for ix, image in enumerate(sorted(folder.glob(glob))):
        crop_image(image, (output / f"frame_{ix:03d}").with_suffix(image.suffix))


if __name__ == "__main__":
    crop_all(Path("."), Path("./cropped"))