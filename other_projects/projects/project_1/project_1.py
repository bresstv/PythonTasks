from text_game import QUESTS, BLUE, RED, GREEN, CYAN, MAGENTA

print(BLUE + "Ти охоронець на науковому комплексі Чорна Меза.")
print(BLUE + "Ти стоїш на блок-пості зі своїм напарником Олексієм.")
print(BLUE + "Раптом лунає потужний вибух, який накриває все навкруги, та ти відключаєшся.\n")

scene = "start"

while scene != "game_over":

    print(QUESTS[scene]["text"])

    for i in QUESTS[scene]["choises"]:
        print(QUESTS[scene]["choises"][i])

    answer = input("Вибір: ")

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
        print("Я не зрозумів.")
        continue

    if action == "next_def":
        scene = target

    elif action == "death":
        print(RED + target)
        print(RED + "ГЕЙМ ОВЕР!!!")
        scene = "game_over"

    elif action == "win":
        print(GREEN + target)
        print(GREEN + "ПЕРЕМОГА!")
        scene = "game_over"