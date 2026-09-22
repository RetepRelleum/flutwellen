import glob
from qgis.core import QgsPolygon, QgsLineString, QgsGeometry
from .Layer import DgmL


class Dgm:
    def __init__(self, path, iface):
        pata = glob.glob(path + '/swiss*.tif')
        dgm = DgmL('Perimeter')
        geom = None
        for pat in pata:
            fa = pat.split('_')
            x = int(fa[2].split('-')[0]) * 1000
            y = int(fa[2].split('-')[1]) * 1000
            xa = [x, x + 1000, x + 1000, x]
            ya = [y, y, y + 1000, y + 1000]
            line = QgsLineString(xa, ya)
            pol = QgsPolygon(line)
            if geom is None:
                geom = QgsGeometry(pol)
            else:
                geom = geom.combine(QgsGeometry(pol))
        if geom is None:
            return
        dgm.insertData(geom)
        dgm.dgm.selectAll()
        mCanvas = iface.mapCanvas()
        mCanvas.zoomToSelected(dgm.dgm)
        dgm.dgm.removeSelection()
