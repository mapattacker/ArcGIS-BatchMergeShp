## Batch merge shapefiles of same name

### Description
I often receive shapefiles that have a standard naming convention, and I used to drop them one by one into the ArcGIS Merge tool, so that I can verify the contents at one go, before uploading to the geodatabase. That absolutely drove me crazy, given that there are lots of files to deal with. Imagine searching in ArcCatalog, 10 different folders for shapeflies with a specific name, and repeat that 30 times for other names.

This script (BatchMergeShp.py) does everything automatically. Just drop all the folders containing the shapefiles into a main folder, define that main folder path, as well as the output folder path into the script. A single shapefile will be created for each unique name.

##### In summary:

1) You have many shapefiles in different folders that have the same name. e.g., 30 sets of files of one name x 10 times

2) You want to merge all files of the same name together so that you can upload them at one go to a central geodatabase

3) Use the script / tool to excecute. A single shapefile with suffix "_merge" will be created in a defined folder.

### Requirements
It uses some Arcpy functions, so requires ArcGIS to be already installed.

### ArcGIS Tool
I have also created an ArcGIS tool to perform the same function. Place the script and toolbox inside the Toolbox folder somewhere together and add the latter into ArcMap/Catalog ArcToolbox window.

### Credits
Have to thank the good folks in geonet.esri.com forum for debugging the script. This script was also a modification of a previous script, of which I can't remember the source. However that is limited to just combing through just at subdirectory level, not all contents of a directory. Also, it took terribly long to execute the script to completion.
