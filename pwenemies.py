""" Copyright 2014 Andrew Russell

This file is part of PotionWars.
PotionWars is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PotionWars is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PotionWars.  If not, see <http://www.gnu.org/licenses/>.
"""
import universal
from universal import *
import person
import itemspotionwars
import copy
import spells_PotionWars
import positions
import items
import spanking


def name():
    return universal.state.player.name

class Enemy(person.Person):
    def __init__(self, name, gender, defaultLitany, description="", printedName=None, coins=20, specialization=universal.BALANCED, dropChance=3, musculature='', 
            bodyType='', height='', hairLength='', hairStyle='', eyeColor='', skinColor='', order=person.zeroth_order, identifier=None):
        """
        Drop chance determines the chances that this character will drop a piece of equipment.
        """
        super(Enemy, self).__init__(name, gender, defaultLitany, defaultLitany, description, printedName, coins, specialization, order, musculature=musculature,
                bodyType=bodyType, height=height, hairLength=hairLength, hairStyle=hairStyle, eyeColor=eyeColor, skinColor=skinColor, identifier=identifier)
        self.dropChance = dropChance
        self.printedName = self.printedName + (' (M)' if self.is_male() else ' (F)')
        self.equip(items.emptyWeapon)
        self.equip(items.emptyLowerArmor)
        self.equip(items.emptyUpperArmor)
        self.equip(items.emptyUnderwear)
        self.spankingFunctions = {
                positions.OTK: (self.otk_intro, self.otk_round, self.otk_failure)
                positions.STANDING: (self.standing_intro, self.standing_round, self.standing_failure)
                positions.ON_THE_GROUND: (self.on_the_ground_intro, self.on_the_ground_round, self.on_the_ground_failure)
            }

    def otk_intro(self, top, bottom):
        raise NotImplementedError()

    def otk_round(self, top, bottom):
        raise NotImplementedError()

    def otk_failure(self, top, bottom):
        raise NotImplementedError()

    def otk_reversal(self, top, bottom):
        raise NotImplementedError()

    def standing_intro(self, top, bottom):
        raise NotImplementedError()

    def standing_round(self, top, bottom):
        raise NotImplementedError()

    def standing_failure(self, top, bottom):
        raise NotImplementedError()

    def standing_reversal(self, top, bottom):
        raise NotImplementedError()

    def on_the_ground_intro(self, top, bottom):
        raise NotImplementedError()

    def on_the_ground_round(self, top, bottom):
        raise NotImplementedError()

    def on_the_ground_failure(self, top, bottom):
        raise NotImplementedError()

    def on_the_ground_reversal(self, top, bottom):
        raise NotImplementedError()

    def drop(self):
        "TODO: Implement"
        raise NotImplementedError()

    def level_up(self, level):
        """
        Used for scaling. Level up to the specified level.
        TODO: Implement
        """
        raise NotImplementedError(' '.join(['Uh-Oh! Looks like', author, 'forgot to implement level_up for', self.name, 'please send them an e-mail at', 
            get_author_email_bugs()]))

    def post_combat_spanking(self): 
        raise NotImplementedError(' '.join(['Uh-Oh! Looks like', author, 'forgot to implement post_combat_spanking for', self.name, 'please send them an e-mail at', 
            get_author_email_bugs()]))

    def __eq__(self, other):    
        """
        For enemies, reduce equality to seeing if they point to the same object. This is necessary because two different generic enemies may not have the same name.
        """
        return self is other



#--------------------------Introduced in Episode 1----------------------------------------------------
class VengadorWarrior(Enemy):
    #def __init__(self, name, gender, defaultLitany, description="", printedName=None, 
            #coins=20, specialization=BALANCED)
    def __init__(self, gender, level=0, identifier=None):
        super(VengadorWarrior, self).__init__('Vengador Warrior', gender, None, specialization=universal.WARFARE, bodyType='voluptuous', musculature='muscular', 
                height='tall', identifier=identifier)
        self.level = level
        #self.equip(copy.copy(itemspotionwars.leatherCuirass))
        self.equip(copy.copy(itemspotionwars.tunic))
        self.equip(copy.copy(itemspotionwars.trousers))
        self.equip(copy.copy(itemspotionwars.warspear))
        self.description = universal.format_line(['''A tall, broad-shouldered''', person.manwoman(self) + ".", person.HeShe(self), '''is wielding a''', self.weapon().name, 
        '''and is wearing''', self.shirt().name, '''and''', self.lower_clothing().name + "."])
        self.set_all_stats(strength=1, dexterity=3, willpower=0, talent=0, health=12, mana=0, alertness=1)

    def otk_intro(self, top, bottom):
        if self is top:
            spankingText = universal.format_text([['''The Vengador Warrior rushes''', bottom.printedName, '''in a burst of speed that belies''', top.hisher(), '''size, and jabs''', bottom.printedName, 
                '''in the stomach with''', top.hisher(), '''spear. As''', bottom.printedName, '''hunches forward, the warrior crouches and yanks''', bottom.printedName, 
                '''across''', 
                top.hisher(), '''lap, while wrapping one of''', top.hisher(), '''arms around''', bottom.printedName + "'s", '''midsection.'''],
                ['''Straddling the crouching warrior’s lap,''', bottom.printedName, '''is helpless as the Vengador Warrior administers a thorough, if short, spanking to''', bottom.hisher(), 
                '''plump, unblocked bottom. The whole thing happens so quickly, that''', top.printedName, '''is able to cover the Taironan's entire ass in peppering swats before''', bottom.heshe(),
                '''can even begin to fight back.''']])
        else: 
            spankingText = universal.format_text([[top.printedName, '''rushes the Vengador Warrior in a burst of speed, and jabs the warrior in the stomach with the butt of''', 
                top.hisher(),
                top.weapon().name + ".", '''As the Vengador Warrior involuntarily bends forward,''', top.name, '''goes into a crouch, and throws the Vengador Warrior across''', person.hisher(), 
                '''lap. Then,''', top.heshe(), '''wraps one of''', top.hisher(), '''arms around the fighter’s midsection.'''],
                ['''Straddling''', top.printedName + "'s", '''lap, the warrior finds''', bottom.himselfherself(), '''completely helpless as''', top.printedName, '''administers a thorough, if short,''',
                    '''spanking to''', bottom.hisher(), '''shapely, unblocked bottom.''', '''The whole thing happens so quickly, that''', top.printedName, 
                    '''is able to cover the Taironan's''', bottom.bum_adj(), '''ass in peppering swats before''', bottom.heshe(), '''can even begin to fight back.''']])
        return spankingText

    def standing_intro(self, top, bottom):
        if self is top:
            spankingText = universal.format_text([['''The dark-skinned warrior surprises''', bottom.printedName, '''by striking low with the butt of''', top.hisher(), '''spear, rather than at the''',
            '''torso with the tip.''',
                '''The solid wood crashes into''', bottom.printedName + "’s", '''legs and knocks''', bottom.hisher(), '''feet out from under''', bottom.himher() + ".", 
                bottom.printedName, '''lands hard on''', hisher(), '''knees. The Vengador Warrior wastes no time in leaping forward, roughly grabbing''', bottom.printedName + "’s", 
                '''shoulders and thrusting''', bottom.hisher(), '''head between the warrior’s calves.''', bottom.printedName, '''extends''', bottom.hisher(), '''legs in an attempt to''',
                '''stand up, but with''', bottom.hisher(), '''head hopelessly locked in a tight grip,''', bottom.heshe(), '''only makes''', bottom.hisher(), '''own''', bottom.bum_adj(), 
                '''bottom a tempting target for the Vengador Warrior.'''],
                ['''Pleased with''', top.himselfherself() + ",", '''the Vengador Warrior clutches''', bottom.printedName + "'s", bottom.lower_clothing().name, '''tightly with one hand and begins to''',
                '''whale on''', bottom.hisher(), bottom.muscle_adj(), '''wriggling butt with the other.''']])
        else:
            spankingText = universal.format_text([[top.printedName, '''distracts the dark-skinned warrior with a flurry of swings and thrusts that draw the Vengador Warrior’s attention above''', 
                top.printedName + "'s", '''head.''', top.printedName, '''then sweeps the warrior's feet out from underneath''', bottom.himher() + ".", '''The Vengador Warrior lands hard on''', 
                bottom.hisher(), '''knees.''', top.printedName, '''then roughly grabs the warrior’s shoulders and thrusts the warrior's head between''', top.hisher(), '''calves. The warrior''',
                '''extends''', bottom.hisher(), '''legs in an attempt to stand up, but with''', warrior.hisher(), '''head hopelessly locked in a tight grip,''', bottom.heshe(), '''only makes''',
                 bottom.hisher(), '''own tight bottom a tempting target for''', top.printedName + "."],
                 ['''Pleased with the success of''', top.hisher(), '''fanciful moves,''', top.printedName, '''clutches''', bottom.printedName + "'s", '''trousers tightly with one hand, and begins''',
                 '''to whale on''', bottom.hisher(), '''round butt with the other.''']])
        return spankingText

    def on_the_ground_intro(self, top, bottom):
        if self is top:
            spankingText = universal.format_text([['''Suddenly, the Vengador Warrior unleashes a desperate attack at''', bottom.printedName + "'s", '''head.''', bottom.printedName, 
            '''dodges the spear thrust. The warrior snaps the spear down, and sweeps''', bottom.printedName + "'s", '''legs out from underneath''', bottom.himher() + ",", '''and''', bottom.printedName,
            '''lands hard on''', bottom.hisher(), '''face. Before''', bottom.printedName, '''can get back up, the Vengador Warrior sits down on the middle of''', bottom.printedName + "'s", 
            '''back and begins drumming''', bottom.printedName + "'s", '''bottom with both hands. Facedown, and with''', bottom.hisher(), '''arms pinned uselessly between the Warrior's legs, and''',
            bottom.hisher(), '''own torso,''', bottom.printedName, '''can do nothing but wait for a chance to escape, while''', bottom.heshe(), '''drums''', bottom.hisher(), '''toes onto the floor''',
            '''in pain and humiliation.''']])
        else: 
            spankingText = universal.format_text([['''Suddenly,''', top.printedName, '''lunges forward in a seemingly desperate attack aimed at''', bottom.printedName + "'s", '''head. The warrior''',
                '''dodges the''', top.weapon().weaponType, '''strike, only to discover the attack was feint, when''', top.printedName, '''suddenly shifts''', top.hisher(), '''weight, and knocks''', 
                bottom.hisher(), '''legs knocked out from under''', bottom.himher() + ".", '''As the Vengador Warrior hits the ground facefirst,''', top.printedName, '''sits down on the middle of''',
                '''the''',
                 '''warrior’s back and begins to drum''' bottom.hisher(), '''bottom with both hands. Facedown, and with''', bottom.hisher(), '''arms pinned uselessly between''', top.printedName + 
                 "'s", '''legs and''', bottom.hisher(), '''own sides, the Vengador can do nothing but wait for a chance to escape, and drum''', bottom.hisher(), 
                 '''toes against the floor in pain.''']]) 
        return spankingText

    def otk_continuing(self, top, bottom):
        if self is top:
            return universal.format_text([[bottom.printedName, '''struggles against the broad-shouldered warrior, but with''', bottom.hisher(), '''arm around the''', person.heroheroine + "'s",
            '''waist, the''',
                '''Vengador has all the leverage. That doesn’t stop''', bottom.PrintedName, '''from thrusting''', bottom.hisher(), '''legs upward between stinging full-armed swats, but the warrior''',
                '''sees what the heroine is up to and, with a “Tsk, tsk, none of that!” directs''', top.hisher(), '''attention to''', bottom.printedName + "'s.", bottom.printedName, '''howls''', 
                bottom.hisher(), '''displeasure and drums''', bottom.hisher(), '''fists against the stone floor as the warrior’s solid hand batters''', bottom.hisher(), '''thighs and sit spots.''']])
        else: 
            return universal.format_text([['''The broad-shouldered warrior struggles against''', top.printedName + "'s", '''grip, but with''', bottom.hisher(), '''arm around the warrior’s''',
                '''waist, the''', top.heroheroine(), '''has all the leverage. That doesn’t stop the Vengador Warrior from trying to put''', bottom.hisher(), '''strength to use by thrusting''', 
                bottom.hisher(),
                '''legs upward between stinging full-armed swats, but''', top.printedName, '''sees what the fighter is up to and, with an admonishing click of''', top.hisher(), '''tongue, directs''',
                top.hisher(), '''attention to the warrior’s thighs. The''', bottom.manwoman(), '''howls''', bottom.hisher(), '''displeasure and drums''', bottom.hisher(), '''fists against the stone''',
                '''floor as''', top.printedName + "'s", '''solid hand batters''', bottom.hisher(), '''thighs and sit spots.''']])

    def standing_continuing(self, top, bottom):
        if self is top:
            return universal.format_text([[bottom.printedName, '''continues''', bottom.hisher(), '''struggle to escape from the Vengador Warrior’s grip, but''', bottom.hisher(), '''head is securely''',
                '''stuck between the Vengador Warrior's muscled thighs. A wave of embarrassment rolls over''', bottom.himher(), '''as''', bottom.heshe(), '''feels the warrior’s hard spanks heat up''',
                bottom.hisher(), '''up-thrust, weaving,''' bottom.bum_adj(), '''bottom.''']])
        else:
            return universal.format_text([['''The Vengador Warrior continues''', bottom.hisher(), '''struggle to escape''', top.printedName + "'s", '''grip, but''', bottom.hisher(), '''head is''',
                '''securely stuck between the''', top.heroheroine() + "'s", top.muscle_adj(), '''thighs. If anything,''' bottom.hisher(), '''struggles only spur''', top.printedName, '''on to harder''',
                '''and harder smacks, making''', bottom.hisher(), bottom.muscle_adj(), '''bottom bounce.''']])

    def on_the_ground_continuing(self, top, bottom):
        if self is top:
            return universal.format_text([['''The Vengador Warrior has brightened''', bottom.printedName + "’s", '''ass beneath''', bottom.lower_clothing().name, ' '.join(['''and''', 
                bottom.underwear().name + ","])  if bottom.wearing_underwear() else ',', '''and none of''', bottom.printedName + "'s", '''squirming seems ready to change the situation. The Vengador''',
                '''concentrates on''', bottom.printedName + "'s", '''thighs and sit spots, eliciting both wails and pleas from''', top.hisher(), '''victim.''']])
        else:
            return universal.format_text([[top.printedName, '''continues to mercilessly batter the Vengador Warrior's''', bottom.bum_adj(), '''bottom, and none of the warrior’s squirming seems''',
                '''poised to change the situation.''', top.printedName, '''concentrates on the Vengador’s thighs and sit spots, eliciting both wails and pleas from''', top.hisher(), '''victim.''']])

    def otk_reversal(self, top, bottom):
        return universal.format_text([[self.otk_intro(top, bottom)], ['''However, while''', top.printedName, '''continues to redden''', bottom.printedName + "'s" '''behind,''', bottom.printedName, 
            '''musters all''', bottom.hisher(), '''lower-body strength into a grab-and-twist with''', bottom.printedName + "'s", '''thighs and hips, twisting both the Taironans around and''',
            '''onto the floor. The surprised''', '''warrior''' if self is top else top.heroheroine(), '''is slow to respond, and is still lying on''', top.hisher(), 
            '''stomach when a now-crouching''', bottom.printedName, '''grabs the waistband''',
            '''of''', top.hisher(), '''trousers and yanks the helpless warrior onto''', bottom.hisher(), '''lap.''', bottom.printedName, '''begins pelting the warrior’s squirming bottom with''',
            '''a vengeance.''', top.printedName, '''has no hope of freeing''', top.himselfherself(), '''and finds''', top.himselfherself(), '''primarily preoccupied with trying to keep''', 
            top.hisher(), top.lower_clothing().name, top.lower_clothing().updown() + "."]])

    def standing_reversal(self, top, bottom):
        return universal.format_text([[self.stading_intro(top, bottom)], ['''Then,''', bottom.heroheroine() + "'s", '''strong hands grip''', top.printedName, '''firmly around the ankles.''',
            bottom.printedName, '''pulls''', bottom.hisher(), '''hands forward, forcing''', top.printedName, '''to topple backward, and land on''', top.hisher(), '''behind.''', bottom.printedName,
            '''pulls''', bottom.himselfherself(), '''to''', bottom.hisher(), '''full height and wastes no time in grasping''', top.printedName, '''and shoving''', top.hisher(), '''head between''',
            bottom.hisher(), '''legs.''', bottom.printedName, ' '.join(['''spies the waistband of''', top.printedName + "'s", top.underwear().name, ' '.join(['''peeking out from above''', 
                top.hisher(), 
                top.hisher(), top.lower_clothing().name]) if top.wearing_lower_clothing(), else '', '''and clutches it tightly.''']) if top.wearing_underwear() else 
            ' '.join(['''grabs the back of''', top.printedName + "'s", top.lower_clothing.name + "."]),
                    ['''Then,''', bottom.printedName, '''lifts''', top.printedName + "'s", '''bottom up by to hip level.''', top.printedName, '''curses and kicks, but that doesn't stop''',
                        bottom.printedNamep, '''from putting''', top.printedName, '''in the same vulnerable position in which''', top.heshe(), '''had tried to place''', bottom.printedName + ".",
                        '''With''', top.hisher(), '''head locked tightly between''', bottom.printedName + "'s", '''calves, the warrior can do little more than wriggle''', top.hisher(), 
                        '''bottom as''', bottom.printedName, '''assaults it with stinging spanks, turning it the same color as the humiliated''', top.printedName + "'s", '''face.''']]])
        
    def on_the_ground_reversal(self, top, bottom):
        return format_text([[self.on_the_ground_intro(top, bottom)], [top.printedName, '''But then,''', bottom.printedName, '''flips''', bottom.hisher(), '''hips over, and slings one of''', 
            top.printedName + "'s", '''legs away from''', top.hisher(), '''body. The other combatant lands on all fours but isn't there for long, because''', bottom.printedName, '''quickly sits on''',
            top.hisher(), '''back with enough force to slam''', top.himher(), '''to the floor.''', bottom.printedName, '''begins''', bottom.hisher(), '''spanking revenge by focusing all of''', 
            bottom.hisher(), '''swats on one cheek, leaving''', top.printedName, '''writhing under the relentless punishment.''']])

    def default_stats(self):
        self.set_all_stats(strength=1, dexterity=3, willpower=0, talent=0, health=15, mana=0, alertness=1)

    def otk_failure(self, top, bottom):
        return universal.format_text([[top.printedName, '''rushes''', bottom.printedName, '''in a burst of speed, swinging the butt of''', top.hisher(), '''weapon at''', bottom.printedName + "'s",
            '''face.''', bottom.printedName, '''deflects the weapon with''', bottom.hisher(), '''own weapon and swats''', top.printedName + "'s", '''thigh as they dance apart.''']])

    def standing_failure(self, top, bottom):
        retun universal.format_text([[top.printedName, '''spins''', top.hisher(), top.weapon().name, '''in an effort to distract''', bottom.printedName, '''from''', top.hisher(), '''true target:''',
            bottom.printedName + "'s", '''shins. However,''', bottom.printedName, '''sees''', top.printedName + "'s", '''feet heading toward''', bottom.hisher(), '''legs. The warrior knocks them''',
            ''''aside with''', ' '.join(['''the shaft of''', bottom.hisher(), '''spear and quickly brings it back around to crack against''', top.printedName + "'s", top.bum_adj(), '''behind.''']) if
            top.weapon().weaponType == items.Spears.weaponType else ' '.join(['''the blade of''', bottom.hisher(), '''weapon. Then''', bottom.heshe(), '''snaps''', bottom.hisher(), 
                bottom.weapon().name,  
            '''back around, and cracks the flat of the blade against,''', top.printedName + "'s", top.bum_adj(), '''bottom.''']),
                top.printedName, '''jumps and yelps, while one of''', top.hisher(), '''hands involuntarily flies back to''', top.muscle_adj(), '''round bottom in an attempt to rub away the sting.''']])

    def on_the_ground_failure(self, top, bottom):
        return universal.format_text([[top.printedName, '''puts all''', top.hisher(), '''strength into a desperate strike – or so it seems.''', bottom.printedName, '''reads the true intention of''',
            top.hisher(), '''attack, and when the warrior’s leg sweep comes, kicks''', bottom.hisher(), '''foot out of the way with such force that''', top.printedName, 
            '''wobbles, dangerously close''',
            '''to toppling.''', bottom.printedName, '''takes advantage of the brief window of vulnerability to land a solid swat to the embarrassed fighter’s backside before readying''', 
            bottom.himselfherself(),''' for''', bottom.hisher(), '''next move.''']])

    def post_combat_spanking(self):
        bottomAdj = "large, smooth, round" if self.is_female() else "large, rather hairy"
        warriorText = format_text([['''The warrior staggers, and falls to one knee,''', person.hisher(self), '''weapon slipping from''', person.hisher(self), '''fingers.'''],
        [universal.state.player.name, '''approaches''', person.himher(self) + ',', '''kicking''', person.hisher(self), '''weapon out of reach.'''],
        ['''"Why are the insurgents attacking the guild? Who is leading the attack?" asks''', universal.state.player.name + "."],
        ['''The warrior spits at''', universal.state.player.name + "'s", '''face. Well, tries to. It's less spit, and more drool. Losing all your health will do that to you.'''],
        ['''"Right then."''', universal.state.player.name, '''goes down on one knee, grabs the warrior's shoulders, and hauls''', person.himher(self), '''over''', person.hisher(), 
            '''thigh.'''],
        ['''The warrior laughs. "You don't really think a spanking is going to make me reveal anything, do you?"'''],
        ['''"Well, worst case is you get a much needed punishment," says''', universal.state.player.name + ".", person.HeShe(), '''hooks''', person.hisher(), '''fingers in''', 
            '''the warrior's trousers, and slides them down to''', person.hisher(self), '''ankles, baring a''', bottomAdj, '''bottom. The warrior bears''', 
            person.hisher(self), '''undressing stoically.''', name(), '''flexes''', person.hisher(), '''fingers, and gets ready to break said stoicism.'''],
        [name(), '''begins smacking the young''', person.manwoman(self) + "'s", '''bottom, setting a fast and furious pace.''', person.HisHer(self), '''bottom quickly''',
            '''reddens, and''', person.heshe(self), '''begins to squirm a little. Still, the warrior remains stubbornly silent.''', '''So,''', name(), '''shifts''', 
            person.hisher(), '''attention to the warrior's sitspots, and the sensitive crease where bottom meets thigh.'''],
            ['''A few grunts slip past the warrior's lips, and''', person.hisher(self), '''fingers start to curl.'''],
        ['''"Had enough?" asks''', name() + ",", '''massaging''', person.hisher(), '''palm. The warrior's bottom is hard and muscled, and spanking it hurts''', name() + "'s",
            '''hand far more than it has any right to!'''],
        [person.HeShe(self), '''laughs. "Please. Ana's reminder taps hurt more than this."'''],
        ['''For a second,''', name(), '''hesitates, and studies the red, angry looking bottom.''']])
        if universal.state.player.resilience() > self.resilience():
            warriorText = format_text([warriorText, [name(), '''steels''', person.himselfherself() + ".", person.HeShe(), '''slips off''', person.hisher(), '''pack, and pulls''',
                '''out''', person.hisher(), '''wooden spoon.'''],
            ['''"Right then."''', name(), '''taps the spoon against the''', person.manwoman(self) + "'s", '''bottom. "Let's see if I can change that attitude."'''],
            [name(), '''raises the spoon above''', person.hisher(), '''head, and whips it down against the warrior's bottom.'''],
            ['''The warrior gives a strangled cry, and''', person.hisher(self), '''body jerks against''', name() + "'s", '''thigh.'''],
            [name(), '''works the spoon vigorously, spreading a stinging burn across the Vengador's bottom. At first, the Vengador bears the spoon with''',
                '''the same stoicism as''', name() + "'s", '''hand. Then,''', name(), '''lands a particularly stinging smack to''', person.hisher(self), '''sitspot, and''',
                '''the dam breaks.''', person.HeShe(self), '''starts kicking and flailing,''', person.hisher(self), '''red bottom wiggling around on''', name() + "'s", 
                '''thigh.'''],
            ['''"Ok, ok," cries the insurgent. "Stop, stop, please I've had enough!"'''],
            ['''"Why are you attacking the guild?" asks''', name() + "."],
            ['''"Everyone knows Adrian has a stockpile of weapons he uses to outfit his adventurers," says the insurgent. "Only the military and guard armories have more,''',
                '''but those are much more heavily guarded."'''],
            ['''"Who is that woman out there leading the attack?" asks''', name() + "."],
            ['''"I don't know," says the''', person.manwoman(self) + "."],
            [name(), '''gives''', person.himher(self), '''a hard smack with the spoon.'''],
            ['''"It's true, it's true!" wails the insurgent, kicking''', person.hisher(self), '''legs. "I only joined a few months ago. I was trained by Ana."'''],
            ['''"Whose Ana?" asks''', name() + "."],
            ['''"A Taironan woman. I think she's from Bonda," says the warrior. "She was in charge of recruiting and training us."'''],
            ['''"Well, she didn't do a very good job," mutters''', name() + "."],
            ['''"Not like she had a lot of time," snaps the warrior. "Besides there were a lot of us."'''],
            [name(), '''frowns, and pushes the warrior off''', person.hisher(), '''thigh.'''],
            ['''It would appear that''', name() + "'s", '''arrived in Avaricum just in time for things to get interesting. Joy.''']])
            universal.state.player.add_keyword('learned_Vengadores_are_escalating')
        else:
            warriorText = format_text([warriorText, [name(), '''rubs''', person.hisher(), '''hand, and considers the warrior's blazing bottom, and''',
            person.hisher(), '''stoicism. Then,''', name(), '''decides that''', person.heshe(), '''doesn't have anymore time to waste, and shoves the warrior off''',
            person.hisher(), '''knee.'''],
            ['''"You're not worth it," says''', name() + ",", '''standing and brushing off''', person.hisher(), '''hands.'''],
            [name(), '''notices the warrior smirk as''', person.heshe(self), '''pulls up''', person.hisher(self), '''trousers.''', name(), '''turns away from''', 
            person.himher(self) + ".", '''Smirk or not,''', person.heshe(self), '''was still too weak to attack''', name(), '''again.''']])
        return warriorText


class VengadorSpellslinger(Enemy):

    def __init__(self, gender, level=0, identifier=None):
        super(VengadorSpellslinger, self).__init__('Vengador', gender, None, specialization=universal.COMBAT_MAGIC, bodyType='voluptuous', height='short', musculature='soft', identifier=identifier)
        self.level = level
        self.set_all_stats(strength=0, dexterity=1, willpower=2, talent=4, health=6, mana=10, alertness=0)
        if gender == person.FEMALE:
            self.equip(copy.copy(itemspotionwars.wornDress))
        else:
            self.equip(copy.copy(itemspotionwars.wornRobe))
        self.equip(copy.copy(itemspotionwars.staff))
        self.description = universal.format_line(['''A short Taironan''', person.manwoman(self), '''dressed in a''', 
            self.lower_clothing().name + ".", person.HeShe(self), '''carries a''', self.weapon().name + "."])
        self.learn_spell(spells_PotionWars.firebolt)
        self.learn_spell(spells_PotionWars.icebolt)
        self.learn_spell(spells_PotionWars.magicbolt)
        self.spankingPositions = [positions.overOneKnee, positions.waistBetweenLegs, positions.diaper]

    def default_stats(self):
        self.set_all_stats(strength=0, dexterity=1, willpower=2, talent=4, health=8, mana=10, alertness=0)

    def otk_intro(self, top, bottom):
        raise NotImplementedError()

    def otk_round(self, top, bottom):
        raise NotImplementedError()

    def otk_failure(self, top, bottom):
        raise NotImplementedError()

    def otk_reversal(self, top, bottom):
        raise NotImplementedError()

    def standing_intro(self, top, bottom):
        raise NotImplementedError()

    def standing_round(self, top, bottom):
        raise NotImplementedError()

    def standing_failure(self, top, bottom):
        raise NotImplementedError()

    def standing_reversal(self, top, bottom):
        raise NotImplementedError()

    def on_the_ground_intro(self, top, bottom):
        raise NotImplementedError()

    def on_the_ground_round(self, top, bottom):
        raise NotImplementedError()

    def on_the_ground_failure(self, top, bottom):
        raise NotImplementedError()

    def on_the_ground_reversal(self, top, bottom):
        raise NotImplementedError()



    def post_combat_spanking(self):
        insurgentText = format_text([['''The Vengador leans against a nearby wall, breathing heavily.''', person.HeShe(self), '''tries to stumble away from''', name() + ",",
            '''leaning on the wall for support.''', name(), '''steps up next to''', person.himher(self), '''and presses a hand to the wall on either side of''', 
            person.himher(self) + "."],
        ['''"Who taught you how to use magic like that?" asks''', name() + "."],
        ['''"Nobody," says the Vengador. "I'm self-"'''],
        [name(), '''grabs''', person.himher(self), '''by the shoulders, spins''', person.himher(self), '''around, and presses''', person.hisher(self), '''upper body''',
            '''against the wall, so that''', person.hisher(self), '''bottom juts out slightly.''', name(), '''smacks the seat of the Vengador's''', 
            self.lower_clothing().name + "."],
        ['''"You're either lying, or the most gifted spellslinger since Ada herself," says''', name() + ".", name(), '''lands another hard slap to''', person.hisher(self), 
            '''bum. "Now. Who. Taught. You?"'''],
        ['''"Nobody-oww!" The Vengador wiggles and squeals as''', name(), '''starts to spank''', person.hisher(self), '''soft bottom.''', name(), '''doesn't stop until''', 
            person.hisher(universal.state.player), '''hand is good and sore.'''],
        ['''"Now, tell me," says''', name() + "."],
        ['''"No!" says the insurgent.''']])
        if universal.state.player.resilience() > self.resilience():
            if self.gender == person.FEMALE:
                bumAdj = "large, round, light brown"
            else:
                bumAdj = "light brown, surprisingly smooth"
            insurgentText = format_text([insurgentText, ['''"Fine."''', name(), '''grabs the back of''', person.hisher(self), self.lower_clothing().name + ",", 
                '''and lifts''','''it up past''', self.name + "'s", '''waist, revealing a bare,''', bumAdj, '''bottom.'''],
                ['''The Vengador squeals in indignity and kicks weakly at''', name() + ".", '''"No, stop, not on the bare!"'''],
                [name(), '''pins the''', self.lower_clothing().name, '''to the Vengador's back with''', person.hisher(universal.state.player), '''left hand. "Tell me the name of the person who''',
                    '''trained you."'''],
                ['''The insurgent doesn't say anything.'''],
                ['''"Fine."''', name(), '''strikes the insurgent's ample, soft, right butt cheek.''', person.HisHer(self), '''cheek bounces beneath the slap. Then''', name(),
                    '''slaps the left cheek. Then right, then left, then right again.'''],
                ['''Pretty soon, the Vengador's entire bottom is bouncing and rippling beneath''', name() + "'s", '''hard, merciless hand. The Vendgaodr's hips sway''',
                    '''desperately back and forth, trying in vain to dodge''', name() + "'s", '''hard slaps.''', person.HeShe(self), '''kicks''', person.hisher(self), 
                    '''feet and weakly pounds the wall.''', person.HeShe(self), '''tries to escape, but''', person.hisher(self), '''efforts are weak and ineffectual, and''',
                    '''all they earn''', person.himher(self), '''are a few sharp slaps to''', person.hisher(self),  '''thighs.'''],
                ['''"Ok, ok," wails the Vengador. "Please, please stop I'll tell you, I'll tell you!"'''],
                ['''"Well?" says''', name() + ",", '''landing a sharp slap to''', person.hisher(self), ''' very red bottom. "Out with it!"'''],
                ['''"Her name is Sierra," says the vengador through''', person.hisher(self), '''tears. "She works for one of the Slum Ladies, Zulimar. Specializies in''',
                    '''combat magic. She helped train all of us before this attack."'''],
                [name(), '''steps away from the wimpering Taironan, and''', person.heshe(self), '''promptly collapses into a crouch, rubbing''', person.hisher(self), 
                '''throbbing bottom.''', name(), '''looks around, and plots''', person.hisher(self), '''next move.''']])
        else:
            insurgentText = format_text([insurgentText, [name(), '''curses under''', person.hisher(universal.state.player), '''breath, and gives''', hisher(self), '''hand a shake.''', 
                self.name(), '''considers giving the stubborn Taironan a bare bottom spanking. But the sounds of battle return to''', name() + "'s", '''years, a harsh''',
                '''reminder that time is of the essence.''', name(), '''steps away from''', person.hisher(universal.state.player), '''beaten opponent, and plans''', person.hisher(self), 
                '''next move.''']])
        return insurgentText

class VengadorScout(Enemy):
    def __init__(self, gender, level=0, identifier=None):
        super(VengadorScout, self).__init__('Vengador Scout', gender, None, specialization=person.GRAPPLE, bodyType='slim', height='average', musculature='fit', identifier=identifier)
        self.level = level
        self.equip(copy.copy(itemspotionwars.tunic))
        self.equip(copy.copy(itemspotionwars.trousers))
        self.equip(copy.copy(itemspotionwars.dagger))
        self.description = format_line(['''A short, thin Taironan''', person.manwoman(self), '''dresssed in a''', self.shirt().name + "," ''' and''', 
            self.lower_clothing().name + ".", person.HeShe(self), '''carries a''', self.weapon().name + "."])
        self.set_all_stats(strength=1, dexterity=3, willpower=2, talent=1, health=9, mana=7, alertness=2)
        self.spankingPositions = [positions.overTheKnee, positions.underarm, positions.standing]
        self.learn_spell(spells_PotionWars.heal)
        self.learn_spell(spells_PotionWars.weaken)
        self.learn_spell(spells_PotionWars.fortify)

    def post_combat_spanking(self): 
        return format_text([['''The young''', person.manwoman(self), '''is on''', person.hisher(self), '''hands and knees, breathing heavily, and shaking slightly.'''],
        [name(), '''approaches the insurgent, and gives''', person.himher(self), '''a sharp slap on the bottom. The''', person.manwoman(self), 
            '''yelps, and tries to crawl away,''',
        '''but''', person.hisher(self), '''arms give out, and''', person.heshe(self), '''collapses.'''],
        ['''"So what's your job?" asks''', name() + "."],
        ['''The insurgent doesn't respond. Instead''', person.heshe(self), '''struggles back onto''', person.hisher(self), '''hands and knees, and starts to crawl away''',
            '''again.''',
        name(), '''kneels down next to''', person.himher(self), '''and presses against the middle of''', person.hisher(self), '''back, pushing''', person.hisher(self), 
        '''chest and face into the ground.''', name(), '''gives''', person.hisher(self), '''upthrust bottom a warning rub. "Will you answer my question, or do I need to''',
        '''yank these trousers down and paddle your bottom?"'''],
        ['''"Or you could, you know, stop fighting your own people, and instead help us," says the scout angrily, turning''', person.hisher(self), '''head and glaring at''',
            name() + "."],
    [name(), '''sighs. "Not this again."''', person.HeShe(), '''gives''', self.name, '''a pair of swift, hard slaps, one to each cheek. The insurgent squirms a little,''',
        '''but manages to keep quiet. "Try again."'''],
    ['''"I'm a scout," mutters the insurgent.'''],
    ['''"Oh good. I'm new here, and don't know much about the back of the guild," says''', name() + ".", '''"How about you tell me what I can expect?"'''],
    ['''The scout doesn't say anything.'''],
    [name(), '''grabs the waistband of the''', person.manwoman(self) + "'s", '''trousers, and pulls them down to''', person.hisher(self) + "'s", '''knees, revealing a''',
        '''small, but firm bare bottom.'''],
    [name(), '''pulls''', person.hisher(), '''wooden spoon out of''', person.hisher(), '''pack, and taps it lightly against the''', person.manwoman(self) + "'s", 
        '''bottom.''', name(), '''smirks a little when the scout tenses . "Last chance."'''],
    '''"Oh come on, you aren't seriously going to spank me are you?" says the scout. "Do you really thing a sore bottom is going to make me talk?"''',
    ['''"Actually, it can be surprisingly effective," says''', name() + ",", '''rubbing the''', person.manwoman(self) + "'s", '''bottom with the spoon. "It's weird.''',
    '''Regular torture just encourages the torturee to lie to make the pain stop. But for some reason, a spanking prompts the spankee to tell the truth. Maybe our truth''',
    '''centers are in our bottoms, and a spanking stimulates them?"'''],
    ['''"That makes absolutely no sense," says the insurgent.'''],
    ['''"Yes, well, whatever." The spoon whips through the air and cracks against the insurgent's bottom. The insurgent yelps, and''', person.hisher(self), '''hips jerk''',
    '''forward under the impact. "Whatever the reason, it is most effective, as you shall soon see."''', name(), '''works the spoon furiously, giving the''', 
    '''scout's bottom a thorough hiding.'''],
    ['''The scout bawls and thrashes beneath the bombardment,''', person.hisher(self), '''bitty bottom bouncing beneath the spoon's stinging slaps.'''],
    '''"Ok, ok," yelps the scout at last. "I'll tell you, I'll tell you, just please stop spanking me!"''',
    ['''"I'm listening."''', name(), '''rubs the flat of the spoon against the scout's tender bottom.'''],
    ['''"There are eight rooms," mutters the scout. "On the first floor is a kitchen, a clinic, a dining room and the training room for Adrian's combat trainer, a man''',
        '''named Morey. Apparently, the cook is a retired adventurer whose even quicker to whip out her spatula than you are to whip out that horrible spoon. There's a''',
        '''healer in the clinic. The dining room doesn't have much of interest. On the second floor are the grapple training room, the magic training room and the stealth''',
        '''training room. The stealth room is a maze, but I don't know much more. Our people who have gone in there, haven't come back out again. The armory is where''',
        '''Adrian stores all of his equipment. There are currently two Taironans in there right now, directing our acquisitions, a warslinger, and a warrior. Either one''',
        '''of them would wipe the floor with you."'''],
    ['''Wonderful.'''],
    [name(), '''forces a smile. "There, what'd I tell you? Totally effective."'''],
    ['''The scout grumbles something under''', person.hisher(self), '''breath, and reaches back to lift up''', person.hisher(self), '''trousers.'''],
    [name(), '''stands, and considers''', person.hisher(), '''next move.''']])


    def reversal_spanking_text(self, spanker, spankee, position):
        T = spanker
        B = spankee
        P = position
        if P == positions.underarm:
            return format_text([[T.name, '''rams''', person.hisher(T), '''knee into''', B.name + "'s", '''gut, causing''', B.name, '''to hunch in pain,''', T.name, 
            '''wraps''', person.hisher(T), '''arm around''', B.name + "'s", '''waist. But then''', B.name, '''snakes''', person.hisher(B), '''own arm around''', 
            T.name + "'s", '''waist, sweeps''', T.name + "'s", '''feet out from under''', person.himher(T) + "," '''and bends''', T.name, '''over''', person.hisher(B), 
            '''hip.'''],
            [B.name, '''grabs''', T.name + "'s", T.clothing_below_the_waist().name, '''and''', items.lowerlift(T.clothing_below_the_waist()),
            items.itthem(T.clothing_below_the_waist()), '''exposing''', T.name + "'s", T.underwear().name + ".",  B.name, '''starts to give''', T.name, 
            '''a hard spanking.''',
                T.name + "'s", T.clad_bottom(), '''jiggles beneath the barrage, and it isn't long before''', T.name, '''is bobbing and kicking in''', B.name + "'s", 
                '''merciless grip.'''],
            ['''Eventually,''', T.name, '''manages to land a solid punch to the back of''', B.name + "'s", '''knee.''', B.name + "'s", '''leg buckles, and''', 
            person.heshe(B), '''loses''', person.hisher(B), '''balance. This gives''', T.name, '''just the opening''', person.heshe(T), '''needs to wiggle free.''', 
            person.HeShe(T),
            spanking.restore_lower_lift(T.clothing_below_the_waist()), person.hisher(T), T.clothing_below_the_waist().name, '''back over''', person.hisher(T), 
            '''smarting bottom.''']])
        elif P == positions.diaper:
            return format_text([[T.name, '''crouches slightly, and goes for''', B.name + "'s", '''legs.''', B.name, '''shuffles backward a few steps, and''', 
                person.hisher(B), '''hands lance out to catch''', T.name + "'s", '''shoulders.''', B.name, '''gives a hard downward shove on''', T.name + "'s", 
                '''shoulders, forcing''', T.name, '''to bend over so far that''', T.name, '''has to catch''', person.himselfherself(T), '''with''', person.hisher(T), 
                '''hands.''', B.name, '''wraps''', person.hisher(B), '''thighs around''', T.name + "'s", '''neck, and lands a sharp slap to''', T.name + "'s", 
                '''vulnerable, upthrust bottom.''', T.name, '''grunts, grabs''', B.name + "'s", '''calves and tries to force them apart enough to slip free.''',
                B.name, '''holds firm, however, and begins spanking''', T.name + "'s", '''bottom.'''],
            ['''The spanking is hard and fast, and before long''', T.name + "'s", '''bottom is jerking back and forth, and''', T.name, '''is yowling and stomping''', 
                person.hisher(T), '''feet. Eventually,''', person.heshe(T), '''manages to force''', B.name + "'s", '''legs apart enough for''', person.hisher(T), 
                '''head to slip free.''', T.name, '''scrambles backwards, while''', B.name, '''fixes''', person.hisher(B), '''stance, and prepares for''', T.name + "'s",
                '''retaliation.''']])
    def had_spanking_reversed_by(self, person, position):
        return self.reversal_spanking_text(self, person, position)
    #abstractmethod
    def reversed_spanking_of(self, person, position):
        return self.reversal_spanking_text(person, self, position)
    #abstractmethod

    def spanking_miss_text(self, spanker, spankee, position):
        T = spanker;
        B = spankee; 
        if position == positions.underarm:
            return format_text([[T.name, '''rams''', person.hisher(T), '''knee into''', B.name + "'s", '''gut.''', B.name, '''hunches in pain, bending over slightly.''',
            T.name, '''tries to wrap''', person.hisher(T), '''arm around''', B.name + "'s", '''back, but''', B.name, '''rams''', person.hisher(B), '''elbow''',
            '''into''', T.name + "'s", '''armpit.''', T.name, '''cries out in pain, and stumbles back a few steps, clutching at''', person.hisher(T), '''armpit. This''',
            '''gives''', B.name, '''the time''', person.heshe(T), '''needs to catch regain''', person.hisher(B), '''footing.''']])
        elif position == positions.diaper:
            return format_line([T.name, '''grabs''', B.name + "'s", '''legs.''', B.name, '''smashes''', person.hisher(B), '''knee into''', T.name + "'s", '''nose, and''',
            T.name, '''stumbles backward.'''])

    def avoided_spanking_by(self, person, position):
        return self.spanking_miss_text(person, self, position)
    #abstractmethod
    def failed_to_spank(self, person, position):
        return self.spanking_miss_text(self, person, position)

    def spanking_text(self, spanker, spankee, position):
        T = spanker
        B = spankee
        P = position
        if P == positions.underarm:
            return format_text([[T.name, '''rams''', person.hisher(T), '''knee into''', B.name + "'s", '''gut.''', B.name, '''hunches in pain, bending over slightly, and''',
                T.name, '''wraps''', person.hisher(T), '''arm around''', B.name + "'s", '''back.''', person.HeShe(T), '''bends''', B.name, '''over''', person.hisher(T), 
                '''hip.''', T.name, '''gives''', B.name + "'s", '''bottom a light rub, and then proceeds to give it a good hiding.'''],
                [B.name, '''twists and kicks desperately in''', T.name + "'s", '''grip, but''', T.name, '''only tightens''', person.hisher(T), '''grip, and increases the''',
                '''speed and force of''', person.hisher(T), '''smacks.''', B.name, '''starts to yelp, and''', person.hisher(B), '''squirming becomes so bad, that''',
                person.heshe(B), '''manages to break free.''', person.HeShe(B), '''scrambles away, rubbing''', person.hisher(B), '''smarting bottom and cursing.''']])
        elif P == positions.diaper:
            return format_text([[T.name, '''grabs''', B.name + "'s", '''legs and heaves, throwing''', B.name, '''flat on''', person.hisher(B), '''back.''', T.name, 
            '''pushes''', B.name + "'s", '''legs back over''', person.hisher(B), '''head, and crouches down next to''', B.name + "'s", '''vulnerable bottom.''', T.name, 
            '''raises''', person.hisher(T), '''hand.''', B.name, '''wiggles and claws at the ground, desperately trying to drag''', person.himselfherself(B), '''away, but''',
            T.name, '''holds''', person.himher(B), '''fast. Then,''', T.name + "'s", '''hand crashes into''', B.name + "'s", '''bottom.''', '''The bottom ripples beneath''',
            '''the impact, and''', B.name, '''yowls.''', T.name, '''raises''', person.hisher(T), '''hand and spanks''', B.name, '''again. And again, and again, and again,''',
            '''seemingly with no sign of stopping.'''],
            [B.name, '''writhes around on the ground, howling and carrying on, while''', T.name, '''thrashes''', person.hisher(B), '''bottom. Eventually,''', B.name, 
            '''manages to heave''', person.hisher(B), '''upper body up enough to grab''', T.name + "'s", '''arm and break''', T.name + "'s", '''grip on''', person.hisher(B),
            '''legs.''', B.name, '''rolls onto''', person.hisher(B), '''side and scrambles back to''', person.hisher(B), '''feet.''']])
        
    #abstractmethod
    def spanks(self, person, position):
        return self.spanking_text(self, person, position)
    #abstractmethod
    def spanked_by(self, person, position):
        return self.spanking_text(person, self, position)
