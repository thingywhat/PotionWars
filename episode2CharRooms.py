import universal
import person
import items
import itemspotionwars
import textCommandsMusic
import townmode
import episode

ildri = None
kitchen = None
deidre = None
alondra = None
    #def __init__(self, name, gender, defaultLitany, litany, description="", printedName=None, 
    #        coins=20, specialization=universal.BALANCED, order=zeroth_order, dropChance=0, rawName=None, skinColor='', eyeColor='', hairColor='', hairStyle='', marks=None,
    #        musculature='', hairLength='', height='', bodyType=''): 
#BODY_TYPES = ['slim', 'average', 'voluptuous', 'heavyset']


#HEIGHTS = ['short', 'average', 'tall', 'huge']


#MUSCULATURE = ['soft', 'fit', 'muscular']


#HAIR_LENGTH = ['short', 'shoulder-length', 'back-length', 'butt-length']

#SHORT_HAIR_STYLE = ['down']
#SHOULDER_HAIR_STYLE = SHORT_HAIR_STYLE + ['ponytail', 'braid', 'pigtail', 'bun']
def build_chars():
    global ildri, deidre, alondra
    try:
        ildri = universal.state.get_character('Ildri.person')
    except KeyError:
        ildri = person.Person('Ildri', person.FEMALE, None, None, ' '.join(["Ildri is a towering, muscular, golden-haired, and fair-skinned woman. She looks to be about the same age as Adrian. She is",
            "wearing an apron, a",
            "short-sleeve tunic, a pair of wool trousers, and a heavy pair of boots. Her long blonde hair is pulled back into a single thick braid."]), skinColor="peach", eyeColor="blue", 
            hairColor="blonde", hairStyle="braid", musculature="muscular", hairLength="back-length", height="huge", bodyType="voluptuous")
    else:
        ildri.description = ' '.join(["Ildri is a towering, muscular, golden-haired, and fair-skinned woman. She looks to be about the same age as Adrian. She is",
            "wearing an apron, a",
            "short-sleeve tunic, a pair of wool trousers, and a heavy pair of boots. Her long blonde hair is pulled back into a single thick braid."])
        ildri.skinColor = 'peach'
        ildri.eyeColor = 'blue'
        ildri.hairColor = 'blonde'
        ildri.hairStyle = 'braid'
        ildri.musculature = 'muscular'
        ildri.hairLength = 'back-length'
        ildri.height = 'huge'
        ildri.bodyType = 'voluptuous'
    try: 
        deidre = universal.state.get_character('Deidre.person')
    except KeyError:
        deidre = person.Person('Deidre', person.FEMALE, None, None, ''.join(["A tall, slender woman with frizzy, shoulder-length blonde hair pulled back into a bun. She has piercing blue eyes, and",
            " carries herself with rod-straight posture. A black beret sits on top of her head."]), specialization=universal.STATUS_MAGIC, order=person.first_order, skinColor="peach", eyeColor="blue",
            hairColor="blonde", hairLength="shoulder-length", hairStyle="bun", height="tall", bodyType="slim", musculature="fit")
    try:
        alondra = universal.state.get_character('Alondra.person')
    except KeyError:
        alondra = person.Person('Alondra', person.FEMALE, None, None, ''.join(['''Alondra is a Taironan woman with rich, dark caramel skin, . She is a little on the short side of average.''',
            '''She has shoulder-length hair black hair, and relatively small, dark brown eyes. In contrast to her height, her breasts are a little on the large side of average.''',
            '''She has a round, protruding bottom that rolls enticingly when she walks.''']), specialization=universal.SPEED, order=person.second_order, skinColor="caramel", eyeColor="brown",
            hairColor="black", hairLength="shoulder-length", hairStyle="down", height="average", bodyType="voluptuous", musculature="soft")

    try:
        sofia = universal.state.get_character("Sofia.person")
    except KeyError:
        sofia = person.Person("Sofia", person.FEMALE, None, None, ''.join(['''Sofia is a middle-aged Taironan woman with moderately dark skin. She is short and thin, with graying shoulder-length''',
            '''hair. She is wearing a plain cotton dress.''']))




def build_rooms():
    global kitchen
    print("starting to build kitchen")
    try:
        kitchen = universal.state.get_room('Kitchen')
    except KeyError:
        print("Building kitchen!")
        kitchen = townmode.Room("Kitchen", ' '.join(["The kitchen is a rather large room with two long, waist-high counters running through the middle. Along the sides of the walls are a few small",
            "tables and",
            "stools. A pair of massive hearths sit at the far end, a pair of turnspit coelophysii are lying next to the hearth. Their heads come up, and they gurgle happily as", 
            universal.state.player.name,
            "enters. There is a large hole in the south wall. The hole has been braced with several hastily carved timbers, and a few thick furs have been draped over it, so that",
            "customers can't peer directly into the back of the guild. A pair of high windows sit on the western wall on either side of the hearth."]), [universal.state.get_room("Adventurer's Guild")],
            None, None, textCommandsMusic.LIGHT_HEARTED, "textCommandsMusic.LIGHT_HEARTED", None)
    try:
        sofiasClinic = universal.state.get_room("Sofia's Clinic")
    except KeyError:
        sofiasClinic = townmode.Room("Sofia's Clinic", ' '.join(["The 'clinic' is nothing more than a long, dark, low-ceilinged room crammed with piles of ragged blankets. Immersed in the piles of",
            "blankets are dozens of Taironans, all in different states of duress. Most of them are shivering quietly, or sleeping fitfully. Some are moaning, and shifting. A few are crying, and shaking",
            "violently. There is even one man who is being wrestled back into his blankets, while screaming incoherently in some dialect that", textCommandsMusic.name(), "doesn't recognize. No more than",
            "half a dozen helpers, mostly women, are moving about the clinic's patients."]), [universal.state.get_room("Slums")], None, None, textCommandsMusic.TAIRONAN, "textCommandsMusic.TAIRONAN", None)

def start_scene_1_episode_3(loading=False): 
    universal.say("Next Time on Pandemonium Cycle: The Potion Wars")
    music.play_music(music.THEME)
    universal.say(["Roland and Elise are getting married, and", textCommandsMusic.name(), "is asked to escort Elise to the Lowen Monastery for the wedding. But things get a little bit complicated when an old enemy of Roland's",
    "ambushes them!"])
    universal.set_commands("Press Enter t osave")
    universal.set_command_interpreter(textCommandsMusic.end_content_interpreter)

def end_scene_1_episode3():
        pass

episode3Scene1 = episode.Scene("Episode 3 Scene 1", start_scene_1_episode_3, end_scene_1_episode3)
episode3 = episode.Episode(3, 'No Good Deed', scenes=[episode3Scene1])
