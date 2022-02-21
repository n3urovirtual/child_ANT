#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on February 21, 2022, at 15:12
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'childANT'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\presi\\Documents\\GitHub\\child_ANT\\Child ANT\\childANT_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instr_1"
instr_1Clock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='Stimuli/inst_1.png', mask=None,
    ori=0, pos=(0, 0), size=(1150,950),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
is_space = keyboard.Keyboard()
import random

# Initialize components for Routine "instr_2"
instr_2Clock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='Stimuli/inst_2.png', mask=None,
    ori=0, pos=(0, 0), size=(1150, 950),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
is_space2 = keyboard.Keyboard()

# Initialize components for Routine "instr_3"
instr_3Clock = core.Clock()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='Stimuli/inst_3.png', mask=None,
    ori=0, pos=(0, 0), size=(1150, 950),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
is_space3 = keyboard.Keyboard()

# Initialize components for Routine "instr_4"
instr_4Clock = core.Clock()
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='Stimuli/inst_4.png', mask=None,
    ori=0, pos=(0, 0), size=(1150, 950),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
is_space4 = keyboard.Keyboard()

# Initialize components for Routine "instr_5"
instr_5Clock = core.Clock()
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='Stimuli/inst_5.png', mask=None,
    ori=0, pos=(0, 0), size=(1150, 950),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
is_space5 = keyboard.Keyboard()

# Initialize components for Routine "instr_6"
instr_6Clock = core.Clock()
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='Stimuli/inst_6.png', mask=None,
    ori=0, pos=(0, 0), size=(1150, 950),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
is_space6 = keyboard.Keyboard()

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fix_cross = visual.ShapeStim(
    win=win, name='fix_cross', vertices='cross',
    size=(40, 40),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "cue"
cueClock = core.Clock()
fix_cross2 = visual.ShapeStim(
    win=win, name='fix_cross2', vertices='cross',
    size=(40, 40),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
asterisk = visual.ImageStim(
    win=win,
    name='asterisk', 
    image='Stimuli/asterisk.png', mask=None,
    ori=0, pos=[0,0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
fix_cross3 = visual.ShapeStim(
    win=win, name='fix_cross3', vertices='cross',
    size=(40, 40),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "target"
targetClock = core.Clock()
fix_cross4 = visual.ShapeStim(
    win=win, name='fix_cross4', vertices='cross',
    size=(40, 40),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
target_stimulus = visual.ImageStim(
    win=win,
    name='target_stimulus', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
response = keyboard.Keyboard()

# Initialize components for Routine "response_feedback"
response_feedbackClock = core.Clock()
feedback_image = visual.ImageStim(
    win=win,
    name='feedback_image', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sounds = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='sounds')
sounds.setVolume(1)

# Initialize components for Routine "Game_start"
Game_startClock = core.Clock()
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='Stimuli/inst_7.png', mask=None,
    ori=0, pos=(0, 0), size=(1150, 950),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
is_space7 = keyboard.Keyboard()

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fix_cross = visual.ShapeStim(
    win=win, name='fix_cross', vertices='cross',
    size=(40, 40),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "cue"
cueClock = core.Clock()
fix_cross2 = visual.ShapeStim(
    win=win, name='fix_cross2', vertices='cross',
    size=(40, 40),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
asterisk = visual.ImageStim(
    win=win,
    name='asterisk', 
    image='Stimuli/asterisk.png', mask=None,
    ori=0, pos=[0,0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
fix_cross3 = visual.ShapeStim(
    win=win, name='fix_cross3', vertices='cross',
    size=(40, 40),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "target"
targetClock = core.Clock()
fix_cross4 = visual.ShapeStim(
    win=win, name='fix_cross4', vertices='cross',
    size=(40, 40),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
target_stimulus = visual.ImageStim(
    win=win,
    name='target_stimulus', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
response = keyboard.Keyboard()

# Initialize components for Routine "response_feedback"
response_feedbackClock = core.Clock()
feedback_image = visual.ImageStim(
    win=win,
    name='feedback_image', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sounds = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='sounds')
sounds.setVolume(1)

# Initialize components for Routine "trial_break"
trial_breakClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Κάνε ένα σύντομο διάλειμμα.\n\nΌταν είσαι έτοιμος/η, πάτησε το <SPACE> για να συνεχίσεις.',
    font='Times New Roman',
    pos=(0, 0), height=40, wrapWidth=1250, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Το πεινασμένο ψάρι χόρτασε, άρα η αποστολή σου ολοκληρώθηκε.\n\nΕυχαριστούμε για τη συμμετοχή σου!',
    font='Times New Roman',
    pos=(0, 0), height=40, wrapWidth=1500, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr_1"-------
continueRoutine = True
# update component parameters for each repeat
is_space.keys = []
is_space.rt = []
_is_space_allKeys = []
# keep track of which components have finished
instr_1Components = [image, is_space]
for thisComponent in instr_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_1"-------
while continueRoutine:
    # get current time
    t = instr_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *is_space* updates
    waitOnFlip = False
    if is_space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        is_space.frameNStart = frameN  # exact frame index
        is_space.tStart = t  # local t and not account for scr refresh
        is_space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(is_space, 'tStartRefresh')  # time at next scr refresh
        is_space.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(is_space.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(is_space.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if is_space.status == STARTED and not waitOnFlip:
        theseKeys = is_space.getKeys(keyList=['space'], waitRelease=False)
        _is_space_allKeys.extend(theseKeys)
        if len(_is_space_allKeys):
            is_space.keys = _is_space_allKeys[-1].name  # just the last key pressed
            is_space.rt = _is_space_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_1"-------
for thisComponent in instr_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_2"-------
continueRoutine = True
# update component parameters for each repeat
is_space2.keys = []
is_space2.rt = []
_is_space2_allKeys = []
# keep track of which components have finished
instr_2Components = [image_2, is_space2]
for thisComponent in instr_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_2"-------
while continueRoutine:
    # get current time
    t = instr_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_2* updates
    if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_2.frameNStart = frameN  # exact frame index
        image_2.tStart = t  # local t and not account for scr refresh
        image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
        image_2.setAutoDraw(True)
    
    # *is_space2* updates
    waitOnFlip = False
    if is_space2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        is_space2.frameNStart = frameN  # exact frame index
        is_space2.tStart = t  # local t and not account for scr refresh
        is_space2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(is_space2, 'tStartRefresh')  # time at next scr refresh
        is_space2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(is_space2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(is_space2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if is_space2.status == STARTED and not waitOnFlip:
        theseKeys = is_space2.getKeys(keyList=['space'], waitRelease=False)
        _is_space2_allKeys.extend(theseKeys)
        if len(_is_space2_allKeys):
            is_space2.keys = _is_space2_allKeys[-1].name  # just the last key pressed
            is_space2.rt = _is_space2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_2"-------
for thisComponent in instr_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_3"-------
continueRoutine = True
# update component parameters for each repeat
is_space3.keys = []
is_space3.rt = []
_is_space3_allKeys = []
# keep track of which components have finished
instr_3Components = [image_3, is_space3]
for thisComponent in instr_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_3"-------
while continueRoutine:
    # get current time
    t = instr_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_3* updates
    if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_3.frameNStart = frameN  # exact frame index
        image_3.tStart = t  # local t and not account for scr refresh
        image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
        image_3.setAutoDraw(True)
    
    # *is_space3* updates
    waitOnFlip = False
    if is_space3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        is_space3.frameNStart = frameN  # exact frame index
        is_space3.tStart = t  # local t and not account for scr refresh
        is_space3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(is_space3, 'tStartRefresh')  # time at next scr refresh
        is_space3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(is_space3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(is_space3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if is_space3.status == STARTED and not waitOnFlip:
        theseKeys = is_space3.getKeys(keyList=['space'], waitRelease=False)
        _is_space3_allKeys.extend(theseKeys)
        if len(_is_space3_allKeys):
            is_space3.keys = _is_space3_allKeys[-1].name  # just the last key pressed
            is_space3.rt = _is_space3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_3"-------
for thisComponent in instr_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_4"-------
continueRoutine = True
# update component parameters for each repeat
is_space4.keys = []
is_space4.rt = []
_is_space4_allKeys = []
# keep track of which components have finished
instr_4Components = [image_4, is_space4]
for thisComponent in instr_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_4"-------
while continueRoutine:
    # get current time
    t = instr_4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_4* updates
    if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_4.frameNStart = frameN  # exact frame index
        image_4.tStart = t  # local t and not account for scr refresh
        image_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
        image_4.setAutoDraw(True)
    
    # *is_space4* updates
    waitOnFlip = False
    if is_space4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        is_space4.frameNStart = frameN  # exact frame index
        is_space4.tStart = t  # local t and not account for scr refresh
        is_space4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(is_space4, 'tStartRefresh')  # time at next scr refresh
        is_space4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(is_space4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(is_space4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if is_space4.status == STARTED and not waitOnFlip:
        theseKeys = is_space4.getKeys(keyList=['space'], waitRelease=False)
        _is_space4_allKeys.extend(theseKeys)
        if len(_is_space4_allKeys):
            is_space4.keys = _is_space4_allKeys[-1].name  # just the last key pressed
            is_space4.rt = _is_space4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_4"-------
for thisComponent in instr_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_5"-------
continueRoutine = True
# update component parameters for each repeat
is_space5.keys = []
is_space5.rt = []
_is_space5_allKeys = []
# keep track of which components have finished
instr_5Components = [image_5, is_space5]
for thisComponent in instr_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_5"-------
while continueRoutine:
    # get current time
    t = instr_5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_5* updates
    if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_5.frameNStart = frameN  # exact frame index
        image_5.tStart = t  # local t and not account for scr refresh
        image_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
        image_5.setAutoDraw(True)
    
    # *is_space5* updates
    waitOnFlip = False
    if is_space5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        is_space5.frameNStart = frameN  # exact frame index
        is_space5.tStart = t  # local t and not account for scr refresh
        is_space5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(is_space5, 'tStartRefresh')  # time at next scr refresh
        is_space5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(is_space5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(is_space5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if is_space5.status == STARTED and not waitOnFlip:
        theseKeys = is_space5.getKeys(keyList=['space'], waitRelease=False)
        _is_space5_allKeys.extend(theseKeys)
        if len(_is_space5_allKeys):
            is_space5.keys = _is_space5_allKeys[-1].name  # just the last key pressed
            is_space5.rt = _is_space5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_5"-------
for thisComponent in instr_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_6"-------
continueRoutine = True
# update component parameters for each repeat
is_space6.keys = []
is_space6.rt = []
_is_space6_allKeys = []
# keep track of which components have finished
instr_6Components = [image_6, is_space6]
for thisComponent in instr_6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_6"-------
while continueRoutine:
    # get current time
    t = instr_6Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_6Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_6* updates
    if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_6.frameNStart = frameN  # exact frame index
        image_6.tStart = t  # local t and not account for scr refresh
        image_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
        image_6.setAutoDraw(True)
    
    # *is_space6* updates
    waitOnFlip = False
    if is_space6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        is_space6.frameNStart = frameN  # exact frame index
        is_space6.tStart = t  # local t and not account for scr refresh
        is_space6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(is_space6, 'tStartRefresh')  # time at next scr refresh
        is_space6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(is_space6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(is_space6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if is_space6.status == STARTED and not waitOnFlip:
        theseKeys = is_space6.getKeys(keyList=['space'], waitRelease=False)
        _is_space6_allKeys.extend(theseKeys)
        if len(_is_space6_allKeys):
            is_space6.keys = _is_space6_allKeys[-1].name  # just the last key pressed
            is_space6.rt = _is_space6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_6"-------
for thisComponent in instr_6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr_6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Practise_loop = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Practise.csv'),
    seed=None, name='Practise_loop')
thisExp.addLoop(Practise_loop)  # add the loop to the experiment
thisPractise_loop = Practise_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractise_loop.rgb)
if thisPractise_loop != None:
    for paramName in thisPractise_loop:
        exec('{} = thisPractise_loop[paramName]'.format(paramName))

for thisPractise_loop in Practise_loop:
    currentLoop = Practise_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPractise_loop.rgb)
    if thisPractise_loop != None:
        for paramName in thisPractise_loop:
            exec('{} = thisPractise_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [fix_cross]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation"-------
    while continueRoutine:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_cross* updates
        if fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_cross.frameNStart = frameN  # exact frame index
            fix_cross.tStart = t  # local t and not account for scr refresh
            fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
            fix_cross.setAutoDraw(True)
        if fix_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross.tStartRefresh + random.uniform(0.4,1.6)-frameTolerance:
                # keep track of stop time/frame for later
                fix_cross.tStop = t  # not accounting for scr refresh
                fix_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross, 'tStopRefresh')  # time at next scr refresh
                fix_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "cue"-------
    continueRoutine = True
    routineTimer.add(0.150000)
    # update component parameters for each repeat
    asterisk.setPos((Cue_X, Cue_Y))
    # keep track of which components have finished
    cueComponents = [fix_cross2, asterisk]
    for thisComponent in cueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    cueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "cue"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = cueClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=cueClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_cross2* updates
        if fix_cross2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_cross2.frameNStart = frameN  # exact frame index
            fix_cross2.tStart = t  # local t and not account for scr refresh
            fix_cross2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross2, 'tStartRefresh')  # time at next scr refresh
            fix_cross2.setAutoDraw(True)
        if fix_cross2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross2.tStartRefresh + 0.15-frameTolerance:
                # keep track of stop time/frame for later
                fix_cross2.tStop = t  # not accounting for scr refresh
                fix_cross2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross2, 'tStopRefresh')  # time at next scr refresh
                fix_cross2.setAutoDraw(False)
        
        # *asterisk* updates
        if asterisk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            asterisk.frameNStart = frameN  # exact frame index
            asterisk.tStart = t  # local t and not account for scr refresh
            asterisk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(asterisk, 'tStartRefresh')  # time at next scr refresh
            asterisk.setAutoDraw(True)
        if asterisk.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > asterisk.tStartRefresh + 0.15-frameTolerance:
                # keep track of stop time/frame for later
                asterisk.tStop = t  # not accounting for scr refresh
                asterisk.frameNStop = frameN  # exact frame index
                win.timeOnFlip(asterisk, 'tStopRefresh')  # time at next scr refresh
                asterisk.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cue"-------
    for thisComponent in cueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "fixation_2"-------
    continueRoutine = True
    routineTimer.add(0.450000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [fix_cross3]
    for thisComponent in fixation_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixation_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixation_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixation_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_cross3* updates
        if fix_cross3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_cross3.frameNStart = frameN  # exact frame index
            fix_cross3.tStart = t  # local t and not account for scr refresh
            fix_cross3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross3, 'tStartRefresh')  # time at next scr refresh
            fix_cross3.setAutoDraw(True)
        if fix_cross3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross3.tStartRefresh + 0.45-frameTolerance:
                # keep track of stop time/frame for later
                fix_cross3.tStop = t  # not accounting for scr refresh
                fix_cross3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross3, 'tStopRefresh')  # time at next scr refresh
                fix_cross3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation_2"-------
    for thisComponent in fixation_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "target"-------
    continueRoutine = True
    routineTimer.add(1.700000)
    # update component parameters for each repeat
    target_stimulus.setPos((Stimulus_X, Stimulus_Y))
    target_stimulus.setImage(Stimulus)
    response.keys = []
    response.rt = []
    _response_allKeys = []
    # keep track of which components have finished
    targetComponents = [fix_cross4, target_stimulus, response]
    for thisComponent in targetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    targetClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "target"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = targetClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=targetClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_cross4* updates
        if fix_cross4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_cross4.frameNStart = frameN  # exact frame index
            fix_cross4.tStart = t  # local t and not account for scr refresh
            fix_cross4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross4, 'tStartRefresh')  # time at next scr refresh
            fix_cross4.setAutoDraw(True)
        if fix_cross4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross4.tStartRefresh + 1.7-frameTolerance:
                # keep track of stop time/frame for later
                fix_cross4.tStop = t  # not accounting for scr refresh
                fix_cross4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross4, 'tStopRefresh')  # time at next scr refresh
                fix_cross4.setAutoDraw(False)
        
        # *target_stimulus* updates
        if target_stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            target_stimulus.frameNStart = frameN  # exact frame index
            target_stimulus.tStart = t  # local t and not account for scr refresh
            target_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_stimulus, 'tStartRefresh')  # time at next scr refresh
            target_stimulus.setAutoDraw(True)
        if target_stimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target_stimulus.tStartRefresh + 1.7-frameTolerance:
                # keep track of stop time/frame for later
                target_stimulus.tStop = t  # not accounting for scr refresh
                target_stimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target_stimulus, 'tStopRefresh')  # time at next scr refresh
                target_stimulus.setAutoDraw(False)
        
        # *response* updates
        waitOnFlip = False
        if response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response.frameNStart = frameN  # exact frame index
            response.tStart = t  # local t and not account for scr refresh
            response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
            response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response.tStartRefresh + 1.7-frameTolerance:
                # keep track of stop time/frame for later
                response.tStop = t  # not accounting for scr refresh
                response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(response, 'tStopRefresh')  # time at next scr refresh
                response.status = FINISHED
        if response.status == STARTED and not waitOnFlip:
            theseKeys = response.getKeys(keyList=['right', 'left'], waitRelease=False)
            _response_allKeys.extend(theseKeys)
            if len(_response_allKeys):
                response.keys = _response_allKeys[-1].name  # just the last key pressed
                response.rt = _response_allKeys[-1].rt
                # was this correct?
                if (response.keys == str(correctAns)) or (response.keys == correctAns):
                    response.corr = 1
                else:
                    response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in targetComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "target"-------
    for thisComponent in targetComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
           response.corr = 1;  # correct non-response
        else:
           response.corr = 0;  # failed to respond (incorrectly)
    # store data for Practise_loop (TrialHandler)
    Practise_loop.addData('response.keys',response.keys)
    Practise_loop.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        Practise_loop.addData('response.rt', response.rt)
    Practise_loop.addData('response.started', response.tStartRefresh)
    Practise_loop.addData('response.stopped', response.tStopRefresh)
    
    # ------Prepare to start Routine "response_feedback"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    if response.corr==1:
        feedback_img= feedback
        sound='Sounds/correct.wav'
    else:
        feedback_img=Stimulus
        sound='Sounds/incorrect.wav'
    feedback_image.setPos((Stimulus_X, Stimulus_Y))
    feedback_image.setImage(feedback_img)
    sounds.setSound(sound, secs=2, hamming=True)
    sounds.setVolume(1, log=False)
    # keep track of which components have finished
    response_feedbackComponents = [feedback_image, sounds]
    for thisComponent in response_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    response_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "response_feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = response_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=response_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_image* updates
        if feedback_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_image.frameNStart = frameN  # exact frame index
            feedback_image.tStart = t  # local t and not account for scr refresh
            feedback_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_image, 'tStartRefresh')  # time at next scr refresh
            feedback_image.setAutoDraw(True)
        if feedback_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_image.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback_image.tStop = t  # not accounting for scr refresh
                feedback_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_image, 'tStopRefresh')  # time at next scr refresh
                feedback_image.setAutoDraw(False)
        # start/stop sounds
        if sounds.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sounds.frameNStart = frameN  # exact frame index
            sounds.tStart = t  # local t and not account for scr refresh
            sounds.tStartRefresh = tThisFlipGlobal  # on global time
            sounds.play()  # start the sound (it finishes automatically)
        if sounds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sounds.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sounds.tStop = t  # not accounting for scr refresh
                sounds.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sounds, 'tStopRefresh')  # time at next scr refresh
                sounds.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in response_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "response_feedback"-------
    for thisComponent in response_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practise_loop.addData('feedback_image.started', feedback_image.tStartRefresh)
    Practise_loop.addData('feedback_image.stopped', feedback_image.tStopRefresh)
    sounds.stop()  # ensure sound has stopped at end of routine
    thisExp.nextEntry()
    
# completed 1 repeats of 'Practise_loop'


# ------Prepare to start Routine "Game_start"-------
continueRoutine = True
# update component parameters for each repeat
is_space7.keys = []
is_space7.rt = []
_is_space7_allKeys = []
# keep track of which components have finished
Game_startComponents = [image_7, is_space7]
for thisComponent in Game_startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Game_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Game_start"-------
while continueRoutine:
    # get current time
    t = Game_startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Game_startClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_7* updates
    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        image_7.setAutoDraw(True)
    
    # *is_space7* updates
    waitOnFlip = False
    if is_space7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        is_space7.frameNStart = frameN  # exact frame index
        is_space7.tStart = t  # local t and not account for scr refresh
        is_space7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(is_space7, 'tStartRefresh')  # time at next scr refresh
        is_space7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(is_space7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(is_space7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if is_space7.status == STARTED and not waitOnFlip:
        theseKeys = is_space7.getKeys(keyList=['space'], waitRelease=False)
        _is_space7_allKeys.extend(theseKeys)
        if len(_is_space7_allKeys):
            is_space7.keys = _is_space7_allKeys[-1].name  # just the last key pressed
            is_space7.rt = _is_space7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Game_startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Game_start"-------
for thisComponent in Game_startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Game_start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Main_loop = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Conditions.csv'),
    seed=None, name='Main_loop')
thisExp.addLoop(Main_loop)  # add the loop to the experiment
thisMain_loop = Main_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMain_loop.rgb)
if thisMain_loop != None:
    for paramName in thisMain_loop:
        exec('{} = thisMain_loop[paramName]'.format(paramName))

for thisMain_loop in Main_loop:
    currentLoop = Main_loop
    # abbreviate parameter names if possible (e.g. rgb = thisMain_loop.rgb)
    if thisMain_loop != None:
        for paramName in thisMain_loop:
            exec('{} = thisMain_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [fix_cross]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation"-------
    while continueRoutine:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_cross* updates
        if fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_cross.frameNStart = frameN  # exact frame index
            fix_cross.tStart = t  # local t and not account for scr refresh
            fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
            fix_cross.setAutoDraw(True)
        if fix_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross.tStartRefresh + random.uniform(0.4,1.6)-frameTolerance:
                # keep track of stop time/frame for later
                fix_cross.tStop = t  # not accounting for scr refresh
                fix_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross, 'tStopRefresh')  # time at next scr refresh
                fix_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "cue"-------
    continueRoutine = True
    routineTimer.add(0.150000)
    # update component parameters for each repeat
    asterisk.setPos((Cue_X, Cue_Y))
    # keep track of which components have finished
    cueComponents = [fix_cross2, asterisk]
    for thisComponent in cueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    cueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "cue"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = cueClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=cueClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_cross2* updates
        if fix_cross2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_cross2.frameNStart = frameN  # exact frame index
            fix_cross2.tStart = t  # local t and not account for scr refresh
            fix_cross2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross2, 'tStartRefresh')  # time at next scr refresh
            fix_cross2.setAutoDraw(True)
        if fix_cross2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross2.tStartRefresh + 0.15-frameTolerance:
                # keep track of stop time/frame for later
                fix_cross2.tStop = t  # not accounting for scr refresh
                fix_cross2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross2, 'tStopRefresh')  # time at next scr refresh
                fix_cross2.setAutoDraw(False)
        
        # *asterisk* updates
        if asterisk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            asterisk.frameNStart = frameN  # exact frame index
            asterisk.tStart = t  # local t and not account for scr refresh
            asterisk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(asterisk, 'tStartRefresh')  # time at next scr refresh
            asterisk.setAutoDraw(True)
        if asterisk.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > asterisk.tStartRefresh + 0.15-frameTolerance:
                # keep track of stop time/frame for later
                asterisk.tStop = t  # not accounting for scr refresh
                asterisk.frameNStop = frameN  # exact frame index
                win.timeOnFlip(asterisk, 'tStopRefresh')  # time at next scr refresh
                asterisk.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cue"-------
    for thisComponent in cueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "fixation_2"-------
    continueRoutine = True
    routineTimer.add(0.450000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [fix_cross3]
    for thisComponent in fixation_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixation_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixation_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixation_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_cross3* updates
        if fix_cross3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_cross3.frameNStart = frameN  # exact frame index
            fix_cross3.tStart = t  # local t and not account for scr refresh
            fix_cross3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross3, 'tStartRefresh')  # time at next scr refresh
            fix_cross3.setAutoDraw(True)
        if fix_cross3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross3.tStartRefresh + 0.45-frameTolerance:
                # keep track of stop time/frame for later
                fix_cross3.tStop = t  # not accounting for scr refresh
                fix_cross3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross3, 'tStopRefresh')  # time at next scr refresh
                fix_cross3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation_2"-------
    for thisComponent in fixation_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "target"-------
    continueRoutine = True
    routineTimer.add(1.700000)
    # update component parameters for each repeat
    target_stimulus.setPos((Stimulus_X, Stimulus_Y))
    target_stimulus.setImage(Stimulus)
    response.keys = []
    response.rt = []
    _response_allKeys = []
    # keep track of which components have finished
    targetComponents = [fix_cross4, target_stimulus, response]
    for thisComponent in targetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    targetClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "target"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = targetClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=targetClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_cross4* updates
        if fix_cross4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_cross4.frameNStart = frameN  # exact frame index
            fix_cross4.tStart = t  # local t and not account for scr refresh
            fix_cross4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross4, 'tStartRefresh')  # time at next scr refresh
            fix_cross4.setAutoDraw(True)
        if fix_cross4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross4.tStartRefresh + 1.7-frameTolerance:
                # keep track of stop time/frame for later
                fix_cross4.tStop = t  # not accounting for scr refresh
                fix_cross4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_cross4, 'tStopRefresh')  # time at next scr refresh
                fix_cross4.setAutoDraw(False)
        
        # *target_stimulus* updates
        if target_stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            target_stimulus.frameNStart = frameN  # exact frame index
            target_stimulus.tStart = t  # local t and not account for scr refresh
            target_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_stimulus, 'tStartRefresh')  # time at next scr refresh
            target_stimulus.setAutoDraw(True)
        if target_stimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target_stimulus.tStartRefresh + 1.7-frameTolerance:
                # keep track of stop time/frame for later
                target_stimulus.tStop = t  # not accounting for scr refresh
                target_stimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target_stimulus, 'tStopRefresh')  # time at next scr refresh
                target_stimulus.setAutoDraw(False)
        
        # *response* updates
        waitOnFlip = False
        if response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response.frameNStart = frameN  # exact frame index
            response.tStart = t  # local t and not account for scr refresh
            response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
            response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response.tStartRefresh + 1.7-frameTolerance:
                # keep track of stop time/frame for later
                response.tStop = t  # not accounting for scr refresh
                response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(response, 'tStopRefresh')  # time at next scr refresh
                response.status = FINISHED
        if response.status == STARTED and not waitOnFlip:
            theseKeys = response.getKeys(keyList=['right', 'left'], waitRelease=False)
            _response_allKeys.extend(theseKeys)
            if len(_response_allKeys):
                response.keys = _response_allKeys[-1].name  # just the last key pressed
                response.rt = _response_allKeys[-1].rt
                # was this correct?
                if (response.keys == str(correctAns)) or (response.keys == correctAns):
                    response.corr = 1
                else:
                    response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in targetComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "target"-------
    for thisComponent in targetComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
           response.corr = 1;  # correct non-response
        else:
           response.corr = 0;  # failed to respond (incorrectly)
    # store data for Main_loop (TrialHandler)
    Main_loop.addData('response.keys',response.keys)
    Main_loop.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        Main_loop.addData('response.rt', response.rt)
    Main_loop.addData('response.started', response.tStartRefresh)
    Main_loop.addData('response.stopped', response.tStopRefresh)
    
    # ------Prepare to start Routine "response_feedback"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    if response.corr==1:
        feedback_img= feedback
        sound='Sounds/correct.wav'
    else:
        feedback_img=Stimulus
        sound='Sounds/incorrect.wav'
    feedback_image.setPos((Stimulus_X, Stimulus_Y))
    feedback_image.setImage(feedback_img)
    sounds.setSound(sound, secs=2, hamming=True)
    sounds.setVolume(1, log=False)
    # keep track of which components have finished
    response_feedbackComponents = [feedback_image, sounds]
    for thisComponent in response_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    response_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "response_feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = response_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=response_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_image* updates
        if feedback_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_image.frameNStart = frameN  # exact frame index
            feedback_image.tStart = t  # local t and not account for scr refresh
            feedback_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_image, 'tStartRefresh')  # time at next scr refresh
            feedback_image.setAutoDraw(True)
        if feedback_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_image.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback_image.tStop = t  # not accounting for scr refresh
                feedback_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_image, 'tStopRefresh')  # time at next scr refresh
                feedback_image.setAutoDraw(False)
        # start/stop sounds
        if sounds.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sounds.frameNStart = frameN  # exact frame index
            sounds.tStart = t  # local t and not account for scr refresh
            sounds.tStartRefresh = tThisFlipGlobal  # on global time
            sounds.play()  # start the sound (it finishes automatically)
        if sounds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sounds.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                sounds.tStop = t  # not accounting for scr refresh
                sounds.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sounds, 'tStopRefresh')  # time at next scr refresh
                sounds.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in response_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "response_feedback"-------
    for thisComponent in response_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Main_loop.addData('feedback_image.started', feedback_image.tStartRefresh)
    Main_loop.addData('feedback_image.stopped', feedback_image.tStopRefresh)
    sounds.stop()  # ensure sound has stopped at end of routine
    
    # ------Prepare to start Routine "trial_break"-------
    continueRoutine = True
    # update component parameters for each repeat
    if Main_loop.thisN not in [24,48,62]:
        continueRoutine=False
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trial_breakComponents = [text, key_resp]
    for thisComponent in trial_breakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_breakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_break"-------
    while continueRoutine:
        # get current time
        t = trial_breakClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_breakClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_break"-------
    for thisComponent in trial_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Main_loop.addData('text.started', text.tStartRefresh)
    Main_loop.addData('text.stopped', text.tStopRefresh)
    # the Routine "trial_break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Main_loop'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text_2]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
