import tasks
import repositoryUtils as ru


def pickOption(option):     #u zavisnosti koju opciju izaberemo ,odredjena funkcija se izvrsava(varijabla ima pokazivac na funkciju)
    switcher = {
        0: tasks.exit,
        1: tasks.directorySelection,
      #  4: tasks.wordSearch,
      #  #  5: tasks.printContent,
    }
    func = switcher.get(option, lambda: "pogresna opcija")
    func()
    # Ako smo odabrali izlaz, nasilno izadji i ne pitaj nista
    if option != 0:
        quitOpt = input(" .. press any key to continue ... ")


n = -1  # predefinisana peginacija


def main():
    option = -1
    while option != 0:
        try:
            ru.cls()  # brisanje ekrana
            print("[1] Odabir direktorijuma")
            print("[3] Unesi n za paginaciju") #kolio hocemo rezultata
            print("[4] Pretraga reci ")
            print("[5] Ispisis sadrzaj")
            print("[0] Prekid")

            option = int(input())
            pickOption(option)
        except ValueError:
            print("Unesite neku od ponudjenih opcija:")


main()