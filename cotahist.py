import datetime as dt
import layouts
import readZipedFile as rzf

def getItems(zipPath, file):
    f = rzf.read_zip_file(zipPath, file)
    p = []
    for l in f:
        if l[0:2] == '01':
            o = rzf.decode_line(l, layouts.cotahist_layout)
            if o['tpmerc'] == '010':
                if o['codbdi'] == '02':
                    p.append([dt.datetime.strptime(o['dtpregao'], '%Y%m%d' ).date(), o['codneg'],o['nomres'], float(o['preult'])/100, int(o['totneg']), int(o['quattot']), float(o['voltot'])/100])
    return p
