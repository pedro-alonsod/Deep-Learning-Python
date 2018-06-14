#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import numpy
from keras import layers 
from keras import models

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1))) 
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.summary()

print(model)

"""
Created on Wed Jun 13 20:57:33 2018

@author: pedroalonso
"""

