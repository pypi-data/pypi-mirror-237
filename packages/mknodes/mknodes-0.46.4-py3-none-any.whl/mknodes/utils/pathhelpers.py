from __future__ import annotations

from collections.abc import Mapping
import functools
import os
import pathlib
import posixpath
import shutil

from mknodes.utils import log


logger = log.get_logger(__name__)


def copy(
    source_path: str | os.PathLike,
    output_path: str | os.PathLike,
    exist_ok: bool = True,
):
    """Copy source_path to output_path, making sure any parent directories exist.

    The output_path may be a directory.

    Arguments:
        source_path: File to copy
        output_path: path where file should get copied to.
        exist_ok: Whether exception should be raised in case stuff would get overwritten
    """
    output_path = pathlib.Path(output_path)
    source_path = pathlib.Path(source_path)
    output_path.parent.mkdir(parents=True, exist_ok=exist_ok)
    if source_path.is_dir():
        if output_path.is_dir():
            msg = "Cannot copy folder to file!"
            raise RuntimeError(msg)
        shutil.copytree(source_path, output_path, dirs_exist_ok=exist_ok)
    else:
        if output_path.is_dir():
            output_path = output_path / source_path.name
        shutil.copyfile(source_path, output_path)


def write_file(content: str | bytes, output_path: str | os.PathLike):
    """Write content to output_path, making sure any parent directories exist.

    Arguments:
        content: Content to write
        output_path: path where file should get written to.
    """
    output_path = pathlib.Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    mode = "wb" if isinstance(content, bytes) else "w"
    encoding = None if "b" in mode else "utf-8"
    with output_path.open(mode=mode, encoding=encoding) as f:
        f.write(content)


def write_files(mapping: Mapping[str | os.PathLike, str | bytes]):
    """Write a mapping of filename-to-content to disk.

    Arguments:
        mapping: {"path/to/file.ext": b"content", ...} - style mapping
    """
    for k, v in mapping.items():
        write_file(v, k)


def find_file_in_folder_or_parent(
    filename: str | pathlib.Path,
    folder: os.PathLike | str = ".",
) -> pathlib.Path | None:
    """Search for a file with given name in folder and its parent folders.

    Arguments:
        filename: File to search
        folder: Folder to start searching from
    """
    path = pathlib.Path(folder).absolute()
    while not (path / filename).exists() and len(path.parts) > 1:
        path = path.parent
    return file if (file := (path / filename)).exists() else None


@functools.cache
def load_file_cached(path: str | os.PathLike) -> str:
    if "://" in str(path):
        return fsspec_get(str(path))
    return pathlib.Path(path).read_text(encoding="utf-8")


def download_from_github(
    org: str,
    repo: str,
    path: str | os.PathLike,
    destination: str | os.PathLike,
    username=None,
    token=None,
    recursive: bool = False,
):
    import fsspec

    token = token or os.environ.get("GITHUB_TOKEN")
    if token and not username:
        token = None
    destination = pathlib.Path(destination)
    destination.mkdir(exist_ok=True, parents=True)
    fs = fsspec.filesystem("github", org=org, repo=repo)
    logger.info("Copying files from Github: %s", path)
    fs.get(fs.ls(str(path)), destination.as_posix(), recursive=recursive)


@functools.cache
def fsspec_get(path: str) -> str:
    import fsspec

    with fsspec.open(path) as file:
        return file.read().decode()


@functools.lru_cache
def _get_norm_url(path: str) -> tuple[str, int]:
    from urllib.parse import urlsplit

    if not path:
        path = "."
    elif "\\" in path:
        logger.warning(
            "Path %r uses OS-specific separator '\\'. "
            "That will be unsupported in a future release. Please change it to '/'.",
            path,
        )
        path = path.replace("\\", "/")
    # Allow links to be fully qualified URLs
    parsed = urlsplit(path)
    if parsed.scheme or parsed.netloc or path.startswith(("/", "#")):
        return path, -1

    # Relative path - preserve information about it
    norm = posixpath.normpath(path) + "/"
    relative_level = 0
    while norm.startswith("../", relative_level * 3):
        relative_level += 1
    return path, relative_level


def normalize_url(path: str, url: str | None = None, base: str = "") -> str:
    """Return a URL relative to the given page or using the base."""
    path, relative_level = _get_norm_url(path)
    if relative_level == -1:
        return path
    if url is not None:
        result = relative_url(url, path)
        if relative_level > 0:
            result = "../" * relative_level + result
        return result

    return posixpath.join(base, path)


def relative_url(url_a: str, url_b: str) -> str:
    """Compute the relative path from URL A to URL B.

    Arguments:
        url_a: URL A.
        url_b: URL B.

    Returns:
        The relative URL to go from A to B.
    """
    parts_a = url_a.split("/")
    if "#" in url_b:
        url_b, anchor = url_b.split("#", 1)
    else:
        anchor = None
    parts_b = url_b.split("/")

    # remove common left parts
    while parts_a and parts_b and parts_a[0] == parts_b[0]:
        parts_a.pop(0)
        parts_b.pop(0)

    # go up as many times as remaining a parts' depth
    levels = len(parts_a) - 1
    parts_relative = [".."] * levels + parts_b
    relative = "/".join(parts_relative)
    return f"{relative}#{anchor}" if anchor else relative


if __name__ == "__main__":
    file = download_from_github("phil65", "mknodes", "mknodes", "testus/")
    print(file)
