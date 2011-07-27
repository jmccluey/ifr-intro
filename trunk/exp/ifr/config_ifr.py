# Configuration for Immediate Free Recall

"""
This module sets options for running Immediate Free Recall.
"""

### experiment structure ###
nSessions = 2

nLists = 16 # number of unique word lists
nReps = 2 # number of time those word lists are repeated
nTotalLists = nLists * nReps
listLength = 24
wpfile = '../pools/ifr_wordpool.txt'

# word order
wasfile = '../pools/ifr_was.txt'
WASthresh = .55 # maximum acceptable WAS similarity between any pair of words
maxTries = 1200 # maximum number of tries to create a list
allowPrevSessWords = True

# version file name
svnVersionFile = 'version.txt'

# break control
breakSubjectControl = True

### stimuli ###

# stimulus display settings
doMicTest = True
sessionEndText = "Thank you!\nYou have completed the session."
recallStartText = '*******'
wordHeight = .08 # Word Font size (percentage of vertical screen)
defaultFont = '../fonts/Verdana.ttf'
fixationHeight = .07

# beep at start and end of recording (freq,dur,rise/fall)
startBeepFreq = 800
startBeepDur = 500
startBeepRiseFall = 100
stopBeepFreq = 400
stopBeepDur = 500
stopBeepRiseFall = 100

# instruction keys
downButton = 'DOWN'
upButton = 'UP'
exitButton = 'RETURN'

# Instructions
textFiles = dict()

textFiles['introSess'] = 'text/introSess.txt'
textFiles['introRecall'] = 'text/introRecall.txt'
textFiles['introQuestions'] = 'text/introQuestions.txt'
textFiles['introGetReady'] = 'text/introGetReady.txt'
textFiles['trialBreak'] = 'text/trialBreak.txt'

files = [wpfile,
         wasfile]
files.extend(textFiles.values())

### timing ###

# breaks
instructISI = 500
preListDelay = 1500
breakDuration = 5000

# study
wordDuration = 300
wordISI = 2000
jitter = 400

# retention
preRecallDelay = 1200
jitterBeforeRecall = 200

# test
recallDuration = 75000


fastConfig = True
if fastConfig:
    listLength = 6
    recallDuration = 10000
