# -------------------------------------------------------------
# Author: Francesco Vitucci
# License: GPL3
# -------------------------------------------------------------


# -------------------------------------------------------------
# Import libraries
# -------------------------------------------------------------

import numpy as np

# -------------------------------------------------------------
# Event class
# -------------------------------------------------------------

class Event:
    def __init__(self, dict: dict):
        self.dict = dict

# -------------------------------------------------------------
# Note class
# -------------------------------------------------------------

class Note(Event):
    def __init__(self, dict: dict):
        super().__init__(dict)
        self.onset = dict['onset']
        self.duration = dict['duration']

    def __str__(self) -> str:
        return f'Note object. Dict: {self.dict}'

# -------------------------------------------------------------
# Figure class
# -------------------------------------------------------------

type noteList = list[Note]

class Figure():
    def __init__(self, noteList: noteList):

        if not isinstance(noteList, list):
            raise TypeError("Expected a list of Notes.")
        if not all(isinstance(obj, Note) for obj in noteList):
            raise TypeError("Expected a list of Notes.")
        
        #self.noteList = noteList

        self.noteList = []
        for note in noteList:
            if "pitch" not in note.dict:
                note.dict["pitch"] = -1
            self.noteList.append(note)

        # vvv questo è sbagliato vvv
        self.figureParams = list(self.noteList[0].dict.keys())

    def getFigureParamsDict(self) -> dict:
        globalRes = []
        for elem in self.noteList:
            localRes = []
            for entry in list(elem.dict.items()):
                localRes.append(entry[1])
            globalRes.append(localRes)
        paramList = list(map(list, zip(*globalRes)))
        # ------
        d = {}
        for paramIndex in  range(len(self.figureParams)):
            d[self.figureParams[paramIndex]] = paramList[paramIndex]

        return d
    
    def getParamFFTAnalysis(self, paramName: str) -> list:
    
        paramFFT = np.fft.fft(self.getFigureParamsDict()[paramName])

        return paramFFT
    
# -------------------------------------------------------------
# Comparator class
# -------------------------------------------------------------

type figureList = list[Figure]

class Comparator:
    def __init__(self, figureList: figureList):

        self.figureList = figureList

    def getMaxLen(self) -> int:
        lengths = []
        for figure in self.figureList:
            lengths.append(len(figure.noteList))
        return max(lengths)
    
    def compareParamFFTAnalysis(self, param: str):
        pass