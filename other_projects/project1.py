import colorama
colorama.init(autoreset= True)

BLUE = colorama.Fore.BLUE
RED = colorama.Fore.RED
GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW
MAGENTA = colorama.Fore.MAGENTA
CYAN = colorama.Fore.CYAN


print(f"{BLUE}Ти охоронець наукового центру Чорна Меза.\n")
print(f"{BLUE}Ти стоїш на блокпості зі своїм напарником...\n")
print(f"{BLUE}Раптом вибухи. Ти втрачаєш свідомість...\n")

print(f"{BLUE}Ти прокидаєшся. Поруч Glock-17.\n")
print(f"{BLUE}На напарнику сидить хедкраб...\n")

while True:
    print(f"\n{RED}1. Взяти його автомат і бігти на склад")
    print(f"{GREEN}2. Втекти без зброї")
    print(f"{YELLOW}3. Вистрілити напарнику в голову")

    choice = input(f"{MAGENTA}Введи цифри від одного до трьох: ")

    if choice == "1":
        print(f"\n{BLUE}Ти добіг до збройового складу...\n")
        break

    elif choice == "2":
        print(f"{RED}Ти втік без зброї, тебе швидко знайшли та розстліляли на місці.")
        exit()

    elif choice == "3":
        print(f"{RED}Ти вбив напарника, сзаді підійшов хед-краб та запригнув тобі на голову, тепер ти зомбі.")
        exit()

    else:
        print(f"{CYAN}Ти щось не те ввів, введи число бляха.")


while True:
    print(f"\n{BLUE}На складі стоїть військовий HECU.\n")

    print(f"{RED}1. Вистрілити і забрати зброю")
    print(f"{GREEN}2. Зламати шию")
    print(f"{YELLOW}3. Самогубство")

    choice = input(f"{MAGENTA}Вибір від одного до трьох: ")

    if choice == "1":
        print(f"{BLUE}Ти вбив його і забрав зброю.\n")
        break

    elif choice == "2":
        print(f"{BLUE}Тихо усунув і забрав зброю.\n")
        break

    elif choice == "3":
        print(f"{RED}Ти помер. Game Over.")
        exit()

    else:
        print(f"{CYAN}Ти щось не те ввів, введи число бляха. ")


while True:
    print(f"\n{BLUE}Сирени виють. Комплекс заражений.\n")

    print(f"{RED}1. Прориватися до виходу")
    print(f"{GREEN}2. Шукати виживших")
    print(f"{YELLOW}3. Сховатися у мінному полі.")

    choice = input(f"{MAGENTA}Вибір: ")

    if choice == "1":
        print(f"\n{CYAN}Ти прорвався крізь хаос та ти вижив, мои апладіраванія :)\n")
        break

    elif choice == "2":
        print(f"{RED}Виживших немає на вулиці, тебе знайшли солдати та вбили.")
        exit()

    elif choice == "3":
        print(f"{RED}Ти попитався у ньому сховатися але тебе похітив невідомий у фіолетовому костюмі з галстуком. ")
        exit()

    else:
        print(f"{CYAN}Ти щось не те ввів, введи число бляха.")