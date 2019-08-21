import zipfile as z
def read_zip_file(zippath, filename):
    with z.ZipFile(zippath) as myzip:
        with myzip.open(filename, mode='r') as myfile:
            return myfile.read().splitlines()


def decode_line(line, layout):

    obj = {}
    for k, v in layout.items():
        obj[k] = str(line[v['start']-1:v['end']]).encode("utf-8").strip()
    return obj;
