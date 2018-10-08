#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.3),
    on October 03, 2018, at 00:42
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'PY2_shuffler_SSD_arrow_variant_ISI_staircase'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'F:\\Fixed\\Finalized_Psychopy\\SST\\PY2_shuffler_SSD_arrow_variant_ISI_staircase.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 1024], fullscr=True, screen=1,
    allowGUI=False, allowStencil=False,
    monitor='Real_Monitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Start_Instructions"
Start_InstructionsClock = core.Clock()
Task_Start_Instructions = visual.TextStim(win=win, name='Task_Start_Instructions',
    text='Thank you for participating in this experiment!\n\nIn the upcoming task you will be presented with a series of green arrows, each facing to the right or to the left. Your task is to respond as quickly and as accurately as possible to these stimuli by pressing the "z" key for arrows facing to your left and the "/" (slash) key for arrows facing to your right. Please place your left and right index fingers on each respective key. The slash key is on the same row as the Z key.\n\nOccasionally, an arrow will be followed by a red stop sign. If you see such a sign, your task is to NOT respond on that trial (i.e. do not press the z or / key on that trial). On some trials, these signs will be presented soon after the arrow, making it easy to stop your response. On other trials, the sign will be presented late, making it very difficult to stop your response.\n\nNevertheless, it is important that you DO NOT WAIT for a stop signal to occur. Feedback will be provided to you if you take too long to respond to a specific trial.\n\nPress the "/" key to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
#task_stimuli_parameters
Go_stimuli_ms = 16
Initial_SSD_SOA_ms = 16
fixation_min_ms = 16
fixation_max_ms = 16
FeedbackDur_ms = 16
fixation_degrees = 1.5
go_size_degrees = 1.75
Stop_stim_degrees = 1.75
Feedback_Color = 'red'
ISI_min_ms = 16
ISI_max_ms = 16

#conversions to frames and misc intializations
Go_too_slow_N = 0
Go_Frames_Dur = round(Go_stimuli_ms/(1000/expInfo['frameRate']),0)
SSD_SOA_Frames = round(Initial_SSD_SOA_ms/(1000/expInfo['frameRate']),0)
fixation_min_frames = round(fixation_min_ms/(1000/expInfo['frameRate']),0)
fixation_max_frames = round(fixation_max_ms/(1000/expInfo['frameRate']),0)
FeedbackDur_frames =  round(FeedbackDur_ms/(1000/expInfo['frameRate']),0)
ISI_min_frames = round(ISI_min_ms/(1000/expInfo['frameRate']),0)
ISI_max_frames = round(ISI_max_ms/(1000/expInfo['frameRate']),0)

#Initializes stimuli parameters of the experiment save for stimuli 
#position. Stimuli durations are in millisecond units (subsequently 
#converted to frames) while sizes are in visual angle degree units 
#at screen center. Note: monitor framerate is recorded directly from 
#the screen at the start of the experiment and used to calculate 
#actual frame durations. 

import psychopy.core
clock = psychopy.core.Clock()

# Initialize components for Routine "Block_Initializer"
Block_InitializerClock = core.Clock()

BlockInstructions = visual.TextStim(win=win, name='BlockInstructions',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
Get_Ready = visual.TextStim(win=win, name='Get_Ready',
    text='Get Ready!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "Trial_initalizer"
Trial_initalizerClock = core.Clock()


# Initialize components for Routine "trial"
trialClock = core.Clock()

fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='cross',units='deg', 
    size=(1.0, 1.0),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
StopSign = visual.ImageStim(
    win=win, name='StopSign',units='deg', 
    image='Stop_Sign.png', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Go_arrow = visual.ImageStim(
    win=win, name='Go_arrow',units='deg', 
    image='Arrow.png', mask=None,
    ori=1.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()

Feedback = visual.TextStim(win=win, name='Feedback',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-1.0);
FeedbackLine2 = visual.TextStim(win=win, name='FeedbackLine2',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-2.0);
StopSign_Feedback = visual.ImageStim(
    win=win, name='StopSign_Feedback',units='deg', 
    image='Stop_Sign.png', mask=None,
    ori=0, pos=(0, 0), size=(1.75, 1.75),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "Block_End_Test"
Block_End_TestClock = core.Clock()

text = visual.TextStim(win=win, name='text',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "End_Instructions"
End_InstructionsClock = core.Clock()
Task_End_Instructions = visual.TextStim(win=win, name='Task_End_Instructions',
    text='You have completed this task!\n\nPlease inform the experimenter',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Start_Instructions"-------
t = 0
Start_InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Task_Start_Resp = event.BuilderKeyResponse()

# keep track of which components have finished
Start_InstructionsComponents = [Task_Start_Instructions, Task_Start_Resp]
for thisComponent in Start_InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_Instructions"-------
while continueRoutine:
    # get current time
    t = Start_InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Task_Start_Instructions* updates
    if t >= 0.0 and Task_Start_Instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        Task_Start_Instructions.tStart = t
        Task_Start_Instructions.frameNStart = frameN  # exact frame index
        Task_Start_Instructions.setAutoDraw(True)
    
    # *Task_Start_Resp* updates
    if t >= 0.0 and Task_Start_Resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        Task_Start_Resp.tStart = t
        Task_Start_Resp.frameNStart = frameN  # exact frame index
        Task_Start_Resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if Task_Start_Resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['slash'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_Instructions"-------
for thisComponent in Start_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Start_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Block_Loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Blocked_Conditions.xlsx'),
    seed=None, name='Block_Loop')
thisExp.addLoop(Block_Loop)  # add the loop to the experiment
thisBlock_Loop = Block_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_Loop.rgb)
if thisBlock_Loop != None:
    for paramName in thisBlock_Loop:
        exec('{} = thisBlock_Loop[paramName]'.format(paramName))

for thisBlock_Loop in Block_Loop:
    currentLoop = Block_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_Loop.rgb)
    if thisBlock_Loop != None:
        for paramName in thisBlock_Loop:
            exec('{} = thisBlock_Loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Block_Initializer"-------
    t = 0
    Block_InitializerClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    goarray = ['GO'] * NGo_Trials
    stoparray = ['STOP'] * NSSD_Trials
    trialarray = goarray + stoparray
    shuffle(trialarray)
    totaltrialnumber = len(trialarray)
    trialnum = 0
    
    thisExp.addData('clocktime',clock.getTime())
    BlockInstructions.setText(Block_Instructions)
    # keep track of which components have finished
    Block_InitializerComponents = [BlockInstructions, Get_Ready]
    for thisComponent in Block_InitializerComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Block_Initializer"-------
    while continueRoutine:
        # get current time
        t = Block_InitializerClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *BlockInstructions* updates
        if t >= 0.0 and BlockInstructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            BlockInstructions.tStart = t
            BlockInstructions.frameNStart = frameN  # exact frame index
            BlockInstructions.setAutoDraw(True)
        frameRemains = 0.0 + Block_Instructions_dur- win.monitorFramePeriod * 0.75  # most of one frame period left
        if BlockInstructions.status == STARTED and t >= frameRemains:
            BlockInstructions.setAutoDraw(False)
        
        # *Get_Ready* updates
        if t >= Block_Instructions_dur and Get_Ready.status == NOT_STARTED:
            # keep track of start time/frame for later
            Get_Ready.tStart = t
            Get_Ready.frameNStart = frameN  # exact frame index
            Get_Ready.setAutoDraw(True)
        frameRemains = Block_Instructions_dur + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Get_Ready.status == STARTED and t >= frameRemains:
            Get_Ready.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block_InitializerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block_Initializer"-------
    for thisComponent in Block_InitializerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "Block_Initializer" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=(NGo_Trials * 2) + NSSD_Trials, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Trial_initalizer"-------
        t = 0
        Trial_initalizerClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        #Initializes specific trial parameter values based on trial type. 
        #Currently set to output more data than necessary for debugging. 
        
        if trialarray[0] == 'GO':
            trial_type = 'GO'
            Trial_SSD_Frames_Dur = 0
            Trial_Go_Frames_Dur = Go_Frames_Dur - Trial_SSD_Frames_Dur
            trials.addData('trial_type', trial_type)
            trials.addData('SSD_SOA_Frames', SSD_SOA_Frames)
            trials.addData('fixation_min_frames', fixation_min_frames)
            trials.addData('fixation_max_frames', fixation_max_frames)
            trials.addData('Trial_SSD_Frames_Dur', Trial_SSD_Frames_Dur)
            trials.addData('Trial_Go_Frames_Dur', Trial_Go_Frames_Dur)
            trials.addData('NGo_Trials', NGo_Trials)
            trials.addData('NSSD_Trials', NSSD_Trials)
        
        if trialarray[0] == 'STOP':
            trial_type = 'STOP'
            Trial_SSD_Frames_Dur = Go_Frames_Dur - SSD_SOA_Frames 
            Trial_Go_Frames_Dur = Go_Frames_Dur - Trial_SSD_Frames_Dur
            trials.addData('trial_type', trial_type)
            trials.addData('SSD_SOA_Frames', SSD_SOA_Frames)
            trials.addData('fixation_min_frames', fixation_min_frames)
            trials.addData('fixation_max_frames', fixation_max_frames)
            trials.addData('Trial_SSD_Frames_Dur', Trial_SSD_Frames_Dur)
            trials.addData('Trial_Go_Frames_Dur', Trial_Go_Frames_Dur)
            trials.addData('NGo_Trials', NGo_Trials)
            trials.addData('NSSD_Trials', NSSD_Trials)
        
        trialarray.pop(0)
        # keep track of which components have finished
        Trial_initalizerComponents = []
        for thisComponent in Trial_initalizerComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Trial_initalizer"-------
        while continueRoutine:
            # get current time
            t = Trial_initalizerClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Trial_initalizerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Trial_initalizer"-------
        for thisComponent in Trial_initalizerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trialnum = trialnum + 1
        # the Routine "Trial_initalizer" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        if random() <= 0.5:
            Arrow_ori = -90
            corr_response = 'z'
        
        else :
            Arrow_ori = 90
            corr_response= 'slash'
        
        if trial_type == 'STOP':
            corr_response = 'None'
        
        trials.addData('corr_response', corr_response)
        fixation.setSize((fixation_degrees, fixation_degrees))
        StopSign.setSize((Stop_stim_degrees, Stop_stim_degrees))
        GO_SST_RESP = event.BuilderKeyResponse()
        STOP_SST_RESP = event.BuilderKeyResponse()
        Go_arrow.setOri(Arrow_ori)
        Go_arrow.setSize((go_size_degrees,go_size_degrees))
        # keep track of which components have finished
        trialComponents = [fixation, StopSign, GO_SST_RESP, STOP_SST_RESP, Go_arrow]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if GO_SST_RESP.status == FINISHED:
                continueRoutine = False 
            
            if STOP_SST_RESP.status == FINISHED:
                continueRoutine = False 
            
            # *fixation* updates
            if t >= 0.0 and fixation.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation.tStart = t
                fixation.frameNStart = frameN  # exact frame index
                fixation.setAutoDraw(True)
            if fixation.status == STARTED and frameN >= (fixation.frameNStart + fixation_min_frames+ random()*(fixation_max_frames - fixation_min_frames)):
                fixation.setAutoDraw(False)
            
            # *StopSign* updates
            if (trial_type == 'STOP' and Go_arrow.status == FINISHED) and StopSign.status == NOT_STARTED:
                # keep track of start time/frame for later
                StopSign.tStart = t
                StopSign.frameNStart = frameN  # exact frame index
                StopSign.setAutoDraw(True)
            if StopSign.status == STARTED and frameN >= (StopSign.frameNStart + Trial_SSD_Frames_Dur):
                StopSign.setAutoDraw(False)
            
            # *GO_SST_RESP* updates
            if (trial_type == 'GO'and fixation.status == FINISHED) and GO_SST_RESP.status == NOT_STARTED:
                # keep track of start time/frame for later
                GO_SST_RESP.tStart = t
                GO_SST_RESP.frameNStart = frameN  # exact frame index
                GO_SST_RESP.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(GO_SST_RESP.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if GO_SST_RESP.status == STARTED and frameN >= (GO_SST_RESP.frameNStart + Trial_Go_Frames_Dur + Trial_SSD_Frames_Dur):
                GO_SST_RESP.status = STOPPED
            if GO_SST_RESP.status == STARTED:
                theseKeys = event.getKeys(keyList=['z', 'slash'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if GO_SST_RESP.keys == []:  # then this was the first keypress
                        GO_SST_RESP.keys = theseKeys[0]  # just the first key pressed
                        GO_SST_RESP.rt = GO_SST_RESP.clock.getTime()
                        # was this 'correct'?
                        if (GO_SST_RESP.keys == str(corr_response)) or (GO_SST_RESP.keys == corr_response):
                            GO_SST_RESP.corr = 1
                        else:
                            GO_SST_RESP.corr = 0
            
            # *STOP_SST_RESP* updates
            if (trial_type == 'STOP' and fixation.status == FINISHED) and STOP_SST_RESP.status == NOT_STARTED:
                # keep track of start time/frame for later
                STOP_SST_RESP.tStart = t
                STOP_SST_RESP.frameNStart = frameN  # exact frame index
                STOP_SST_RESP.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(STOP_SST_RESP.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if STOP_SST_RESP.status == STARTED and frameN >= (STOP_SST_RESP.frameNStart + Trial_Go_Frames_Dur + Trial_SSD_Frames_Dur):
                STOP_SST_RESP.status = STOPPED
            if STOP_SST_RESP.status == STARTED:
                theseKeys = event.getKeys(keyList=['z', 'slash'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    STOP_SST_RESP.keys = theseKeys[-1]  # just the last key pressed
                    STOP_SST_RESP.rt = STOP_SST_RESP.clock.getTime()
                    # was this 'correct'?
                    if (STOP_SST_RESP.keys == str(corr_response)) or (STOP_SST_RESP.keys == corr_response):
                        STOP_SST_RESP.corr = 1
                    else:
                        STOP_SST_RESP.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *Go_arrow* updates
            if (fixation.status == FINISHED) and Go_arrow.status == NOT_STARTED:
                # keep track of start time/frame for later
                Go_arrow.tStart = t
                Go_arrow.frameNStart = frameN  # exact frame index
                Go_arrow.setAutoDraw(True)
            if Go_arrow.status == STARTED and frameN >= (Go_arrow.frameNStart + Trial_Go_Frames_Dur):
                Go_arrow.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # check responses
        if GO_SST_RESP.keys in ['', [], None]:  # No response was made
            GO_SST_RESP.keys=None
            # was no response the correct answer?!
            if str(corr_response).lower() == 'none':
               GO_SST_RESP.corr = 1  # correct non-response
            else:
               GO_SST_RESP.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('GO_SST_RESP.keys',GO_SST_RESP.keys)
        trials.addData('GO_SST_RESP.corr', GO_SST_RESP.corr)
        if GO_SST_RESP.keys != None:  # we had a response
            trials.addData('GO_SST_RESP.rt', GO_SST_RESP.rt)
        # check responses
        if STOP_SST_RESP.keys in ['', [], None]:  # No response was made
            STOP_SST_RESP.keys=None
            # was no response the correct answer?!
            if str(corr_response).lower() == 'none':
               STOP_SST_RESP.corr = 1  # correct non-response
            else:
               STOP_SST_RESP.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('STOP_SST_RESP.keys',STOP_SST_RESP.keys)
        trials.addData('STOP_SST_RESP.corr', STOP_SST_RESP.corr)
        if STOP_SST_RESP.keys != None:  # we had a response
            trials.addData('STOP_SST_RESP.rt', STOP_SST_RESP.rt)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "feedback"-------
        t = 0
        feedbackClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        if trial_type == 'GO' and GO_SST_RESP.keys == 'slash' :
            FeedbackPos1 = (0,0)
            FeedbackPos2 = (0,0)
            Feedbackmsg1 = ''
            Feedbackmsg2 = ''
            Sign_present = 0
            continueRoutine = False 
        
        if trial_type == 'GO' and GO_SST_RESP.keys == 'z' :
            FeedbackPos1 = (0,0)
            FeedbackPos2 = (0,0)
            Feedbackmsg1 = ''
            Feedbackmsg2 = ''
            Sign_present = 0
            continueRoutine = False 
        
        if trial_type == 'STOP' and STOP_SST_RESP.corr == 1:
            trials.addData('STOPfeedbackran', 'No')
            FeedbackPos1 = (0,0)
            FeedbackPos2 = (0,0)
            Feedbackmsg1 = ''
            Feedbackmsg2 = ''
            Sign_present = 0
            SSD_SOA_Frames = SSD_SOA_Frames + 3
            continueRoutine = False 
        
        if trial_type == 'GO' and GO_SST_RESP.keys == None :
            Go_too_slow_N = Go_too_slow_N +1
            FeedbackPos1 = (0,0)
            Feedbackmsg2 = 'Faster'
            FeedbackPos2 = (0, -.1)
            Sign_present = 0
            trials.addData('GoFeedbackDur_frames', FeedbackDur_frames)
        
        if trial_type == 'STOP' and STOP_SST_RESP.corr == 0:
            trials.addData('STOPfeedbackran', 'Yes')
            FeedbackPos1 = (0,0.2)
            Feedbackmsg2 = ''
            FeedbackPos2 = (0, -.1)
            Sign_present = 1
            SSD_SOA_Frames = SSD_SOA_Frames - 3
            trials.addData('Stop_feedback_Frames', FeedbackDur_frames)
        
        ISI_dur = ISI_min_frames+ random()*(ISI_max_frames - ISI_min_frames)
        trials.addData('ISI_duration', ISI_dur)
        
        if Go_too_slow_N == 3:
            Go_too_slow_N = 0
            trialarray.append('GO')
            shuffle(trialarray)
            totaltrialnumber = totaltrialnumber+1
        Feedback.setColor(Feedback_Color, colorSpace='rgb')
        Feedback.setText('X')
        Feedback.setPos(FeedbackPos1)
        FeedbackLine2.setColor(Feedback_Color, colorSpace='rgb')
        FeedbackLine2.setText(Feedbackmsg2)
        FeedbackLine2.setPos(FeedbackPos2)
        StopSign_Feedback.setOpacity(Sign_present)
        # keep track of which components have finished
        feedbackComponents = [Feedback, FeedbackLine2, StopSign_Feedback]
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "feedback"-------
        while continueRoutine:
            # get current time
            t = feedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *Feedback* updates
            if t >= 0.0 and Feedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                Feedback.tStart = t
                Feedback.frameNStart = frameN  # exact frame index
                Feedback.setAutoDraw(True)
            if Feedback.status == STARTED and frameN >= (Feedback.frameNStart + FeedbackDur_frames):
                Feedback.setAutoDraw(False)
            
            # *FeedbackLine2* updates
            if t >= 0.0 and FeedbackLine2.status == NOT_STARTED:
                # keep track of start time/frame for later
                FeedbackLine2.tStart = t
                FeedbackLine2.frameNStart = frameN  # exact frame index
                FeedbackLine2.setAutoDraw(True)
            if FeedbackLine2.status == STARTED and frameN >= (FeedbackLine2.frameNStart + FeedbackDur_frames):
                FeedbackLine2.setAutoDraw(False)
            
            # *StopSign_Feedback* updates
            if t >= 0.0 and StopSign_Feedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                StopSign_Feedback.tStart = t
                StopSign_Feedback.frameNStart = frameN  # exact frame index
                StopSign_Feedback.setAutoDraw(True)
            if StopSign_Feedback.status == STARTED and frameN >= (StopSign_Feedback.frameNStart + FeedbackDur_frames):
                StopSign_Feedback.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Block_End_Test"-------
        t = 0
        Block_End_TestClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        trials.addData('lenarray', len(trialarray))
        trials.addData('trialnum', trialnum)
        trials.addData('Go_too_slow_N', Go_too_slow_N)
        
        if trialnum == totaltrialnumber:
            trials.finished=1
        
        if SSD_SOA_Frames < 3:
            SSD_SOA_Frames = 3
        
        if SSD_SOA_Frames > 39:
            SSD_SOA_Frames = 39
        
        
        # keep track of which components have finished
        Block_End_TestComponents = [text]
        for thisComponent in Block_End_TestComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Block_End_Test"-------
        while continueRoutine:
            # get current time
            t = Block_End_TestClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if text.status == FINISHED:
                continueRoutine = False 
            
            # *text* updates
            if t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t
                text.frameNStart = frameN  # exact frame index
                text.setAutoDraw(True)
            if text.status == STARTED and frameN >= (text.frameNStart + ISI_dur):
                text.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Block_End_TestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Block_End_Test"-------
        for thisComponent in Block_End_TestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "Block_End_Test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed (NGo_Trials * 2) + NSSD_Trials repeats of 'trials'
    
# completed 1 repeats of 'Block_Loop'


# ------Prepare to start Routine "End_Instructions"-------
t = 0
End_InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Task_End_Response = event.BuilderKeyResponse()
thisExp.addData('clocktime',clock.getTime())
# keep track of which components have finished
End_InstructionsComponents = [Task_End_Instructions, Task_End_Response]
for thisComponent in End_InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "End_Instructions"-------
while continueRoutine:
    # get current time
    t = End_InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Task_End_Instructions* updates
    if t >= 0.0 and Task_End_Instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        Task_End_Instructions.tStart = t
        Task_End_Instructions.frameNStart = frameN  # exact frame index
        Task_End_Instructions.setAutoDraw(True)
    
    # *Task_End_Response* updates
    if t >= 0.0 and Task_End_Response.status == NOT_STARTED:
        # keep track of start time/frame for later
        Task_End_Response.tStart = t
        Task_End_Response.frameNStart = frameN  # exact frame index
        Task_End_Response.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if Task_End_Response.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in End_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End_Instructions"-------
for thisComponent in End_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "End_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()







# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
