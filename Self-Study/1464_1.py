def sol():
    M = max(R, G, B)
    m = min(R, G, B)
    V = M
    S = 255 * ((V - m) / V)

    if V == R:
        H = (60 * (G - B)) / (V - m)
    elif V == G:
        H = 120 + 60 * (B - R) / (V - m)
    elif V == B:
        H = 240 + 60 * (R - G) / (V - m)

    if H < 0:
        H += 360

    return (hlo <= H <= hhi) and (slo <= S <= shi) and (vlo <= V <= vhi)


hlo, hhi = map(int, input().split())
slo, shi = map(int, input().split())
vlo, vhi = map(int, input().split())
R, G, B = map(int, input().split())

print("Lumi will like it." if sol() else "Lumi will not like it.")
