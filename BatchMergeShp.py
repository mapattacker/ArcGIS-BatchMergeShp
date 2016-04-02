import time, arcpy, os
start = time.time()

#################### ENTER VARIABLES ##########################
workspace = r'C:\Users\User\Desktop\XX'  #Enter path directory where files are contained
output_folder = r'C:\Users\User\Desktop\XX' #Enter path directory where output should go
###############################################################

Dict = {}

for root, dirs, files in os.walk(workspace):
    for dir in dirs:
        arcpy.env.workspace = os.path.join(root,dir)
        for fc in arcpy.ListFeatureClasses():
            if not fc in Dict: 
                Dict[fc] = []
                Dict[fc].append(os.path.join(root,fc))
            else:
                Dict[fc].append(os.path.join(root,fc))

for key in Dict:
    print key

for key in Dict:
    output = os.path.join(output_folder,key[:-4]) + '_merge'
    arcpy.Merge_management(Dict[key], output)
    print output + " created"

end = time.time()
date = time.strftime('%H:%M:%S')
print '\nscript ends at {} at {}'.format((end-start), date)
