from copy import deepcopy
from beepy import beep
from colored import fg, bg, attr
import re

replacements = [("Al", "ThF"), ("Al", "ThRnFAr"), ("B", "BCa"), ("B", "TiB"), ("B", "TiRnFAr"), ("Ca", "CaCa"), ("Ca", "PB"), ("Ca", "PRnFAr"), ("Ca", "SiRnFYFAr"), ("Ca", "SiRnMgAr"), ("Ca", "SiTh"), ("F", "CaF"), ("F", "PMg"), ("F", "SiAl"), ("H", "CRnAlAr"), ("H", "CRnFYFYFAr"), ("H", "CRnFYMgAr"), ("H", "CRnMgYFAr"), ("H", "HCa"), ("H", "NRnFYFAr"), ("H", "NRnMgAr"), ("H", "NTh"), ("H", "OB"), ("H", "ORnFAr"), ("Mg", "BF"), ("Mg", "TiMg"), ("N", "CRnFAr"), ("N", "HSi"), ("O", "CRnFYFAr"), ("O", "CRnMgAr"), ("O", "HP"), ("O", "NRnFAr"), ("O", "OTi"), ("P", "CaP"), ("P", "PTi"), ("P", "SiRnFAr"), ("Si", "CaSi"), ("Th", "ThCa"), ("Ti", "BP"), ("Ti", "TiTi"), ("e", "HF"), ("e", "NAl"), ("e", "OMg")]

molecule = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"

#replacements = [('H','HO'),('H','OH'),('O','HH')]

#molecule = "HOHOHO"

def solution():

    molecules = []

    for replacement in replacements:
        found = [(r.start(), r.end()) for r in re.finditer(replacement[0], molecule)]
        for s,e in found:
            new_molecule = molecule[:s] + replacement[1] + molecule[e:]
            if new_molecule not in molecules:
                molecules.append(new_molecule)

    for m in molecules:
        print(m)
    print(len(molecules))

    beep(sound=5)

solution()
