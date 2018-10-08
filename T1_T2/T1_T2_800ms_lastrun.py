#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.3),
    on October 04, 2018, at 10:16
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
expName = 'T1_T2_800ms'  # from the Builder filename that created this script
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
    originPath=u'F:\\Fixed\\Finalized_Psychopy\\T1_T2\\T1_T2_800ms.psyexp',
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

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Trial_Example"
Trial_ExampleClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "block_start_wait"
block_start_waitClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Get Ready!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=0.0);
Gray_Square_2 = visual.Rect(
    win=win, name='Gray_Square_2',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
Gray_Square3 = visual.Rect(
    win=win, name='Gray_Square3',
    width=(0.6, 0.6)[0], height=(0.6, 0.6)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text_3 = visual.TextStim(win=win, name='text_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-1.0);


# Initialize components for Routine "Trial_Creator"
Trial_CreatorClock = core.Clock()


# Initialize components for Routine "Trial"
TrialClock = core.Clock()
Gray_Square = visual.Rect(
    win=win, name='Gray_Square',
    width=(0.6, 0.6)[0], height=(0.6, 0.6)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
T1_text = visual.TextStim(win=win, name='T1_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-1.0);
T1_Delay = visual.TextStim(win=win, name='T1_Delay',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
T2_text = visual.TextStim(win=win, name='T2_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "A_B_query"
A_B_queryClock = core.Clock()
Gray_Square2 = visual.Rect(
    win=win, name='Gray_Square2',
    width=(0.6, 0.6)[0], height=(0.6, 0.6)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.506,0.506,0.506], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
X_or_Y = visual.TextStim(win=win, name='X_or_Y',
    text='X "[" key\n   or\nY "]" key)?\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-1.0);


# Initialize components for Routine "End_Task"
End_TaskClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Good job! You have completed this task. Please inform the researcher for further instructions. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
Block = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Blocks.xlsx'),
    seed=None, name='Block')
thisExp.addLoop(Block)  # add the loop to the experiment
thisBlock = Block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in Block:
    currentLoop = Block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instructions"-------
    t = 0
    InstructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text.setText(Task_Instructions)
    Task_Starter = event.BuilderKeyResponse()
    # keep track of which components have finished
    InstructionsComponents = [text, Task_Starter]
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Instructions"-------
    while continueRoutine:
        # get current time
        t = InstructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        
        # *Task_Starter* updates
        if t >= 0.0 and Task_Starter.status == NOT_STARTED:
            # keep track of start time/frame for later
            Task_Starter.tStart = t
            Task_Starter.frameNStart = frameN  # exact frame index
            Task_Starter.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if Task_Starter.status == STARTED:
            theseKeys = event.getKeys(keyList=['z'])
            
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
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instructions"-------
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Trial_Example"-------
    t = 0
    Trial_ExampleClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(Trial_example)
    Trial_starter = event.BuilderKeyResponse()
    # keep track of which components have finished
    Trial_ExampleComponents = [image, Trial_starter]
    for thisComponent in Trial_ExampleComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Trial_Example"-------
    while continueRoutine:
        # get current time
        t = Trial_ExampleClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # *Trial_starter* updates
        if t >= 0.0 and Trial_starter.status == NOT_STARTED:
            # keep track of start time/frame for later
            Trial_starter.tStart = t
            Trial_starter.frameNStart = frameN  # exact frame index
            Trial_starter.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if Trial_starter.status == STARTED:
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
        for thisComponent in Trial_ExampleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial_Example"-------
    for thisComponent in Trial_ExampleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Trial_Example" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "block_start_wait"-------
    t = 0
    block_start_waitClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    block_start_waitComponents = [text_4, Gray_Square_2]
    for thisComponent in block_start_waitComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "block_start_wait"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = block_start_waitClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_4.status == STARTED and t >= frameRemains:
            text_4.setAutoDraw(False)
        
        # *Gray_Square_2* updates
        if t >= 0.0 and Gray_Square_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Gray_Square_2.tStart = t
            Gray_Square_2.frameNStart = frameN  # exact frame index
            Gray_Square_2.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Gray_Square_2.status == STARTED and t >= frameRemains:
            Gray_Square_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_start_waitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block_start_wait"-------
    for thisComponent in block_start_waitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=TrialNumber, method='sequential', 
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
        
        # ------Prepare to start Routine "ISI"-------
        t = 0
        ISIClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        ISI_Dur = 1 + random()*1
        # keep track of which components have finished
        ISIComponents = [Gray_Square3, text_3]
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ISI"-------
        while continueRoutine:
            # get current time
            t = ISIClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Gray_Square3* updates
            if t >= 0.0 and Gray_Square3.status == NOT_STARTED:
                # keep track of start time/frame for later
                Gray_Square3.tStart = t
                Gray_Square3.frameNStart = frameN  # exact frame index
                Gray_Square3.setAutoDraw(True)
            frameRemains = 0.0 + ISI_Dur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Gray_Square3.status == STARTED and t >= frameRemains:
                Gray_Square3.setAutoDraw(False)
            
            # *text_3* updates
            if t >= 0.0 and text_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_3.tStart = t
                text_3.frameNStart = frameN  # exact frame index
                text_3.setAutoDraw(True)
            frameRemains = 0.0 + ISI_Dur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_3.status == STARTED and t >= frameRemains:
                text_3.setAutoDraw(False)
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Trial_Creator"-------
        t = 0
        Trial_CreatorClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        
        T1code = randint(1,4)
        T2code = randint(1,3)
        
        if T1code == 1:
            T1 = 'X'
            T1corr_resp = 'bracketleft'
            trials.addData('T1', 'X')
        
        if T1code == 2:
            T1 = 'Y'
            T1corr_resp = 'bracketright'
            trials.addData('T1', 'Y')
        
        if T1code == 3:
            T1 = '#'
            T1corr_resp = 'none'
            trials.addData('T1', '#')
        
        
        if T2code == 1:
            T2 = '1'
            T2corr_resp = 'left'
            trials.addData('T2', '1')
        
        if T2code == 2:
            T2 = '2'
            T2corr_resp = 'right'
            trials.addData('T2', '2')
        
        
        # keep track of which components have finished
        Trial_CreatorComponents = []
        for thisComponent in Trial_CreatorComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Trial_Creator"-------
        while continueRoutine:
            # get current time
            t = Trial_CreatorClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Trial_CreatorComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Trial_Creator"-------
        for thisComponent in Trial_CreatorComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "Trial_Creator" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Trial"-------
        t = 0
        TrialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        T1_text.setText(T1)
        T2_text.setText(T2)
        T2_Resp = event.BuilderKeyResponse()
        # keep track of which components have finished
        TrialComponents = [Gray_Square, T1_text, T1_Delay, T2_text, T2_Resp]
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Trial"-------
        while continueRoutine:
            # get current time
            t = TrialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Gray_Square* updates
            if t >= 0.0 and Gray_Square.status == NOT_STARTED:
                # keep track of start time/frame for later
                Gray_Square.tStart = t
                Gray_Square.frameNStart = frameN  # exact frame index
                Gray_Square.setAutoDraw(True)
            
            # *T1_text* updates
            if t >= 0.0 and T1_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                T1_text.tStart = t
                T1_text.frameNStart = frameN  # exact frame index
                T1_text.setAutoDraw(True)
            frameRemains = 0.0 + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if T1_text.status == STARTED and t >= frameRemains:
                T1_text.setAutoDraw(False)
            
            # *T1_Delay* updates
            if t >= 0.1 and T1_Delay.status == NOT_STARTED:
                # keep track of start time/frame for later
                T1_Delay.tStart = t
                T1_Delay.frameNStart = frameN  # exact frame index
                T1_Delay.setAutoDraw(True)
            frameRemains = 0.1 + 0.80- win.monitorFramePeriod * 0.75  # most of one frame period left
            if T1_Delay.status == STARTED and t >= frameRemains:
                T1_Delay.setAutoDraw(False)
            
            # *T2_text* updates
            if (T1_Delay.status == FINISHED) and T2_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                T2_text.tStart = t
                T2_text.frameNStart = frameN  # exact frame index
                T2_text.setAutoDraw(True)
            
            # *T2_Resp* updates
            if (T2_text.status == STARTED) and T2_Resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                T2_Resp.tStart = t
                T2_Resp.frameNStart = frameN  # exact frame index
                T2_Resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(T2_Resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if T2_Resp.status == STARTED:
                theseKeys = event.getKeys()
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    T2_Resp.keys = theseKeys[-1]  # just the last key pressed
                    T2_Resp.rt = T2_Resp.clock.getTime()
                    # was this 'correct'?
                    if (T2_Resp.keys == str(T2corr_resp)) or (T2_Resp.keys == T2corr_resp):
                        T2_Resp.corr = 1
                    else:
                        T2_Resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Trial"-------
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if T2_Resp.keys in ['', [], None]:  # No response was made
            T2_Resp.keys=None
            # was no response the correct answer?!
            if str(T2corr_resp).lower() == 'none':
               T2_Resp.corr = 1  # correct non-response
            else:
               T2_Resp.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('T2_Resp.keys',T2_Resp.keys)
        trials.addData('T2_Resp.corr', T2_Resp.corr)
        if T2_Resp.keys != None:  # we had a response
            trials.addData('T2_Resp.rt', T2_Resp.rt)
        # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "A_B_query"-------
        t = 0
        A_B_queryClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        if T1 == '#':
            continueRoutine = False 
        
        if Block_type == 'Ignore_T1':
            continueRoutine = False 
        
        else:
            stim_dur = 999
        T1_Resp = event.BuilderKeyResponse()
        # keep track of which components have finished
        A_B_queryComponents = [Gray_Square2, X_or_Y, T1_Resp]
        for thisComponent in A_B_queryComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "A_B_query"-------
        while continueRoutine:
            # get current time
            t = A_B_queryClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Gray_Square2* updates
            if t >= 0.0 and Gray_Square2.status == NOT_STARTED:
                # keep track of start time/frame for later
                Gray_Square2.tStart = t
                Gray_Square2.frameNStart = frameN  # exact frame index
                Gray_Square2.setAutoDraw(True)
            frameRemains = 0.0 + stim_dur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Gray_Square2.status == STARTED and t >= frameRemains:
                Gray_Square2.setAutoDraw(False)
            
            # *X_or_Y* updates
            if t >= 0 and X_or_Y.status == NOT_STARTED:
                # keep track of start time/frame for later
                X_or_Y.tStart = t
                X_or_Y.frameNStart = frameN  # exact frame index
                X_or_Y.setAutoDraw(True)
            frameRemains = 0 + stim_dur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if X_or_Y.status == STARTED and t >= frameRemains:
                X_or_Y.setAutoDraw(False)
            
            
            # *T1_Resp* updates
            if (X_or_Y.status == STARTED) and T1_Resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                T1_Resp.tStart = t
                T1_Resp.frameNStart = frameN  # exact frame index
                T1_Resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(T1_Resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if T1_Resp.status == STARTED and t >= (T1_Resp.tStart + stim_dur):
                T1_Resp.status = STOPPED
            if T1_Resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['bracketleft', 'bracketright'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    T1_Resp.keys = theseKeys[-1]  # just the last key pressed
                    T1_Resp.rt = T1_Resp.clock.getTime()
                    # was this 'correct'?
                    if (T1_Resp.keys == str(T1corr_resp)) or (T1_Resp.keys == T1corr_resp):
                        T1_Resp.corr = 1
                    else:
                        T1_Resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in A_B_queryComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "A_B_query"-------
        for thisComponent in A_B_queryComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # check responses
        if T1_Resp.keys in ['', [], None]:  # No response was made
            T1_Resp.keys=None
            # was no response the correct answer?!
            if str(T1corr_resp).lower() == 'none':
               T1_Resp.corr = 1  # correct non-response
            else:
               T1_Resp.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('T1_Resp.keys',T1_Resp.keys)
        trials.addData('T1_Resp.corr', T1_Resp.corr)
        if T1_Resp.keys != None:  # we had a response
            trials.addData('T1_Resp.rt', T1_Resp.rt)
        # the Routine "A_B_query" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed TrialNumber repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'Block'


# ------Prepare to start Routine "End_Task"-------
t = 0
End_TaskClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Task_Ender = event.BuilderKeyResponse()
# keep track of which components have finished
End_TaskComponents = [text_2, Task_Ender]
for thisComponent in End_TaskComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "End_Task"-------
while continueRoutine:
    # get current time
    t = End_TaskClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *Task_Ender* updates
    if t >= 0.0 and Task_Ender.status == NOT_STARTED:
        # keep track of start time/frame for later
        Task_Ender.tStart = t
        Task_Ender.frameNStart = frameN  # exact frame index
        Task_Ender.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(Task_Ender.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if Task_Ender.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Task_Ender.keys = theseKeys[-1]  # just the last key pressed
            Task_Ender.rt = Task_Ender.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in End_TaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End_Task"-------
for thisComponent in End_TaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Task_Ender.keys in ['', [], None]:  # No response was made
    Task_Ender.keys=None
thisExp.addData('Task_Ender.keys',Task_Ender.keys)
if Task_Ender.keys != None:  # we had a response
    thisExp.addData('Task_Ender.rt', Task_Ender.rt)
thisExp.nextEntry()
# the Routine "End_Task" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()



# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
