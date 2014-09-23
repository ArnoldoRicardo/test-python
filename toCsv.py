import vobject
import glob
import sys

vobj=vobject.readOne(open("Nelson.vcf"))
print vobj.contents


def main(args):
    suma = 0
    titulos = ['nombre del archivo', 'Total', 'subtotoal', 'rfc', 'fecha', 'ivaTrasladado', 'isrTrasladado', 'ivaRetenido', 'isrRetenido']
    import csv
    out = csv.writer(open("out.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
    out.writerow(titulos)
    for argument in args:
        t = datos(argument)
        row = []
        if not t["rfcEmisor"] in catedraticos:
            suma += t["total"]
            row.append(argument)
            row.append(t['total'])
            row.append(t['subTotal'])
            row.append(t['rfcEmisor'])
            row.append(t['fecha'])
            row.append(t['ivat'])
            row.append(t['isrt'])
            row.append(t['ivar'])
            row.append(t['isrr'])
            out.writerow(row)

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        main(sys.argv[1:])
    else:
        files = glob.glob("*.xml")
        if files:
            main(files)
        else:
            raw_input("no hay archivos xml")
