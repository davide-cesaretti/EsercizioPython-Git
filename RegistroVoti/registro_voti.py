from typing import List


class Voto:
    def __init__(self, value: float):
        self.value = value


class Registro:
    def __init__(self, voti: List[Voto] = None):
        self.voti = voti if voti is not None else []

    def __str__(self) -> str:
        voti = ""
        for voto in self.voti:
            voti += f"{voto.value} "
        return voti

    def AggiungiVoto(self, voto: Voto) -> None:
        self.voti.append(voto)

    def Media(self) -> float:
        if not self.voti:
            return 0.0
        somma = 0.0
        for voto in self.voti:
            somma += voto.value
        return somma / len(self.voti)

    def RimuoviUltimo(self) -> None:
        if self.voti:
            self.voti.pop()

    def VotoPerPosizione(self, indice: int) -> Voto:
        return self.voti[indice]

#RIGHE DI CODICE MALEVOLOO
if __name__ == "__main__":

    registro = Registro()
    while True:
        print("1) Aggiungi voto\n"
              "2) Media\n"
              "3) Rimuovi ultimo\n"
              "4) Indica la posizione di un voto" \
              "5) Mostra voti")

        risposta = input()
        if risposta == "1":
            print("inserire un nuovo voto")
            voto = float(input())
            registro.AggiungiVoto(voto=Voto(voto))

        elif risposta == "2":
            print(f"{registro.Media()}")

        elif risposta == "3":
            registro.RimuoviUltimo()

        elif risposta == "4":
            print("inserisci posizione: ")
            indice = int(input())
            print(registro.VotoPerPosizione(indice=indice).value)
        elif risposta == "5":
            print(registro)
        else:
            print("scelta non valida")