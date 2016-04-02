# Batch merge shapefiles of same name

### Description
I often receive shapefiles that have a standard naming convention, and I used to drop them one by one into the ArcGIS Merge tool, so that I can verify the contents at one go, before uploading to the geodatabase. That absolutely drove me crazy, given that there are lots of files to deal with. Imagine searching in ArcCatalog, 10 different folders for shapeflies with a specific name, and repeat that 30 times for other names.

This script (BatchMergeShp.py) does everything automatically. Just drop all the folders containing the shapefiles into a main folder, define that main folder path, as well as the output folder path into the script. A single shapefile will be created for each unique name.

### Requirements
It uses some Arcpy functions, so requires ArcGIS to be already installed.

### ArcGIS Tool
I have also created an ArcGIS tool to perform the same function. Just place the script and toolbox inside the Toolbox folder and add the latter into ArcMap/Catalog ArcToolbox window.

### Credits
Have to thank the good folks in geonet.esri.com forum for debugging the script.
