import pandas as pd
import io

def AshesClassName(Primary, Secondary):
    Primary = Primary.lower()
    Secondary = Secondary.lower()
    df = pd.read_csv(io.StringIO(Data), sep=",")
    #print(df.to_string())
    return df.loc[ClassToNum(Primary)][ClassToNum(Secondary)+1]

def AoCclassPrimarySecondary(Class):
    df = pd.read_csv(io.StringIO(Data), sep=",")
    for x in range(0,df.shape[0]):
        for y in range(0,df.shape[1]):
            if str(df.loc[x][y]) == Class: 
                    print(x,y)
                    return df.loc[x][0],df.columns[y]
                
    
def ClassToNum(ClassName):
    classnum = {
            "bard": 0,
            "cleric": 1,
            "fighter": 2,
            "mage": 3,
            "ranger": 4,
            "rogue": 5,
            "summoner": 6,
            "tank": 7,
            }
    return classnum[ClassName]

def AshesClasses():
    return "Bard Cleric Fighter Mage Ranger Rogue Summoner Tank"

Data = '''NaN,Bard,Cleric,Fighter,Mage,Ranger,Rogue,Summoner,Tank
Bard,Minstrel,Soul Weaver,Tellsword,Magician,Song Warden,Trickster,Songcaller,Siren
Cleric,Scryer,High Priest,Templar,Oracle,Protector,Shadow Disciple,Shaman,Apostle
Fighter,Bladedancer,Highsword,Weapon Master,Spellsword,Hunter,Shadowblade,Bladecaller,Dreadnought
Mage,Sorcerer,Acolyte,Battle Mage,Archwizard,Spellhunter,Shadow Caster,Warlock,Spellstone
Ranger,Bowsinger,Soulbow,Strider,Scion,Hawkeye,Scout,Falconer,Sentinel
Rogue,Charlatan,Cultist,Duelist,Nightspell,Predator,Assassin,Shadow Lord,Shadow Guardian
Summoner,Enchanter,Necromancer,Wild Blade,Spellmancer,Beastmaster,Shadowmancer,Conjurer,Brood Warden
Tank,Argent,Paladin,Knight,Spellshield,Warden,Nightshield,Keeper,Guardian'''
