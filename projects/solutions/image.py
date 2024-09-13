"""
Simple BMP and PPM image reader and writer

Limitations:
- Only uncompressed BMP
- Only 24 bpp BMP

References:
- http://davis.lbl.gov/Manuals/NETPBM/doc/ppm.html
- https://en.wikipedia.org/wiki/BMP_file_format
- https://docs.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-bitmapv5header
- https://instesre.org/howto/BW_image/ReadingBitmaps.htm
- https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Alone_boy_silhouette_image.jpg/640px-Alone_boy_silhouette_image.jpg
"""

from typing import BinaryIO, List, Optional, Tuple, TypedDict, Union
from pathlib import Path
import struct
import sys


class FileHeader(TypedDict):
    "BMP file header"
    _type: str
    _size: int
    _image_offset: int


class BitmapInfoHeader(TypedDict):
    "One of several possible BMP image headers"
    size: int
    width: int
    height: int
    colour_planes: int
    bpp: int
    compression: int
    image_size: int
    h_resolution: int
    v_resolution: int
    palette_size: int
    important_colours: int


class Image:
    "Generic image data"
    width: int
    height: int
    resolution: Tuple[int, int]
    _pixels: List[Tuple[int, int, int]]

    def __init__(self, width, height, resolution, pixel_data):
        self.width = width
        self.height = height
        self.resolution = resolution
        self._pixels = pixel_data

    def pixels(self):
        "Return a copy of the pixel data"
        return self._pixels.copy()


def file_header(data: bytes) -> FileHeader:
    "Read file header from a valid BMP image"
    return {
        "_type": "".join(
            [x.decode() for x in struct.unpack_from("cc", buffer=data, offset=0)]
        ),
        "_size": struct.unpack_from("i", buffer=data, offset=2)[0],
        "_image_offset": struct.unpack_from("i", buffer=data, offset=10)[0],
    }


def dib_header(data: bytes) -> BitmapInfoHeader:
    """
    Read a DIB header in the BITMAPINFOHEADER format from a valid BMP image.
    Note that this is one of several available header formats.
    """
    return {
        "size": struct.unpack_from("I", buffer=data, offset=14)[0],
        "width": struct.unpack_from("i", buffer=data, offset=18)[0],
        "height": struct.unpack_from("i", buffer=data, offset=22)[0],
        "colour_planes": struct.unpack_from("h", buffer=data, offset=26)[0],
        "bpp": struct.unpack_from("h", buffer=data, offset=28)[0],
        "compression": struct.unpack_from("I", buffer=data, offset=30)[0],
        "image_size": struct.unpack_from("I", buffer=data, offset=34)[0],
        "h_resolution": struct.unpack_from("I", buffer=data, offset=38)[0],
        "v_resolution": struct.unpack_from("I", buffer=data, offset=42)[0],
        "palette_size": struct.unpack_from("I", buffer=data, offset=46)[0],
        "important_colours": struct.unpack_from("I", buffer=data, offset=50)[0],
    }


def pixels(header: BitmapInfoHeader, data: bytes) -> List[Tuple[int, int, int]]:
    """
    Extract pixel data from a valid BMP image.
    `data` MUST be a buffer containing pixel data. Pixel data is read from the
    beginning of this buffer.
    """
    width = header["width"]
    padding = (3 * width) % 4
    pix = []
    offset = 0
    for _ in range(header["height"]):
        buf = data[offset : offset + (3 * width)]
        pix += list(struct.iter_unpack("BBB", buf))
        offset += (3 * width) + padding
    top_to_bottom = list(
        reversed(
            [
                pix[h * header["width"] : (h + 1) * header["width"]]
                for h in range(header["height"])
            ]
        )
    )
    return [
        (int(p[0]), int(p[1]), int(p[2])) for sublist in top_to_bottom for p in sublist
    ]


def save_ppm(img: Image, output: Union[str, Path, BinaryIO]):
    "Save an `Image` into PPM P6 (binary) format"
    if isinstance(output, (str, Path)):
        with open(output, mode="wb") as outf:
            return save_ppm(img, outf)
    else:
        output.write(f"P6\n{img.width} {img.height}\n255\n".encode())
        pixel_data = img.pixels()
        for _h in range(img.height):
            for _w in range(img.width):
                output.write(struct.pack("BBB", *pixel_data[_h * img.width + _w]))
        return img


def read_bmp(infile: Union[str, Path, BinaryIO]) -> Optional[Image]:
    "Load a BMP image file into an `Image`"
    if isinstance(infile, (str, Path)):
        with open(infile, mode="rb") as in_f:
            return read_bmp(in_f)

    else:
        bmp = infile.read()
        header = file_header(bmp)
        dib = dib_header(bmp)

        offset = header["_image_offset"]
        size = dib["image_size"]
        pixel_data = pixels(dib, bmp[offset : offset + size])

        return Image(
            width=dib["width"],
            height=dib["height"],
            resolution=(dib["h_resolution"], dib["v_resolution"]),
            pixel_data=pixel_data,
        )


def save_bmp(img: Image, output: Union[str, Path, BinaryIO]):
    "Save an `Image` into Windows BMP format file"
    if isinstance(output, (str, Path)):
        with open(output, mode="wb") as outf:
            return save_bmp(img, outf)
    else:
        _pix = img.pixels()

        padding = (3 * img.width) % 4
        pixel_data = b"".join(
            reversed(
                [
                    b"".join(
                        [
                            struct.pack("BBB", *p)
                            for p in _pix[h * img.width : (h + 1) * img.width]
                        ]
                    )
                    + struct.pack("x" * padding)
                    for h in range(img.height)
                ]
            )
        )

        # File header
        output.write(
            struct.pack("<ccIhhI", b"B", b"M", 14 + 40 + len(pixel_data), 0, 0, 14 + 40)
        )

        # DIP header (Windows BITMAPINFOHEADER)
        output.write(
            struct.pack(
                "<IiiHHiiiiii",
                40,
                img.width,
                img.height,
                1,
                24,
                0,
                len(pixel_data),
                *img.resolution,
                0,
                0,
            )
        )

        # Pixel data
        output.write(pixel_data)
        return img


if __name__ == "__main__":
    if (myimg := read_bmp(sys.argv[1])) is None:
        print("Failed to load bitmap")
        sys.exit(1)

    if sys.argv[2] == "--ppm":
        with open(sys.argv[3], mode="wb") as ppm_file:
            save_ppm(myimg, ppm_file)

    elif sys.argv[2] == "--bmp":
        with open(sys.argv[3], mode="wb") as bmp_file:
            save_bmp(myimg, bmp_file)
