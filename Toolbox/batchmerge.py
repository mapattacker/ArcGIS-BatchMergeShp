import arcpy, os

#input path of folder where all shapefiles reside in
workspace = arcpy.GetParameterAsText(0)
#input output folder of merged shapefiles
output_folder = arcpy.GetParameterAsText(1)

Dict = {}

for root, dirs, files in os.walk(workspace):
    for dir in dirs:
        arcpy.env.workspace = os.path.join(root,dir)
        for fc in arcpy.ListFeatureClasses():
            if not fc in Dict:
                Dict[fc] = []
                Dict[fc].append(os.path.join(root,dir,fc))
            else:
                Dict[fc].append(os.path.join(root,dir,fc))

for key in Dict:
    output = os.path.join(output_folder,key[:-4]) + '_merge'
    arcpy.Merge_management(Dict[key], output)
    print output + " created"
    arcpy.AddMessage('{} created'.format(output))

arcpy.AddMessage('Script completed!')
