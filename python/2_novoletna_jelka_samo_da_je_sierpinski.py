from random import choice, randint
import risar as r

#ogljisca trikotnika
ax, ay = 10, 475
bx, by = 537, 475
cx, cy = 271, 10
tocke = [(ax, ay), (bx, by), (cx, cy)]


#risanje jelke, ki pa ni... je sierpinski trikotnik
x, y = 100, 200
for i in range(10000):
    dx, dy = choice(tocke)
    x, y = (x + dx) / 2, (y + dy) / 2
    barva = r.nakljucna_barva()
    sirina = randint(1, 3)
    r.tocka(x, y, barva=barva, sirina=sirina) # malo sem dodelal risarja


r.stoj()