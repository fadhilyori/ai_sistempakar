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