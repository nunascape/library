import math
R=100.0; S=R*math.sqrt(2)
TILE=("M -70.711 70.711 A 100 100 0 1 1 70.711 70.711 "
      "A 100 100 0 0 0 70.711 212.132 A 100 100 0 0 0 -70.711 212.132 "
      "A 100 100 0 0 0 -70.711 70.711 Z")
ARR={'A':('D',0),'B':('G',90),'C':('G',0),'D':('I',90),
     'E':('K',180),'F':('K',270),'G':('K',0),'H':('M',270),
     'I':('M',0),'J':('M',90),'K':('J',0),'L':('J',90),
     'M':('J',180),'N':('H',270),'O':('F',0),'P':('F',270)}
HUB={'D':(0,-2*S),'F':(-S,-S),'G':(S,-S),'H':(-2*S,0),'I':(2*S,0),
     'J':(-S,S),'K':(S,S),'M':(0,2*S)}
KEY={'A':['B','P'],'B':['A','C','P'],'C':['B','D','E'],'D':['C','E'],
 'E':['C','D','F','G'],'F':['E','G'],'G':['E','F','H'],'H':['G','I','J'],
 'I':['H','J'],'J':['H','I','K'],'K':['J','L','M'],'L':['K','M'],
 'M':['K','L','N','O'],'N':['M','O'],'O':['M','N','P'],'P':['A','B','O']}
L=list(ARR); VB="-395 -400 790 940"

def symbol(code, cls="nb-sym"):
    p=[f'<path class="hub" d="{TILE}"/>']
    for ch in code:
        c,rot=ARR[ch]; hx,hy=HUB[c]
        p.append(f'<path class="on" d="{TILE}" transform="translate({hx:.3f} {hy:.3f}) rotate({rot})"/>')
    lab=("Combination "+code) if code else "The empty combination"
    return f'<svg class="{cls}" viewBox="{VB}" role="img" aria-label="{lab}">'+"".join(p)+'</svg>'

import itertools
def by_size():
    out={k:[] for k in range(1,7)}
    for k in range(1,7):
        for cs in itertools.combinations(L,k):
            if all(b not in KEY[a] for a,b in itertools.combinations(cs,2)):
                out[k].append("".join(cs))
    return out

def tessellation(k=0.2):
    """Nuna tiling as hairline outlines, scaled by k for use as a header texture."""
    W=2*S*k; H=2*S*k
    t=[]
    for i in range(-4,7):
        for j in range(-4,7):
            if (i+j)%2: continue
            x,y=i*S, j*S
            tone="a" if i%2==0 else "b"
            t.append(f'<path class="t{tone}" d="{TILE}" transform="translate({x:.2f} {y:.2f})"/>')
    body=f'<g transform="scale({k})">'+"".join(t)+'</g>'
    return W,H,body
