import sys
import re
import person
import textrect
import townmode
import universal
from universal import *
import pygame
from pygame.locals import *
import music
import os

""" Note: This file will have to be modified if we ever decide to have multiple person.PC's. Not quite sure what the best way of handling the case of multiple person.PC's is. We'll have
    to see.
"""

gameTitle = ''

TITLE_IMAGE_FILE = None
TITLE_IMAGE_FILE_1 = None
TITLE_IMAGE_FILE_2 = None
TITLE_IMAGE_FILE_3 = None

TITLE_IMAGES = []

def set_title_image(image, extension, numImages):
    "Note: DO NOT provide the extension when providing the path. Provide the extension separately."
    global TITLE_IMAGES
    TITLE_IMAGES.append(image + "." + extension)
    for i in range(1, numImages):
        TITLE_IMAGES.append(image + str(i) + "." + extension)
    print(TITLE_IMAGES)

def title(text):
    global gameTitle
    gameTitle = text

def get_title():
    return gameTitle

gameSubtitle = ''
def subtitle(text):
    global gameSubtitle
    gameSubtitle = text

def get_subtitle():
    return gameSubtitle

firstEpisode = None
OPENING_CRAWL = None

def set_opening_crawl(musicFile, alreadyDecrypted=True):
    global OPENING_CRAWL
    if alreadyDecrypted:
        OPENING_CRAWL = musicFile
    else:
        OPENING_CRAWL = music.decrypt(resource_path(musicFile))

def title_screen_interpreter(keyEvent):
    if keyEvent.key == pygame.K_s:
        request_difficulty()
    elif keyEvent.key == pygame.K_ESCAPE:
        quit()
    elif keyEvent.key == pygame.K_l:
        load_game()
    elif keyEvent.key == pygame.K_a:
        display_acknowledgments()

def display_acknowledgments():
    universal.say_title('Acknowledgments')
    universal.get_screen().blit(universal.get_background(), universal.get_world_view().topleft)
    universal.say(format_text([['Code, Story, Concept: Andrew Russell'], 
        ['Coded in Python using the Pygame engine: pygame.org'],
        ['Images:'],
        ['  title screen image: Rak'],
        #['Sound Effects: Filippo Vicarelli. Downloaded from his website: noiseforfun.com'],
        #['Dungeon step: Click Switch'],
        ['Music: Filippo Vicarelli. Purchased through his website: playonloop.com.'], 
        ['  Opening Crawl/Church theme: Apparition'],
        ['  Title Theme: The Challenge'],
        ['  Episode 1 Titlecard: Bridge over Darkness'],
        ["  Vengador's Theme: Antique Market"],
        ["  Guard's Theme: War Victimis"],
        ['  Avaricum Theme: Spiritual Path'],
        ['  Battle Theme: The Chase'],
        ["  Peaceful Theme(Adventurer's Guild): Jesu"],
        ['  Tense Theme: Hurry Up'],
        ['  Defeated Theme: Graveyard Lord'],
        ["  Peter's Theme: Telekinesis"],
        ["  Carlita's Theme: Goodbye"],
        ["  Maria's Theme : Moonlight"],
        ["  Carrie's Theme: Smart Ideas"],
        ["  Catalin's Theme: Sadistic Game"],
        ["  Roland's Theme: Risky Plan"],
        ["  Elise's Theme: Land of Peace"],
        ]
        ))
    acknowledge(title_screen, None)

def display_title():
    """
    Unused.
    """
    titleImage = pygame.image.load(TITLE_IMAGE_FILE)
    universal.get_screen().blit(titleImage)
    universal.get_screen().flip()
    """
    display_text(get_title() + ":", worldView, worldView.midleft)
    display_text(get_subtitle() + ":", worldView, worldView.midleft)
    """
    

DELAY_INCREMENTS = 100
DELAY_TIME = 8000
DELAY_TIME_SHORT = DELAY_TIME / 2
DELAY_TIME_REALLY_SHORT = DELAY_TIME / 4
DELAY_TIME_LONG = 2 * DELAY_TIME

skip = False
def check_delay():
    for event in pygame.event.get():
        if event.type == KEYUP and event.key == K_RETURN:
            global skip
            skip = True

def delay_really_short():
    count = 0
    while not skip and count < DELAY_TIME_REALLY_SHORT / DELAY_INCREMENTS:
        check_delay()
        pygame.time.delay(DELAY_INCREMENTS)
        count += 1
def delay_short():
    count = 0
    while not skip and count < DELAY_TIME_SHORT / DELAY_INCREMENTS:
        check_delay()
        pygame.time.delay(DELAY_INCREMENTS)
        count += 1

def delay():
    count = 0
    while not skip and count < DELAY_TIME / DELAY_INCREMENTS:
        check_delay()
        pygame.time.delay(DELAY_INCREMENTS)
        count += 1

def delay_long():
    count = 0
    while not skip and count < DELAY_TIME_LONG / DELAY_INCREMENTS:
        check_delay()
        pygame.time.delay(DELAY_INCREMENTS)
        count += 1

def display_crawl():
    if skip:
        universal.say_replace('')
    worldView = universal.get_world_view()
    textRect = universal.get_world_view().copy()
    titleFont = pygame.font.SysFont(universal.FONT_LIST, universal.TITLE_SIZE)
    displayPosition = (worldView.topleft[0], worldView.topleft[1] + 2 * titleFont.get_linesize())
    universal.display_text(universal.get_text_to_display(), textRect, displayPosition, isTitle=False)
    pygame.display.flip()

def opening_crawl():
    music.play_music(OPENING_CRAWL, fadeoutTime=0, wait=True)
    #universal.say_replace([
    #"You've been stabbed in the stomach. Your health magic triggers."])
    #display_crawl()
    #delay_short()  
    #universal.say_replace("But there's no damage to repair.")
    #display_crawl()
    #delay_short()
    universal.say_replace(["A sharp pain springs into life deep within your chest, as if some beast",
    "is trying to cut its way free.",
        "Your health magic surges, as your body tries to repair the damage."])
    display_crawl()
    delay()
    universal.say_replace(["But there's no damage to repair."])
    display_crawl()
    delay_short()
    universal.say_replace(["Ants cover every inch of your skin, tearing into you with their razor-sharp mandibles.",
        "Your health drains away like sand through your fingers."])
    display_crawl()
    delay()
    universal.say_replace(["But there's no damage to repair."])
    display_crawl()
    delay_short()
    universal.say_replace(["Your skin has been scraped raw. The thinnest of clothing,",
        "the slightest of breezes, the gentlest of touches, they all go",
        "beyond pain.",
        "Your body draws on every ounce of power, and suffuses your skin with healing magic."])
    display_crawl()
    delay()
    universal.say_replace("But there's no damage to repair."),
    display_crawl()
    delay_short()
    universal.say_replace(["You can no longer breath. You can no longer see. You can",
        "no longer think."])
    display_crawl()
    delay_short()
    universal.say_replace("You die.")
    display_crawl()
    delay_short()
    universal.say("\n\n40% of your neighbors die.")
    display_crawl()
    delay_short()
    universal.say_replace(["Along the coast of the Medios Sea is a region rife with bickering city-states, known collectively as the One-Thousand-Twenty-Four. The city-states are inhabited by two broad cultures: the bronze-skinned "
        "Taironans, and the much paler Carnutians, though people identify more closely with their city than their culture. In the year 1273, the Wasting Wail descended upon Bonda, a leading",
        "Taironan city. It began in the",
            "Merchant District, raced through the slums, and even swept through the",
            "nobility. Bonda's gates were closed, and the other cities set up a blockade to",
            "enforce the quarantine."])
    display_crawl()
    delay_long()
    universal.say_replace(["An army of holy people came from the Matirian Church, a powerful (Carnutian) religion. They carried with them a new invention: Potions."])
            
    display_crawl()
    delay()
    universal.say_replace(["These Potions, they claimed, were healers in a bottle. They would keep the plague",
            "victims' energy up long enough for them to recover. Out of sheer desperation, the Bondan king allowed the healers into",
            "the city."])
    display_crawl()
    delay_long()
    universal.say_replace(["The death rate dropped from 40% to 5%. When the plague finally ended, there was",
            "a massive celebration throughout the city. Bonda and Avaricum prepared to enter an everlasting",
            "alliance. The Matirian Brothers and Sisters stopped distributing Potions."])
    display_crawl()
    delay_long()
    universal.say_replace([
            "The earliest recipients of the Potions",
            "sank into a deep depression. They couldn't sleep, they could barely",
            "eat, they shook uncontrollably, and some",
            "suffered severe seizures. Crowds gathered outside the Matirian treatment centers,",
            "but", 
            "the Matirians didn't have enough Potions to handle this new, strange disease.",
            "Some began to accuse the Matirians of holding out. Others claimed that the Potions",
            "were poison, part of an Avaricumite plot to conquer Bonda."])
    display_crawl()
    delay_long()
    universal.say_replace("The crowds turned into mobs.")
    display_crawl()
    delay_short()
    universal.say_replace(["Treatment centers were attacked. Brothers and Sisters viciously beaten. Bondan",
            "fought Bondan, brother against sister, for the precious few remaining Potions.",
            "An Avaricumite army arrived and occupied Bonda, helping the Brothers and Sisters",
            "escape."])
    display_crawl()
    delay_long()
    universal.say_replace("Twenty years have passed. Now, Tairona and Carnute teeter on the edge of a")
    display_crawl()
    if not skip:
        music.play_music(music.THEME, DELAY_TIME / 3, wait=True)
    else:
        music.play_music(music.THEME, wait=True)
    #delay_short()

loadingGame = True

def title_screen(episode=None):
    global firstEpisode, loadingGame
    textSurface = None
    titleImage = None
    try:
        titleImage = pygame.image.load(TITLE_IMAGES[0])
        titleImage = pygame.transform.scale(titleImage, (pygame.display.Info().current_w, pygame.display.Info().current_h))
    except IOError:
        textSurface = textrect.render_textrect(get_title(), #+ (":" if get_subtitle() != "" else ""), 
                font, worldView, LIGHT_GREY, DARK_GREY, 1)
    except IndexError:
        textSurface = textrect.render_textrect(get_title(), #+ (":" if get_subtitle() != "" else ""), 
                font, worldView, LIGHT_GREY, DARK_GREY, 1)
    titleImages = []
    if os.path.exists(os.path.join(os.getcwd(), 'save')) and '.init.sav' in os.listdir(os.path.join(os.getcwd(), 'save')):
        townmode.previousMode = None
        townmode.load_game('.init.sav', preserveLoadName=False)
    assert(episode is not None or firstEpisode is not None)
    if episode is not None:
        firstEpisode = episode
    screen = universal.get_screen()
    worldView = universal.get_world_view()
    background = universal.get_background()
    screen.fill(universal.DARK_GREY)
    font = pygame.font.SysFont(universal.FONT_LIST, 50)
    wvMidLeft = worldView.midleft
    if loadingGame:
        for i in range(1, len(TITLE_IMAGES)):
            try:
                titleImages.append(pygame.image.load(TITLE_IMAGES[i]))
                titleImages[-1] = pygame.transform.scale(titleImages[-1], (pygame.display.Info().current_w, pygame.display.Info().current_h))
            except IOError:
                continue
        opening_crawl()
        loadingGame = False
    music.play_music(music.THEME)
    universal.set_commands(['(S)tart', '(L)oad', '(A)cknowledgments', '(Esc)Quit'])
    universal.set_command_interpreter(title_screen_interpreter)
    if not skip:
        pygame.time.delay(125)
        for i in range(0, len(titleImages)):
            print('printing image: ' + str(i))
            screen.blit(titleImages[i], worldView.topleft)
            pygame.time.delay(25)
            pygame.display.flip()
    if titleImage is not None:
        screen.blit(titleImage, worldView.topleft)
    else:
        screen.blit(textSurface, worldView.centerleft)
    pygame.display.flip()
    while 1:
        for event in pygame.event.get():
            if event.type == KEYUP:
                return
    #subtitleLocation = (wvMidLeft[0], wvMidLeft[1]+50)
    #textSurface = textrect.render_textrect(get_subtitle(), pygame.font.SysFont(universal.FONT_LIST, 30), worldView, LIGHT_GREY, DARK_GREY, 1)
    #screen.blit(textSurface, subtitleLocation)
    #pygame.display.update()

def request_difficulty():
    universal.say_title('Character Creation')
    universal.get_screen().blit(universal.get_background(), universal.get_world_view().topleft)
    universal.say('To skip the opening crawl when the game is first loaded, press "Enter"\n\n') 
    universal.say('Before we get started, we need to pick a difficulty level:\n\n')
    universal.say('HAND: Enemies choose their actions purely at random.\n\n')
    universal.say('STRAP: Enemies choose their actions based on their own statistics, and the skills of their allies. They choose their target at random.\n\n')
    universal.say('CANE: Enemies choose their actions based on their statistics, the skills of their allies and previous rounds. They choose their target based on the effects of previous rounds.')
    universal.set_commands(['(H)and', '(S)trap', '(C)ane', '(Esc)Quit', '<==Back'])
    universal.set_command_interpreter(request_difficulty_interpreter)

def request_difficulty_interpreter(keyEvent):
    validCommand = False
    if keyEvent.key == pygame.K_ESCAPE:
        quit()
    elif keyEvent.key == pygame.K_h:
        universal.set_difficulty(universal.HAND)
        validCommand = True
    elif keyEvent.key == pygame.K_s:
        universal.set_difficulty(universal.STRAP)
        validCommand = True
    elif keyEvent.key == pygame.K_c:
        universal.set_difficulty(universal.CANE)
        validCommand = True
    elif keyEvent.key == pygame.K_BACKSPACE:
        title_screen(firstEpisode)
    if validCommand:
        request_gender()

requestNameString = 'Please provide a name, and hit enter when done. Note: The beginning of your name will be automatically capitalized as you type. To erase, use the backspace. To return to the previous screen, press the Esc key.\n'

partialName = ''
def request_name():
    global partialName
    universal.say(requestNameString)
    universal.set_commands(['Esc'])
    if gender == person.MALE:
        partialName = 'Julian'
    else:
        partialName = 'Juliana'
    universal.say(partialName)
    universal.say('_')
    universal.set_command_interpreter(request_name_interpreter)


def request_name_interpreter(keyEvent):
    global partialName
    if keyEvent.key == K_RETURN:
        person.set_PC(person.PlayerCharacter(partialName, 'You are a 23 year old Taironan noble. Unfortunately the vast majority of your family\'s fortunes were destroyed during the Wasting Wail and its fallout about twenty years ago, so you\'re a noble in name only. You have dark, rich caramel skin. You and your sister Catalin were raised by Reyna, a close friend of your parents, in her home city of Chengue. She taught you everything you know about combat and adventuring. At her insistence, you have traveled to Avaricum to seek out an old friend of yours (and an old student of hers): Maria of Chengue.', gender))
        person.get_PC().set_all_stats(2, 2, 2, 2, 2, 10, 10)
        person.set_party(person.Party([person.get_PC()]))
        person.PC.currentEpisode = firstEpisode
        person.PC.name = partialName
        person.PC.set_fake_name()
        request_nickname()
    elif keyEvent.key == K_ESCAPE:
        partialName = ''
        request_gender()
    else:
        playerInput = pygame.key.name(keyEvent.key)
        if re.match(re.compile(r'^\w$'), playerInput):
            partialName += playerInput
        elif keyEvent.key == K_BACKSPACE:
            partialName = partialName[:-1]
        universal.say(requestNameString)
        partialName = simpleTitleCase(partialName)
        if keyEvent.key == K_SPACE:
            partialName += ' '
        universal.say(partialName)
        universal.say('_')

def request_nickname():
    global partialName
    universal.say('Provide a nickname for your character:\n')
    universal.set_commands(['Esc'])
    if person.PC.is_male():
        partialName = 'Juli'
    elif person.PC.is_female():
        partialName = 'Julia'
    universal.say(partialName)
    universal.say('_')
    universal.set_command_interpreter(request_nickname_interpreter)

def request_nickname_interpreter(keyEvent):
    global partialName
    if keyEvent.key == K_RETURN:
        person.PC.nickname = partialName
        final_confirmation()
    elif keyEvent.key == K_ESCAPE:
        partialName = ''
        request_name()
    else:
        playerInput = pygame.key.name(keyEvent.key)
        if re.match(re.compile(r'^\w$'), playerInput):
            partialName += playerInput
        elif keyEvent.key == K_BACKSPACE:
            partialName = partialName[:-1]
        universal.say('Provide a nickname for your character:\n')
        partialName = simpleTitleCase(partialName)
        if keyEvent.key == K_SPACE:
            partialName += ' '
        universal.say(partialName)
        universal.say('_')


def simpleTitleCase(string):
    """
    A quick and dirty function for doing halfway decent title case.
    """
    stringList = str.split(string)
    newString = None
    for word in stringList:
        if word != 'of' and word != 'and' and word != 'the' and word != 'a' and word != 'an' and word != 'for':
            if newString == None:
                newString = [word.title()]
            else:
                newString.append(word.title())
        else:
            if newString == None:
                newString = [word]
            else:
                newString.append(word)
    if newString:
        return ' '.join(newString)
    else:
        return ''

requestDescriptionString = 'The following is your character\'s background. If you wish, you may add additional text. For example, you can give more details about your character\'s physical appearance. Note that this is purely aesthetic, and will not affect any in-game text. Also, you cannot change your character\'s background. To go back, hit Esc. When done, hit enter.\n\n'
def request_description():
    universal.say(requestDescriptionString)
    universal.say(person.PC.description)
    universal.say('_')
    universal.set_command_interpreter(request_description_interpreter)

partialDescription = ''
def request_description_interpreter(keyEvent):
    global partialDescription
    if keyEvent.key == K_RETURN:
        person.PC.description = ' '.join([person.PC.description, partialDescription])
        final_confirmation()
    elif keyEvent.key == K_ESCAPE:
        partialDescription = ''
        request_name()
    else:
        playerInput = pygame.key.name(keyEvent.key)
        if re.match(re.compile(r'^\w$'), playerInput):
            if pygame.key.get_pressed()[K_LSHIFT] or pygame.key.get_pressed()[K_RSHIFT]:
                partialDescription += str.capitalize(playerInput)
            else:
                partialDescription += playerInput
        elif keyEvent.key == K_PERIOD:
            partialDescription += '.'
        elif keyEvent.key == K_COMMA:
            partialDescription += ','
        elif keyEvent.key == K_LEFTPAREN:
            partialDescription += '('
        elif keyEvent.key == K_RIGHTPAREN:
            partialDescription += ')'
        elif keyEvent.key == K_SEMICOLON:
            partialDescription += ';'
        elif keyEvent.key == K_COLON:
            partialDescription += ':'
        elif keyEvent.key == K_BACKSPACE:
            partialDescription = partialDescription[:-1]
        universal.say(requestDescriptionString)
        if keyEvent.key == K_SPACE:
            partialDescription += ' '
        universal.say(' '.join([person.PC.description, partialDescription]))
        universal.say('_')
    

gender = person.MALE
def request_gender():
    universal.say('Please select a gender.') 
    universal.set_commands(['(M)ale', '', '(F)emale', '<==Back', '(Esc)Quit'])
    universal.set_command_interpreter(request_gender_interpreter)

def request_gender_interpreter(keyEvent):
    global gender
    if keyEvent.key == K_m:
        gender = person.MALE
        request_name()
    elif keyEvent.key == K_f:
        gender= person.FEMALE
        request_name()
    elif keyEvent.key == K_BACKSPACE:
        request_difficulty()
    elif keyEvent.key == K_ESCAPE:
        quit()


partialDescription = ''
"""
Stats:
    warfare
    magic
    willpower
    grapple
    stealth
    health
    mana
    current health
    current mana
"""
statPoints = 3

def final_confirmation():
    person.PC.learn_spell(person.allSpells[0][0][0])
    person.PC.learn_spell(person.allSpells[0][1][0])
    person.PC.learn_spell(person.allSpells[0][2][0])
    person.PC.learn_spell(person.allSpells[0][3][0])
    universal.say(person.PC.character_sheet_spells(), columnNum=1)
    #print(person.PC.character_sheet_spells())
    universal.set_commands('Is this acceptable? Y\N')
    universal.set_command_interpreter(final_confirmation_interpreter)

def final_confirmation_interpreter(keyEvent):
    #person.PC = person.get_person.PC()
    if keyEvent.key == K_y:
        person.PC.currentEpisode = firstEpisode
        person.PC.currentEpisode.start_episode()
        townmode.save_game('.init', preserveSaveName=False)
        townmode.saveName = ''
    elif keyEvent.key == K_n:
        global spellPoints
        global statPoints
        spellPoints = 3
        statPoints = 3
        #person.PC.clear_spells()
        #person.PC.reset_stats()
        title_screen(firstEpisode)
        universal.set_command_interpreter(title_screen_interpreter)
        universal.set_commands(['(S)tart', '(L)oad', '(Esc)Quit'])


        
def load_game():
    universal.say_title('Load Game')
    universal.get_screen().blit(universal.get_background(), universal.get_world_view().topleft)
    townmode.load(title_screen)
