import risar as r


def narisi_trikotnik(ax, ay, bx, by, cx, cy):
    sirina = 3
    barva = r.nakljucna_barva()
    r.crta(ax, ay, bx, by, sirina=sirina, barva=barva)
    r.crta(bx, by, cx, cy, sirina=sirina, barva=barva)
    r.crta(cx, cy, ax, ay, sirina=sirina, barva=barva)



def razdeli(ax, ay, bx, by, cx, cy):
    abx, aby = (ax + bx) / 2, (ay + by) / 2
    acx, acy = (ax + cx) / 2, (ay + cy) / 2
    bcx, bcy = (bx + cx) / 2, (by + cy) / 2
    narisi_trikotnik(abx, aby, acx, acy, bcx, bcy)

    if bx - ax > 20:
        razdeli(ax, ay, abx, aby, acx, acy)
        razdeli(acx, acy, bcx, bcy, cx, cy)
        razdeli(abx, aby, bx, by, bcx, bcy)



ax, ay = 10, 475
bx, by = 537, 475
cx, cy = 271, 10

narisi_trikotnik(ax, ay, bx, by, cx, cy)
razdeli(ax, ay, bx, by, cx, cy)
r.stoj()