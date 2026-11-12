SOGLIA_ORE = 800
aeromobili = [
    {"codice": "I-ABC", "modello": "A320", "ore_volo": 1240, "controlli_ok": True},
    {"codice": "I-DEF", "modello": "B737", "ore_volo": 860, "controlli_ok": False},
    {"codice": "I-GHI", "modello": "A220", "ore_volo": 1035, "controlli_ok": True},
    {"codice": "I-JKL", "modello": "ATR72", "ore_volo": 540, "controlli_ok": True},
]

def stampa_riepilgo() -> None:
    print("Elenco dei veicoli disponibili: ")
    for i in range(0, aeromobili.count):
        veicolo = aeromobili[i]
        print(f"Veicolo {i}:"
              f"Codice: {veicolo["codice"]}"
              f"Modello: {veicolo["modello"]}"
              f"Ore di volo: {veicolo["ore_volo"]}"
              f"Controlli(Ok): {veicolo["controlli_ok"]}")



