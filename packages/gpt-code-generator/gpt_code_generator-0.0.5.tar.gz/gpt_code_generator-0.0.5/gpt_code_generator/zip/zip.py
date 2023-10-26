import shutil


def compress(src_path: str, dst_path: str) -> None:
    shutil.make_archive(dst_path, "zip", src_path)


def decompress(src_path: str, dst_path: str) -> None:
    shutil.unpack_archive(src_path, dst_path)
