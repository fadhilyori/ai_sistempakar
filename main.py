class Penyebab:

    def __init__(self, id, nama, penyakit):
        self.id = id
        self.nama = nama
        self.penyakit = penyakit

    def __repr__(self):
        return repr(str(self.getId()) + ":" + str(self.getPresentase()))

    def getId(self):
        return self.id

    def getNama(self):
        return self.nama

    def getPenyakit(self):
        return self.penyakit

    def setPresentase(self, pre):
        self.presentase = pre

    def getPresentase(self):
        return self.presentase


class Penyakit:

    passed = 0

    def __init__(self, id, nama, gejala):
        self.id = id
        self.nama = nama
        self.gejala = gejala

    def __repr__(self):
        return repr(self.getId())

    def getId(self):
        return self.id

    def getNama(self):
        return self.nama

    def getGejala(self):
        return self.gejala

    def calculateProbabilitas(self, gejala):
        for item in gejala:
            if item in self.gejala:
                self.passed += 1
        self.presentase = self.passed / len(self.gejala)

    def getProb(self):
        return self.presentase

class Gejala:

    def __init__(self, id, nama, text):
        self.id = id
        self.nama = nama
        self.text = text

    def __repr__(self):
        return repr(self.getId() + ":" + self.getNama())

    def getId(self):
        return self.id

    def getNama(self):
        return self.nama

    def getText(self):
        return self.text

def main():
    userAnswerYes = []
    penyebab = [Penyebab(33, "Keracunan Staphylococcus aureus", [20, 21])]
    penyakit = [Penyakit(20, "Mencret", [1, 2, 4, 5]),
                Penyakit(21, "Muntah", [4, 5 ,6])]
    gejala = [Gejala(1, "Buang air besar (Lebih dari 2 kali)", "sering mengalami"),
              Gejala(2, "Berak encer", "mengalami"),
              Gejala(3, "Berak berdarah", "mengalami"),
              Gejala(4, "Lesu dan tidak bergairah", "merasa"),
              Gejala(5, "Tidak selera makan", ""),
              Gejala(6, "Merasa mual dan sering muntah (lebih dari 1 kali", ""),
              Gejala(7, "Merasa sakit di bagian perut", "")]
    # Asking question
    for item in gejala:
        if item.getText() != "":
            question = "Apakah anda " + item.getText() + " " + item.getNama().lower() + " [y/n] ? "
        else:
            question = "Apakah anda " + item.getNama().lower() + " [y/n] ? "
        print(question, end="")
        answer = input()
        if answer.lower() == 'y':
            userAnswerYes.append(item.getId())
    print(userAnswerYes)
    # Calculate probability
    for item in penyakit:
        item.calculateProbabilitas(userAnswerYes)
        # print(item.getProb())
    for item in penyebab:
        penyebabID = item.getPenyakit()
        presentase = []
        for itr in penyakit:
            if itr.getId() in penyebabID:
                presentase.append(itr.getProb())
        total = len(item.getPenyakit())
        curr = 0
        for itr in presentase:
            curr = curr + int(itr)
        presentase = (curr / total) * 100
        item.setPresentase(presentase)
        print(item)

if __name__ == "__main__":
    main()