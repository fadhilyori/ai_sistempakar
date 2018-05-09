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