from text_game import QUESTS, BLUE, RED, GREEN, CYAN, MAGENTA

def play_game():
    print(f"{BLUE}Ти охоронець на науковому комплексі Чорна Меза.")
    print(f"{BLUE}Ти стоїш на блок-пості зі своїм напарником Олексієм.")
    print(f"{BLUE}Раптом лунає потужний вибух, який накриває все навкруги, та ти відключаєшся.\n")
    print("-" * 50)
    
    current_scene = "start"
    
    while current_scene in QUESTS:
        scene = QUESTS[current_scene]
        
        print(scene["text"])
        print()
        
        for option_text in scene["choises"].values():
            print(option_text)
            
        user_input = ""
        while user_input not in scene["choises"]:
            user_input = input(f"{MAGENTA}Введи число від 1 до 3: ").strip()
            if user_input not in scene["choises"]:
                print(f"{MAGENTA}\nТи ввів щось не те, спробуй ще раз бляха!\n")
        
        action_type = scene["actions"][user_input]
        target = scene["trans"][user_input]
        
        print("-" * 50)
        
        if action_type == "next_def":
            current_scene = target   
            
        elif action_type == "death":
            print(f"{RED}\n{target}")
            print(f"{RED} ГРА ЗАКІНЧЕНА ")
            current_scene = "game_over"  
            
        elif action_type == "win":
            print(f"{CYAN}\n{target}")
            print(f"{GREEN} ВІТАЄМО З ПЕРЕМОГОЮ! ")
            current_scene = "game_over"  

if __name__ == "__main__":
    play_game()