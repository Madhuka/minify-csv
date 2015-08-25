#!/usr/bin/python
# -*- coding: utf-8 -*-
import minify


def getRegex(str):
    s_array = minify.spilter(str)
    minify.grouping(s_array, 1)
