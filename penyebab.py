class Penyebab:

    def __init__(self, id, nama, penyakit):
        self.id = id
        self.nama = nama
        self.penyakit = penyakit

    def __repr__(self):
        return repr(self.getPresentase())

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