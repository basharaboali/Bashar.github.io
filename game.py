import random

# بيانات اللاعب
data = {"gold": 0, "soldiers": 10, "hero_level": 1}

def start_battle():
    current_s = data["soldiers"]
    level = 1
    print(f"\n🚀 انطلقت المعركة! القوة الأساسية: {current_s}")
    
    while current_s > 0:
        # بوابات الرياضيات 🧮
        gate = random.choice([("+", 5), ("*", 2)])
        print(f"--- المستوى {level} ---")
        print(f"👥 جيشك: {current_s} | ⭐ مستوى البطل: {data['hero_level']}")
        
        choice = input(f"أمامك بوابة {gate[0]}{gate[1]}، هل تدخل؟ (y/n): ")
        if choice == 'y':
            current_s = (current_s + gate[1]) if gate[0] == '+' else (current_s * gate[1])
        
        # قوة العدو تزداد مع مستوى البطل 👾
        enemy = random.randint(10, 20) * level
        print(f"👾 واجهت عدواً قوته: {enemy}")
        
        if current_s >= enemy:
            current_s -= enemy
            win_gold = level * 10
            data["gold"] += win_gold
            print(f"✅ انتصرت! ربحت {win_gold} ذهبة.")
            level += 1
        else:
            print("❌ خسرت المعركة!")
            break

while True:
    print(f"\n💰 الذهب: {data['gold']} | 🎖️ مستوى البطل: {data['hero_level']}")
    print("1. هجوم ⚔️")
    print("2. تطوير البطل (50 ذهبة) 🦸")
    print("3. خروج 🚪")
    
    op = input("ماذا ستفعل؟ ")
    
    if op == "1":
        start_battle()
    elif op == "2":
        if data["gold"] >= 50:
            data["gold"] -= 50
            data["hero_level"] += 1
            data["soldiers"] += 5
            print("✨ تمت ترقية البطل وجيشك زاد!")
        else:
            print("⚠️ لا تملك ذهبًا كافيًا!")
    elif op == "3":
        break

