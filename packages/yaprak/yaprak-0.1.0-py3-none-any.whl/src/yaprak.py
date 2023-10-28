#!/usr/bin/env python
# SPDX-FileCopyrightText: © 2023 N. Sertac Artan <artans.github@gmail.com>
# SPDX-License-Identifier: MIT

import json        
import os
from abc import ABC, abstractmethod

class Yaprak(ABC):
    """Base class for yaprak"""
    def __init__(self, config = None):
        self.config = {}
        self.current_iteration = {}
        self.globals = {}
        self.__IDs = []
        self.__processes = []
        self.__inFileList = []
        self.__outFileList = []
        self.__outPath = None
        if config:
            self.readConfig(config)
            self.globals = {'outPath': self.__outPath}

    def run(self):
        for instances in zip(self.__IDs, self.__inFileList, self.__outFileList):
            self.current_iteration = {'ID': instances[0], 'inFile': instances[1],
                                      'outFile': instances[2]}
            self.load(instances[1])
            for process_spec in self.__processes:
                if process_spec['apply']:
                    function = getattr(self, process_spec['process'])
                    function(process_spec)
            self.save(instances[2])
            self.report()

    @abstractmethod
    def load(self, file):
        raise NotImplementedError("The load method in Yaprak is abstract\
        and should be implemented in the child class")

    @abstractmethod
    def save(self, file):
        raise NotImplementedError("The save method in Yaprak is abstract\
        and should be implemented in the child class")

    @abstractmethod
    def report(self):
        raise NotImplementedError("The report method in Yaprak is abstract\
        and should be implemented in the child class")

    # Config
    def readConfig(self, fileName): 
        self.config = load_json_file(fileName)
        if "IDs" in self.config:
            self.__IDs = self.config['IDs'] 
        if "inFileList" in self.config:
            self.__inFileList = fullPathFileList(self.config, 'in')
        if "outFileList" in self.config:
            self.__outFileList = fullPathFileList(self.config, 'out')
        if "outPath" in self.config:
            self.__outPath = self.config['outPath'] 
            mkdir_p(self.__outPath)
        if "processes" in self.config:
            self.__processes = [x for x in self.config['processes']]

    def setConfig(self, config):
        self.config = config

    def getConfig(self):
        return self.config

    def generateConfig(self):
        pass 

    # IDs
    def setIDs(self, IDs):
        self.__IDs = IDs

    def getIDs(self):
        return self.__IDs 

    def generateIDs(self):
        pass 

    # File Lists
    def setInFileList(self, fileList):
        self.__inFileList = fileList

    def getInFileList(self):
        return self.__inFileList 

    def setOutFileList(self, fileList):
        self.__outFileList = fileList

    def getOutFileList(self):
        return self.__outFileList 

    # Processes
    def setProcesses(self, processes):
        self.__processes = processes

    def getProcesses(self):
        return self.__processes 

    def generateProcesses(self):
        pass 

    # Example processes

class Summary(Yaprak):
    def __init__(self, config = None):
        Yaprak.__init__(self, config)
        self.outSummaryFile = None
        self.readAdditionalConfig(config)

    # Config
    def readAdditionalConfig(self, config): 
        if "outSummaryFile" in self.config:
            self.outSummaryFile = fullPathFile(self.config, 'outSummary')

    def run(self):
        IDs = self.getIDs()
        inFileList = self.getInFileList()
        processes = self.getProcesses()
        for instances in zip(IDs, inFileList):
            self.current_iteration = {'ID': instances[0], 
                                      'inFile': instances[1]}
            self.load(instances[1])
            for process_spec in processes:
                if process_spec['apply']:
                    function = getattr(self, process_spec['process'])
                    function(process_spec)
        self.summarize()
        self.report()

    @abstractmethod
    def summarize(self):
        raise NotImplementedError("The summarize method in Yaprak is abstract\
        and should be implemented in the child class")

def fullPathFile(config, type):
        pathName = type + "Path"
        fileName = type + "File"
        fullPathFileOutput = None 
        # Path and filename separate
        if pathName in config and fileName in config:
            path = config[pathName] 
            fileName = config[fileName]
            fullPathFileOutput = path + fileName
        # Full path
        elif fileName in config: 
            fullPathFileOutput = config[fileName] 
        return fullPathFileOutput 

def fullPathFileList(config, type):
        pathName = type + "Path"
        fileListName = type + "FileList"
            
        # Grab file info from config.
        fullPathFileListOutput = []
        # Path and filename separate
        if pathName in config and fileListName in config:
            path = config[pathName] 
            fileList = config[fileListName]
            fullPathFileListOutput = [path + file for file in fileList]
        # Full path
        elif fileListName in config: 
            fullPathFileListOutput = config[fileListName] 
        return fullPathFileListOutput 

def load_json_file(fileName):
    """
        Loads a json file as config 
        
        Args:
            fileName (str): Name of input json file.

        Returns:
            config: Json data as key-value pairs dictionary
    """
    with open(fileName) as json_file:
        json_data = json.load(json_file)
    return json_data

def mkdir_p(path):
    """
        Creates the directory path if it doesn't exist
        
        Args:
            path (str): Full path of the directory to be created 

        Returns:
            (int): 0 If directory exists 
                   1 If directory does not exist and created by this function.
            None
    """
    if os.path.exists(path):
        print("Output directory exists, overwrites are possible.")
        return 0
    print("Creating new directory " + path + ".")
    os.makedirs(path)
    return 1


