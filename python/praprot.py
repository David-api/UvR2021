import risar as r
import random

trnaformacije = [
    (0, 0, 0, 0.16, 0, 0, 0.01),
    (0.85, 0.04, -0.04, 0.85, 0, 1.60, 0.85),
    (0.20, -0.26, 0.23, 0.22, 0, 1.60, 0.07),
    (-0.15, 0.28, 0.26, 0.24, 0, 0.44, 0.07)
]

x = 0
y = 0

for i in range(10000):
    nak = random.random()
    for a, b, c, d, e, f, p in trnaformacije:
        nak -= p
        if nak < 0:
            x = a * x + b * y + e
            y = c * x + d * y + f
            barva = r.nakljucna_barva()
            sirina = random.randint(1,3)
            r.tocka(x * 45 + r.maxx / 2, r.maxY - y * 45, barva=barva, sirina=sirina)
            break

r.stoj()
