from penyakit import Penyakit
from penyebab import Penyebab
from gejala import Gejala

def main():
    userAnswerYes = []
    # define list 
    penyebab = [Penyebab(33, "Keracunan staphylococcus aureus", [20, 21, 22, 23, 29]), 
                Penyebab(34, "Keracunan jamur beracun", [20, 21, 22, 24, 30]),
                Penyebab(35, "Keracunan salmonellae", [20, 21, 22, 25, 26, 29]),
                Penyebab(36, "Keracunan clostridium botulinum", [21, 27, 31]),
                Penyebab(37, "Keracunan campylobacter", [28, 22, 25, 32])]
    penyakit = [Penyakit(20, "Mencret", [1, 2, 4, 5]),
                Penyakit(21, "Muntah", [4, 5 ,6]),
                Penyakit(22, "Sakit perut", [4, 7]),
                Penyakit(23, "Darah rendah", [4, 8, 9]),
                Penyakit(24, "Koma", [8, 10]),
                Penyakit(25, "Demam", [4, 5, 9, 11]),
                Penyakit(26, "Septicaemia", [4, 8, 11, 12]),
                Penyakit(27, "Lumpuh", [4, 13]),
                Penyakit(28, "Mencret berdarah", [1, 2, 3, 4, 5]),
                Penyakit(29, "Makan daging", [14, 15]),
                Penyakit(30, "Makan jamur", [14, 16]),
                Penyakit(31, "Makan makanan kaleng", [14, 17]),
                Penyakit(32, "Minum susu", [18, 19])]
    gejala = [Gejala(1, "Buang air besar (Lebih dari 2 kali)", "sering mengalami"),
              Gejala(2, "Berak encer", "mengalami"),
              Gejala(3, "Berak berdarah", "mengalami"),
              Gejala(4, "Lesu dan tidak bergairah", "merasa"),
              Gejala(5, "Tidak selera makan", ""),
              Gejala(6, "Merasa mual dan sering muntah (lebih dari 1 kali", ""),
              Gejala(7, "Merasa sakit di bagian perut", ""),
              Gejala(8, "Tekanan darah rendah", "memiliki"),
              Gejala(9, "Pusing", "merasa"),
              Gejala(10, "Pingsan", "mengalami"),
              Gejala(11, "Suhu badan tinggi", "mengalami"),
              Gejala(12, "Luka di bagian tertentu", "mengalami"),
              Gejala(13, "Tidak dapat menggerakkan anggota badan tertentu", ""),
              Gejala(14, "Memakan sesuatu", "pernah"),
              Gejala(15, "Memakan daging", ""),
              Gejala(16, "Memakan jamur", ""),
              Gejala(17, "Memakan makanan kaleng", ""),
              Gejala(18, "Membeli susu", ""),
              Gejala(19, "Meminum susu", "")]

    # Asking question
    nomor = 1
    for item in gejala:
        if item.getText() != "":
            question = str(nomor) + ". Apakah anda " + item.getText() + " " + item.getNama().lower() + " [y/n] ? "
        else:
            question = str(nomor) + ". Apakah anda " + item.getNama().lower() + " [y/n] ? "
        nomor += 1
        print(question, end="")
        answer = input()
        if answer.lower() == 'y' or answer == None or answer == "":
            userAnswerYes.append(item.getId())

    # Menghitung persentase kemungkinan penyakit
    for item in penyakit:
        item.calculateProbabilitas(userAnswerYes)

    # Meghitung persentase kemungkinan penyebab
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
        print(item.getNama() + " : " + str(int(item.getPresentase())) + "%")
        
    # Penentuan hasil
    thresholdValue = 80 # %
    kemungkinanPenyebab = []
    highest = 0
    for item in penyebab:
        if item.getPresentase() >= thresholdValue:
            kemungkinanPenyebab.append(item)
        if item.getPresentase() > highest:
            highest = item.getPresentase()
    if len(kemungkinanPenyebab) == 0:
        print("Anda sehat dan tidak terindikasi penyakit apapun")
    else:
        for item in kemungkinanPenyebab:
            if item.getPresentase() == highest:
                hasil = item
        print("Anda terkena " + hasil.getNama() + ", dengan kemungkinan : " + str(int(hasil.getPresentase())) + "%")
    
if __name__ == "__main__":
    main()