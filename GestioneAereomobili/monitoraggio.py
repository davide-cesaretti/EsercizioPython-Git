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

def filtra_controlli_non_validi(aeromobili):
    return [
        veicolo for veicolo in aeromobili if aeromobili["controlli_ok"] is False
    ]

def filtra_oltre_soglia(aereomobili, soglia):
    return[
        veicolo
        for veicolo in aereomobili
        if aereomobili["ore_volo"] > soglia
    ]

if __name__ == "__main__":
    stampa_riepilgo()
    filtrati_per_controllo = filtra_controlli_non_validi(aeromobili)
    filtra_per_ore_soglia = filtra_oltre_soglia(aeromobili, SOGLIA_ORE)

    print("====FILTRATI PER CONTROLLI NON VALIDI====")
    for item in filtrati_per_controllo:
        print(f"Codice: {item["codice"]}")

    print("====FILTRATI PER SOGLIA ORE====")
    for item in filtrati_per_controllo:
            print(f"Codice: {item["codice"]}")
    


