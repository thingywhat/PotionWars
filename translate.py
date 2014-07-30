#!/usr/bin/python
"""
Copyright 2014 Andrew Russell

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

"""
Usage notes:
    In order to use this translation program, you need two things:
    1. A latex source file using the sprpgs.sty file that contains the transcript for the episode.
    2. A python file that contains the character and room definitions (these SHOULD NOT be added to the file generated by this program, because the generated file WILL BE OVERWRITTEN every time
    you run this script).
"""

IMPORTS = ['import universal', 'import textCommands', 'import person', 'import items', 'import pwenemies', 'import dungeonmode', 'import itemspotionwars']
TAB = '    '
DEBUG = True
def translate(fileName, charRoomFile, episodeName, nodeNum, tab=TAB, imports=None):
    with open(fileName, 'r') as transcript:
        tex = transcript.readlines()

    if imports and not ' '.join(['import', charRoomFile]) in imports:    
        pythonCode = imports + [' '.join(['import', charRoomFile])]
    elif imports:
        pythonCode = list(imports)
    else:
        pythonCode = ['import', charRoomFile]

    texIter = iter(tex) 
    sceneCount = 1
    nodeCount = nodeNum

    try:
        while True:
            scan_to_scene_start(texIter)
            process_scene_start(pythonCode, texIter)
            while True:
                scan_to_node_or_scene_end(texIter)
                if r'\begin{node}' in line or r'\begin{childnode}' in line:
                    nodeCount += 1
                    process_node(pythonCode, texIter, nodeCount)
                elif r'\begin{closeScene}' in line:
                    process_scene_end(pythonCode, texIter)
                    break
    except StopIteration:
        return pythonCode


def scan_to_scene_start(texIter, line):
    line = next(texIter)
    while r'\begin{openScene}' != line:
        line = next(texIter)


def process_scene_start(texIter, pythonCode):
    scan_to_code_block(texIter)
    pythonCode.append(''.join(['def start_scene_', sceneCount, '_', episodeName, '(', 'loading=False', '):']))
    line = next(texIter)
    while '\end{openScene}' != line:
        append_to_function(pythonCode, line)


def scan_to_code_block(texIter):
    line = next(texIter)
    while r'\begin{code}' != line:
        line = next(texIter)

def process_code_block(pythonCode, texIter, tab):
    line = next(texIter)
    while r'\end{code}' != line:
        append_to_function(pythonCode, line, tab)

def scan_to_node_or_scene_end(texIter):
    line = next(texIter)
    while not r'\begin{node}' in line and not r'\begin{childnode}' in line and not r'\begin{closeScene}' in line:
        line = next(texIter)

def process_node(pythonCode, texIter, nodeCount):        




def append_to_function(code, newLine, tab=TAB):
    code.append(''.join([tab, newLine]))



if DEBUG:
    import os
    pythonCode = translate(os.path.join('transcripts', 'episode2.tex'), 'episode2CharRooms.py', 'episode_2', 320, imports=IMPORTS)
    print(pythonCode)


    




