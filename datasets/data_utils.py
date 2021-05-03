# -*- coding: utf-8 -*-
import os
from urllib import request
import gzip


def download(url, folder=None, filename=None):
    """
    Download url to folder and store with filename

    Parameters
    ----------
    url: Web url of file to be downloaded
    folder: Folder where to store, default is '.'
    filename: Filename of the downloaded file, default is the last fragment of
        url
    """
    if folder is None:
        folder = '.'
    os.makedirs(folder, exist_ok=True)

    if filename is None:
        filename = os.path.split(url)[-1]

    full_name = os.path.join(folder, filename)
    if not os.path.exists(full_name):
        print("'%s' does NOT exist, downloading from %s" %
              (filename, url))
        request.urlretrieve(url, full_name)


def get_filenames_from_urls(urls):
    """
    Get filenames from urls by extracting the last fragment of each url

    Parameters
    ----------
    urls: Web urls, dict type

    Returns
    -------
    filenames: Filenames obtained from urls, dict type
    """
    filenames = {}
    for name in urls.keys():
        url = urls.get(name)
        filenames[name] = os.path.split(url)[-1]
    return filenames


def extract_gz(gz_path, folder=None, decompressed_filename=None):
    """
    Extract gzip (.gz) file

    Parameters
    ----------
    gz_path: Path of .gz file
    folder: Folder where to decompress .gz file, default is the same folder as
        gz_path
    decompressed_filename: The filename of decompressed .gz file
    """
    if folder is None:
        folder = os.path.split(gz_path)[0]
    os.makedirs(folder, exist_ok=True)

    if decompressed_filename is None:
        decompressed_filename = gz_path.replace('.gz', '')

    decompressed_path = os.path.join(folder, decompressed_filename)
    print("extract '%s' to get '%s'" % (gz_path, decompressed_path))
    with gzip.GzipFile(gz_path) as gz_file:
        open(decompressed_path, "wb+").write(gz_file.read())