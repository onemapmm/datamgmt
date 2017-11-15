#-------------------------------------------------------------------------------
# Name:        Data_finder_and_field_summarizer_to_txt
# Purpose:     Finds specific datasets such as shapes in folders & subfolders (incluting optional string identifyer) and summarizes attribute fields in a .txt file.
# Author:      Flo
# Created:     15.11.2017
# Copyright:   (c) Flo 2017
#-------------------------------------------------------------------------------

print "A-louq louq-deh."

import arcpy, csv, os
workspace = "D:\OneMap_Myanmar\_DoP\DoP_data\DoP_Update"                                # <-- Select folder to search in.

## search for shapefiles:

shapefiles = []

for dirpath, dirnames, filename in arcpy.da.Walk(workspace,datatype="FeatureClass"):
    for item in filename:
       if item[-10:] == "VT_dop.shp":                                                   # <-- Specify string identifier.
        shapefiles.append(os.path.join(dirpath, item))

## write txt file containing shape name and all fields:

outfile_name = "Attributes_listed.txt"                                                  # <-- Change name of output textfile.
outfile = os.path.join(workspace, outfile_name)

# assess maximum number of fields found in all shp attribute tables:

number_of_fields = 0
for i in shapefiles:
    fields = arcpy.ListFields(i)
    print """{0} : {1} fields""".format(os.path.basename(i), len(fields))             # <-- Optionally print the number of fields per shape for double checking the result.
    if len(fields) > number_of_fields:
        number_of_fields = len(fields)

# write txt file:

with open(outfile,"w+") as f:
    w = csv.writer(f)

    # Add header cloumn to txt containing Name, attribute 1...n:
    header_row = ["name"]
    for n in range(1, number_of_fields + 1):
        header_row.append("field_"+str(n))
    w.writerow(header_row)

    # Populate table with name and fields from shapes:
    for i in shapefiles:
        fields = arcpy.ListFields(i)
        field_names = [field.name for field in fields]
        filename = ([str(os.path.basename(i))])

        # add n.s. for fields that are not populated:
        if len(fields) < number_of_fields:
            fill_positions = number_of_fields-len(fields)
            fill_list=[]
            for x in range (0, fill_positions):
                fill_list.append("n.s.")                                                # <-- Optionally change the value for non-existing fields.
            filename_and_fields = filename + field_names + fill_list
            w.writerow(filename_and_fields)

        else:
            filename_and_fields = filename + field_names
            w.writerow(filename_and_fields)
f.close

print "Pi bi."