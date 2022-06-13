extras = {
    "hyperhacker": ["human", "gravity"],
    "replit": ["human", "human", "human"]
}

materials = {
    "steam": ["fire", "water"],
    "mud": ["water", "dirt"],
    "cloud": ["steam", "air"],
    "brick": ["fire", "mud"],
    "wall": ["brick", "brick"],
    "house": ["wall", "wall"],
    "village": ["house", "house"],
    "city": ["village", "village"],
    "lava": ["fire", "brick"],
    "rock": ["lava", "water"],
    "country": ["city", "city", "city"],
    "continent": ["country", "country", "country"],
    "planet": ["continent", "continent", "continent"],
    "energy": ["fire", "steam"],
    "tornado": ["cloud", "cloud", "energy"],
    "star": ["energy", "energy", "fire"],
    "solar system": ["planet", "planet", "star"],
    "planetquake": ["energy", "energy", "planet"],
    "gravity": ["energy", "dirt"],
    "blackhole": ["gravity", "gravity", "gravity"],
    "moon": ["gravity", "rock"],
    "meteor": ["rock", "rock"],
    "life": ["energy", "water"],
    "neutron": ["energy", "gravity"],
    "proton": ["energy", "energy"],
    "electron": ["energy", "energy", "energy"],
    "atom": ["neutron", "electron", "proton"],
    "molecule": ["atom", "atom"],
    "cell": ["molecule", "molecule"],
    "human": ["cell", "cell", "cell"],
    "plant": ["life", "water"],
    "tree": ["plant", "water"],
    "forest": ["tree", "water"],
    "fire tornado": ["fire", "tornado"],
    "explosion": ["fire tornado", "tornado"],
    "nebula": ["explosion", "star"],
    "neutron star": ["nebula", "gravity"],
    "time": ["blackhole", "gravity"],
    "robot": ["time", "human"],
    "raid": ["robot", "city"],
    "solar system raid": ["raid", "solar system"]
}

items = {**extras, **materials}