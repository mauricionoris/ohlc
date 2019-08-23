import zipfile as z

def read_zip_file(zippath, filename):
    with z.ZipFile(zippath) as myzip:
        with myzip.open(filename, mode='r') as myfile:
            content = myfile.read().decode('latin-1')
            return content.splitlines()


def decode_line(line, layout):

    obj = {}
    for k, v in layout.items():
        obj[k] = line[v['start']-1:v['end']].strip()
    return obj;
