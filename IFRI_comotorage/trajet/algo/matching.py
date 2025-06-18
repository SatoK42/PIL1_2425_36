import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    lat1, lon1, lat2, lon2 = map(math.radians, (lat1, lon1, lat2, lon2))
    dlat, dlon = lat2 - lat1, lon2 - lon1
    return 2 * math.asin(math.sqrt(math.sin(dlat/2)**2 +
                                    math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2)) * R

def route_dist(a, b):
    return haversine(a["latitude"], a["longitude"],
                     b["latitude"], b["longitude"]) * 1.3

def horaire_ok(a, b, marge=30):
    return abs(a["heure_depart"] - b["heure_depart"]) <= marge

def overlap_score(a, b):
    d = route_dist(a, b)
    return max(0, min(d, d*0.8) / (d + 1))

def score_match(d, p):
    if not horaire_ok(d, p): return None
    dkm = route_dist(d, p)
    if dkm > 8: return None
    sc = max(0, 40 - dkm*5)
    sc += overlap_score(d, p) * 30
    sc += max(0, 20 - abs(d["heure_depart"] - p["heure_depart"]) / 2)
    sc += 10  # bonus véhicule / fit
    return sc

def gale_shapley(drivers, passengers):
    # on suppose chaque dict a 'id'
    names_d = [d["id"] for d in drivers]
    names_p = [p["id"] for p in passengers]
    # construire prefs_d: liste d’IDs triés par score
    prefs_d = {}
    for d in drivers:
        prefs = []
        for p in passengers:
            sc = score_match(d, p)
            if sc is not None:
                prefs.append((p, sc))
        prefs.sort(key=lambda x: x[1], reverse=True)
        prefs_d[d["id"]] = [p["id"] for p, _ in prefs]
    prefs_p = {}
    for p in passengers:
        prefs = []
        for d in drivers:
            sc = score_match(d, p)
            if sc is not None:
                prefs.append((d, sc))
        prefs.sort(key=lambda x: x[1], reverse=True)
        prefs_p[p["id"]] = [d["id"] for d, _ in prefs]
    free = names_d[:]
    engaged = {}
    next_prop = {m: 0 for m in names_d}
    while free:
        m = free.pop(0)
        if next_prop[m] >= len(prefs_d[m]):
            continue
        w = prefs_d[m][next_prop[m]]
        next_prop[m] += 1
        current = next((x for x,y in engaged.items() if y == w), None)
        if current is None:
            engaged[m] = w
        else:
            if prefs_p[w].index(m) < prefs_p[w].index(current):
                engaged.pop(current)
                engaged[m] = w
                free.append(current)
            else:
                free.append(m)
    return engaged

# Les préférences (prefs_d, prefs_p) sont construites dynamiquement dans la vue,
# donc on ne les définit pas ici.
# matches = gale_shapley(prefs_d, prefs_p)
# print("🤖 Résultats du matching stable :")
# for d,p in matches.items():
#     sc = score_match(next(x for x in drivers if x["nom"]==d), next(x for x in passengers if x["nom"]==p))
#     print(f"{d} → {p} (score = {sc:.1f})")