#-------------------------------------------------------------------------------
# Name:        Add_listed_datasets_to_display
# Author:      Flo
# Created:     15.11.2017
# Copyright:   (c) Flo 2017
#-------------------------------------------------------------------------------

import arcpy
from arcpy import env
shapefiles = []                                                 #<-- Specify list before running!

# specify map document
mxd = arcpy.mapping.MapDocument("CURRENT")

# get the data frame
dataframe = arcpy.mapping.ListDataFrames(mxd,"*")[0]

# create a new layer for each item in the list.
for i in shapefiles:
    newlayer = arcpy.mapping.Layer(i)
    arcpy.mapping.AddLayer(dataframe, newlayer,"BOTTOM")