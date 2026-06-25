from text_game import QUESTS, BLUE, RED, GREEN, CYAN, MAGENTA

print(BLUE + "Ти охоронець на науковому комплексі Чорна Меза.")
print(BLUE + "Ти стоїш на блок-пості зі своїм напарником Олексієм.")
print(BLUE + "Раптом лунає потужний вибух, який накриває все навкруги, та ти відключаєшся.\n")

scene = "start"

while scene != "game_over":

    print(QUESTS[scene]["text"])

    for i in QUESTS[scene]["choises"]:
        print(QUESTS[scene]["choises"][i])

    answer = input(f"{MAGENTA}Вибір від одного до трьох: \n")

    if answer == "1":
        action = QUESTS[scene]["actions"]["1"]
        target = QUESTS[scene]["trans"]["1"]

    elif answer == "2":
        action = QUESTS[scene]["actions"]["2"]
        target = QUESTS[scene]["trans"]["2"]

    elif answer == "3":
        action = QUESTS[scene]["actions"]["3"]
        target = QUESTS[scene]["trans"]["3"]

    else:
        print(f"{MAGENTA}\nЯкщо не напишеш числа від одного до трьох - до тебе прийде домой доктор фрікмен.\n")
        continue

    if action == "next_def":
        scene = target

    elif action == "death":
        print(f"{RED}{target}" )
        print(f"{RED} ТИ ПРОГРАВ!!! :DDD" )
        scene = "game_over"

    elif action == "win":
        print(f"{GREEN}{target}" )
        print(f"{GREEN} ТИ ВИГРАВ У МОЄЙ ГРІ!!! ;DDD" )
        scene = "game_over"