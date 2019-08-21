
import layouts
import readZipedFile as rzf

def getItems(zipPath, file):
    f = rzf.read_zip_file(zipPath, file)
    p = []
    e = set()
    for l in f:
        if str(l[0:2]).encode("utf-8") == '02':
            o = rzf.decode_line(l, layouts.tip_neg_layout)
            if o['codmer'] == '010':
                e.add(o['codempr'])
                p.append([o['codneg'],o['codempr']])
    return p, e
