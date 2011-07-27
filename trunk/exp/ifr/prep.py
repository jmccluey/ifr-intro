# Immediate Free Recall: prep.py

"""
This module prepares stimuli to be used by ifr.py.
"""

import random
import os
import sys

def listWAScheck(wordInds, WASthresh):
    """
    Check if similarity between any two words in a list exceeds some
    threshold.
    """
    # check to make sure no two words in the list are too similar
    listGood = True
    for word1 in wordInds:
        for word2 in wordInds:
            val = semMat[word1][word2]
            if val >= WASthresh and val < 1:
                listGood = False
                return listGood
    return listGood

def listWordOrder(listLength, WASthresh, maxTries):
    """
    Create one list of words according to certain criteria.  Lists are
    randomly created from available words listed in wp_allowed, and
    rejected if they fail the following test:

    Using WAS values, make sure no two words have higher semantic
    similarity than WASthresh.
    """
    global wp_allowed

    # create a list with random words;  if it fails, try again
    listPass = False
    nTries = 0
    while not listPass:
        nTries += 1
        if nTries == maxTries:
            print 'Warning: maximum tries to create list reached.'
            break

        # make a copy of allowed words so we can pop them
        wp_temp = wp_allowed[:]

        # make a list from allowed words
        listPass = True
        list_wo = []
        list_inds = []

        for n in xrange(listLength):
            # take a random item from allowed words
            item = wp_temp.pop(random.choice(range(len(wp_temp))))

            # get the absolute index in the complete wordpool
            ind = wp_tot.index(item)

            # store the item and itemno
            list_wo.append(item)
            list_inds.append(ind)

        # test: no two words on list too similar
        if not listWAScheck(list_inds, WASthresh):
            listPass = False
            continue

    # if list passes, list words are now unavailable
    wp_allowed = wp_temp[:]
    return list_wo

def sessWordOrder(prev_sess_words, config):
    """
    Create word lists to be presented in one session.
    """
    global wp_allowed

    # create lists and add words to session
    sess_wo = []
    sess_words = []
    for n in xrange(config.nLists):
        list_wo = listWordOrder(config.listLength, config.WASthresh,
                                config.maxTries)
        sess_wo.append(list_wo)
        
        # repeat shuffled lists
        for m in xrange(config.nReps-1):
            # dereference list, or else prior lists of these words
            # will get shuffled too
            list_wo = list_wo[:]

            # shuffle and add
            random.shuffle(list_wo)
            # repeated list criteria?
            sess_wo.append(list_wo)

        sess_words.extend(list_wo)

    if config.allowPrevSessWords:
        # current session's words are now free to be used again
        wp_allowed.extend(sess_words)
    else:
        # only previous session's words are free to be used again
        wp_allowed.extend(prev_sess_words)

    return sess_wo, sess_words

def subjWordOrder(config):
    """
    Create the order of presentation of stimuli for one subject.
    Words can be repeated, but not within a session, and only in
    adjacent sessions if specified in the config (see
    allowPrevSessWords).

    Inputs
    ______
    config : config
        Configuration object for a subject.

    Outputs
    _______
    wordpool_total : A complete list of the words that stimuli were
                     drawn from

    subj_word_order : A list of lists of lists giving a string of each
                      word to be presented in the experiment.  To
                      access the word to be presented at session i,
                      list j, item k:
                      subj_word_order[i][j][k]
    """
    global wp_tot, wp_allowed, semMat

    # read in the wordpool
    wp_tot = []
    wpfile = open(config.wpfile, 'r')
    wpLines = wpfile.readlines()
    for wpLine in wpLines:
        wp_tot.append(wpLine.strip())
    wp_allowed = wp_tot[:]

    # read in WAS values for each possible pair of words
    semMat = []
    wasfile = open(config.wasfile, 'r')
    for word in wasfile:
        wordVals = []
        wordValsString = word.split()
        for val in wordValsString:
            thisVal = float(val)
            wordVals.append(thisVal)
        semMat.append(wordVals)

    subj_wo = []
    prev_sess_words = []
    for n in xrange(config.nSessions):
        # generate lists for this session
        (sess_wo, prev_sess_words) = sessWordOrder(prev_sess_words,
                                                   config)
        subj_wo.append(sess_wo)

    return wp_tot, subj_wo

def verifyFiles(files):
    """
    Verify that all the files specified in the config are there so
    that there is no random failure in the middle of the experiment.
    This will call sys.exit(1) if any of the files are missing.
    """

    for f in files:
        if not os.path.exists(f):
            print "\nERROR:\nPath/File does not exist: %s\n\nPlease verify the config.\n" % f
            sys.exit(1)

def estimateTotalTime(config):
    """
    Calculates time (in minutes) from the start of the experiment to
    the end of the experiment, including rewetting time.

    Timing of one list:

    Code  Name                     Config Variable
    ______________________________________________
    PLD   pre-list delay           preListDelay
    W     word presentation        wordDuration
    ISI   inter-stimulus interval  wordISI + jitter/2
    PRD   pre-recall delay         preRecallDelay + jitterBeforeRecall/2
    R     recall period            recallDuration

    IFR:
    PLD W ISI W ISI ... W ISI PRD R
    """
    
    # mean time for list items
    itemTime = config.wordDuration + config.wordISI + config.jitter/2
    print 'Item: ' + str(itemTime)

    # mean list time
    listTime = config.preListDelay + itemTime*config.listLength + \
               (config.preRecallDelay + config.jitterBeforeRecall/2) + \
               config.recallDuration
    print 'List: ' + str(listTime)

    instruct = 300000 # getting through instructions
    listBreak = config.breakDuration # break after each list

    # total session time
    sessionTime = instruct + (listTime + listBreak)*config.nTotalLists

    # convert to minutes
    sessionTime = sessionTime*(1./1000)*(1./60)

    return sessionTime
