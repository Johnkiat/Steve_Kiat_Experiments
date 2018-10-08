#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.3),
    on October 08, 2018, at 15:07
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
expName = 'Gradual_Change_fader'  # from the Builder filename that created this script
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
    originPath=u'C:\\Users\\JohnKiat\\Documents\\Steve_Kiat_Projects\\Change_Blindness\\Gradual_Change_fader.psyexp',
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
    monitor='Real_Monitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Task_Start"
Task_StartClock = core.Clock()
changetime = 12
nochangetime = 3.14

imagenumarray =['0001','0002','0004','0005','0006','0008','0009','0011','0014','0016','0018','0019','0022','0023','0024','0028','0029','0031','0038','0039','0040','0041','0044','0045','0048','0049','0050','0051','0052','0054','0055','0056','0058','0060','0066','0067','0069','0070','0071','0074','0075','0076','0078','0079','0080','0084','0087','0089','0093','0097','0098','0099','0100','0102','0106','0107','0109','0110','0111','0112','0114','0116','0117','0118','0119','0122','0123','0124','0125','0126','0127','0128']
shuffle(imagenumarray)
Task_Instructions = visual.TextStim(win=win, name='Task_Instructions',
    text="In this task you will be presented with photographs of various scenes. In some of these scenes, a specific object in the scene may periodically appear or disappear several times in a row. Your task is to press the 'spacebar' key AS SOON AS you see such a change occuring. After making that response, you will be asked to left-click on where the change occured with the mouse. Do remember to press the spacebar AS SOON as you actually see the change though as that response is what will determine your score! It is not important to click on the location quickly but it is important to press the spacebar as soon as you see a change. Press the spacebar to see a few examples of these changes.",
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "Examples"
ExamplesClock = core.Clock()
ExampleImage1 = visual.ImageStim(
    win=win, name='ExampleImage1',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1024, 768),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ExampleImage2 = visual.ImageStim(
    win=win, name='ExampleImage2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1024, 768),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

mouse = event.Mouse(win=win)
x, y = [None, None]
text_4 = visual.TextStim(win=win, name='text_4',
    text='Click on where the change is! or (outside the image if there is no change)',
    font='Arial',
    pos=(0, 0.9), height=0.05, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-5.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='Press the Spacebar when you see changes like this! Try it now.',
    font='Arial',
    pos=(0, -.90), height=0.05, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-6.0);

# Initialize components for Routine "Get_ready"
Get_readyClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Get ready for the actual trials!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial_initalizer"
trial_initalizerClock = core.Clock()


# Initialize components for Routine "Trial"
TrialClock = core.Clock()
Image1 = visual.ImageStim(
    win=win, name='Image1',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1024, 768),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Image2 = visual.ImageStim(
    win=win, name='Image2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1024, 768),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

Trial_type = visual.TextStim(win=win, name='Trial_type',
    text=None,
    font='Arial',
    pos=(0, -.90), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-3.0);
Changedetected = visual.TextStim(win=win, name='Changedetected',
    text='Click on where the change is! or (outside the image if there is no change)',
    font='Arial',
    pos=(0, 0.9), height=0.05, wrapWidth=100, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1.0,
    depth=-5.0);
Mouse_Click_Location = event.Mouse(win=win)
x, y = [None, None]

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=0.0);

text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "Task_End"
Task_EndClock = core.Clock()
End_task_instructions = visual.TextStim(win=win, name='End_task_instructions',
    text='Good job! You have completed this task. Please contact the experimenter for further instructions.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Task_Start"-------
t = 0
Task_StartClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

Start_Task = event.BuilderKeyResponse()
# keep track of which components have finished
Task_StartComponents = [Task_Instructions, Start_Task]
for thisComponent in Task_StartComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Task_Start"-------
while continueRoutine:
    # get current time
    t = Task_StartClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *Task_Instructions* updates
    if t >= 0.0 and Task_Instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        Task_Instructions.tStart = t
        Task_Instructions.frameNStart = frameN  # exact frame index
        Task_Instructions.setAutoDraw(True)
    
    # *Start_Task* updates
    if t >= 0.0 and Start_Task.status == NOT_STARTED:
        # keep track of start time/frame for later
        Start_Task.tStart = t
        Start_Task.frameNStart = frameN  # exact frame index
        Start_Task.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if Start_Task.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
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
    for thisComponent in Task_StartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Task_Start"-------
for thisComponent in Task_StartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Task_Start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Examples.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Examples"-------
    t = 0
    ExamplesClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    ExampleImage1.setImage(Image_1)
    ExampleImage2.setImage(Image_2)
    visibility = 0
    extratime = 999
    key_resp_2 = event.BuilderKeyResponse()
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    ExamplesComponents = [ExampleImage1, ExampleImage2, key_resp_2, mouse, text_4, text_5]
    for thisComponent in ExamplesComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Examples"-------
    while continueRoutine:
        # get current time
        t = ExamplesClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ExampleImage1* updates
        if t >= 0.0 and ExampleImage1.status == NOT_STARTED:
            # keep track of start time/frame for later
            ExampleImage1.tStart = t
            ExampleImage1.frameNStart = frameN  # exact frame index
            ExampleImage1.setAutoDraw(True)
        
        # *ExampleImage2* updates
        if t >= 0.0 and ExampleImage2.status == NOT_STARTED:
            # keep track of start time/frame for later
            ExampleImage2.tStart = t
            ExampleImage2.frameNStart = frameN  # exact frame index
            ExampleImage2.setAutoDraw(True)
        if ExampleImage2.status == STARTED:  # only update if drawing
            ExampleImage2.setOpacity(visibility, log=False)
        if t < 3: 
             visibility = 0 
        if t > 3: 
             sinraw = sin(t*1.5)
             visibility = (sinraw+1)/2
        
        
        if visibility < 0:
            visibility = 0
        
        # *key_resp_2* updates
        if t >= 0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_2.keys == []:  # then this was the first keypress
                    key_resp_2.keys = theseKeys[0]  # just the first key pressed
                    key_resp_2.rt = key_resp_2.clock.getTime()
        # *mouse* updates
        if (text_4.status == STARTED) and mouse.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse.tStart = t
            mouse.frameNStart = frameN  # exact frame index
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not stopped!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(ExamplesClock.getTime())
                    # abort routine on response
                    continueRoutine = False
        
        # *text_4* updates
        if (key_resp_2.keys == 'space') and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        
        # *text_5* updates
        if t >= 5 and text_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_5.tStart = t
            text_5.frameNStart = frameN  # exact frame index
            text_5.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ExamplesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Examples"-------
    for thisComponent in ExamplesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
    trials_2.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials_2.addData('key_resp_2.rt', key_resp_2.rt)
    # store data for trials_2 (TrialHandler)
    if len(mouse.x): trials_2.addData('mouse.x', mouse.x[0])
    if len(mouse.y): trials_2.addData('mouse.y', mouse.y[0])
    if len(mouse.leftButton): trials_2.addData('mouse.leftButton', mouse.leftButton[0])
    if len(mouse.midButton): trials_2.addData('mouse.midButton', mouse.midButton[0])
    if len(mouse.rightButton): trials_2.addData('mouse.rightButton', mouse.rightButton[0])
    if len(mouse.time): trials_2.addData('mouse.time', mouse.time[0])
    # the Routine "Examples" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "Get_ready"-------
t = 0
Get_readyClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
Get_readyComponents = [text_3]
for thisComponent in Get_readyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Get_ready"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Get_readyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_3.status == STARTED and t >= frameRemains:
        text_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Get_readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Get_ready"-------
for thisComponent in Get_readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=len(imagenumarray), method='sequential', 
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
    
    # ------Prepare to start Routine "trial_initalizer"-------
    t = 0
    trial_initalizerClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if random() <= 0.5:
        change_side = 'L'
    else :
        change_side = 'R'
    
    trialcode = randint(1,4)
    
    if trialcode == 1:
        firstimage = 'p'
        secondimage = 'a'
        trialtype = 'disappear'
    if trialcode == 2:
        firstimage = 'a'
        secondimage = 'p'
        trialtype = 'appear'
    if trialcode == 3:
        firstimage = 'p'
        secondimage = 'p'
        trialtype = 'a_nochange'
    
    
    
    image1_name = 'Images\\' +imagenumarray[trials.thisN]+change_side+firstimage+'.jpg'
    image2_name ='Images\\'  +imagenumarray[trials.thisN]+change_side+secondimage+'.jpg'
    
    
    trials.addData('trialtype', trialtype)
    trials.addData('change_side', change_side)
    trials.addData('Imagenumber', imagenumarray[trials.thisN])
    # keep track of which components have finished
    trial_initalizerComponents = []
    for thisComponent in trial_initalizerComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial_initalizer"-------
    while continueRoutine:
        # get current time
        t = trial_initalizerClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_initalizerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_initalizer"-------
    for thisComponent in trial_initalizerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "trial_initalizer" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Trial"-------
    t = 0
    TrialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    Image1.setImage(image1_name)
    Image2.setImage(image2_name)
    visibility = 0 
    extratime = 1
    Trial_type.setText('')
    key_resp_1 = event.BuilderKeyResponse()
    # setup some python lists for storing info about the Mouse_Click_Location
    Mouse_Click_Location.x = []
    Mouse_Click_Location.y = []
    Mouse_Click_Location.leftButton = []
    Mouse_Click_Location.midButton = []
    Mouse_Click_Location.rightButton = []
    Mouse_Click_Location.time = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    TrialComponents = [Image1, Image2, Trial_type, key_resp_1, Changedetected, Mouse_Click_Location]
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Trial"-------
    while continueRoutine:
        # get current time
        t = TrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Image1* updates
        if t >= 0.0 and Image1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Image1.tStart = t
            Image1.frameNStart = frameN  # exact frame index
            Image1.setAutoDraw(True)
        frameRemains = 0.0 + nochangetime + changetime + extratime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Image1.status == STARTED and t >= frameRemains:
            Image1.setAutoDraw(False)
        
        # *Image2* updates
        if t >= 0.0 and Image2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Image2.tStart = t
            Image2.frameNStart = frameN  # exact frame index
            Image2.setAutoDraw(True)
        frameRemains = 0.0 + nochangetime + changetime + extratime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Image2.status == STARTED and t >= frameRemains:
            Image2.setAutoDraw(False)
        if Image2.status == STARTED:  # only update if drawing
            Image2.setOpacity(visibility, log=False)
        if t < nochangetime: 
             visibility = 0 
        if t > nochangetime: 
            sinraw = sin(t*1.5)
            visibility = (sinraw+1)/2
        
        if t > nochangetime + changetime:
            visibility = 0
        
        if visibility < 0:
            visibility = 0
        
        
        if Image2.status == FINISHED:
            continueRoutine = False 
        
        if key_resp_1.keys == 'space':
            extratime = 999
        
        # *Trial_type* updates
        if t >= 0.0 and Trial_type.status == NOT_STARTED:
            # keep track of start time/frame for later
            Trial_type.tStart = t
            Trial_type.frameNStart = frameN  # exact frame index
            Trial_type.setAutoDraw(True)
        frameRemains = 0.0 + nochangetime + changetime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Trial_type.status == STARTED and t >= frameRemains:
            Trial_type.setAutoDraw(False)
        
        # *key_resp_1* updates
        if t >= 0.0 and key_resp_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_1.tStart = t
            key_resp_1.frameNStart = frameN  # exact frame index
            key_resp_1.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_1.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + nochangetime + changetime + extratime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_1.status == STARTED and t >= frameRemains:
            key_resp_1.status = STOPPED
        if key_resp_1.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_1.keys == []:  # then this was the first keypress
                    key_resp_1.keys = theseKeys[0]  # just the first key pressed
                    key_resp_1.rt = key_resp_1.clock.getTime()
        
        # *Changedetected* updates
        if (key_resp_1.keys == 'space') and Changedetected.status == NOT_STARTED:
            # keep track of start time/frame for later
            Changedetected.tStart = t
            Changedetected.frameNStart = frameN  # exact frame index
            Changedetected.setAutoDraw(True)
        if Changedetected.status == STARTED:  # only update if drawing
            Changedetected.setOpacity(1, log=False)
        # *Mouse_Click_Location* updates
        if (Changedetected.status == STARTED) and Mouse_Click_Location.status == NOT_STARTED:
            # keep track of start time/frame for later
            Mouse_Click_Location.tStart = t
            Mouse_Click_Location.frameNStart = frameN  # exact frame index
            Mouse_Click_Location.status = STARTED
            prevButtonState = Mouse_Click_Location.getPressed()  # if button is down already this ISN'T a new click
        if Mouse_Click_Location.status == STARTED:  # only update if started and not stopped!
            buttons = Mouse_Click_Location.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = Mouse_Click_Location.getPos()
                    Mouse_Click_Location.x.append(x)
                    Mouse_Click_Location.y.append(y)
                    Mouse_Click_Location.leftButton.append(buttons[0])
                    Mouse_Click_Location.midButton.append(buttons[1])
                    Mouse_Click_Location.rightButton.append(buttons[2])
                    Mouse_Click_Location.time.append(TrialClock.getTime())
                    # abort routine on response
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
    if key_resp_1.keys in ['', [], None]:  # No response was made
        key_resp_1.keys=None
    trials.addData('key_resp_1.keys',key_resp_1.keys)
    if key_resp_1.keys != None:  # we had a response
        trials.addData('key_resp_1.rt', key_resp_1.rt)
    # store data for trials (TrialHandler)
    if len(Mouse_Click_Location.x): trials.addData('Mouse_Click_Location.x', Mouse_Click_Location.x[0])
    if len(Mouse_Click_Location.y): trials.addData('Mouse_Click_Location.y', Mouse_Click_Location.y[0])
    if len(Mouse_Click_Location.leftButton): trials.addData('Mouse_Click_Location.leftButton', Mouse_Click_Location.leftButton[0])
    if len(Mouse_Click_Location.midButton): trials.addData('Mouse_Click_Location.midButton', Mouse_Click_Location.midButton[0])
    if len(Mouse_Click_Location.rightButton): trials.addData('Mouse_Click_Location.rightButton', Mouse_Click_Location.rightButton[0])
    if len(Mouse_Click_Location.time): trials.addData('Mouse_Click_Location.time', Mouse_Click_Location.time[0])
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    ISI_Dur = 1 + random()*1
    
    trials.addData('ISI_Dur', ISI_Dur)
    # keep track of which components have finished
    ISIComponents = [text, text_2]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 1 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 1 + ISI_Dur- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_2.status == STARTED and t >= frameRemains:
            text_2.setAutoDraw(False)
        
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
    thisExp.nextEntry()
    
# completed len(imagenumarray) repeats of 'trials'


# ------Prepare to start Routine "Task_End"-------
t = 0
Task_EndClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Task_Ender = event.BuilderKeyResponse()
# keep track of which components have finished
Task_EndComponents = [End_task_instructions, Task_Ender]
for thisComponent in Task_EndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Task_End"-------
while continueRoutine:
    # get current time
    t = Task_EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *End_task_instructions* updates
    if t >= 0.0 and End_task_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        End_task_instructions.tStart = t
        End_task_instructions.frameNStart = frameN  # exact frame index
        End_task_instructions.setAutoDraw(True)
    
    # *Task_Ender* updates
    if t >= 0.0 and Task_Ender.status == NOT_STARTED:
        # keep track of start time/frame for later
        Task_Ender.tStart = t
        Task_Ender.frameNStart = frameN  # exact frame index
        Task_Ender.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if Task_Ender.status == STARTED:
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
    for thisComponent in Task_EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Task_End"-------
for thisComponent in Task_EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Task_End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()





# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
