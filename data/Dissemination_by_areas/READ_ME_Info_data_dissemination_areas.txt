Dissemination areas of Montreal:

shapefile and its accessories: .cpg, .dbf, .qpj, .shp, .shx

Open the .shp file in Tableau and keep the others in the same folder.

Xcel file: 

"MTL_Districts_blocks" the same data in an excel table for reference; geographical info in the POLYGON column;


Tableau file for reference contains "MOntreal" file filtered per areas for reference;

Dissemination Areas With Pop:

Inside the folder there is the shapefile I created with alteryx after changing the data to left join
the shapefile "MOntreal.shp" file column "DUID", with "Population_dissemination_areas_Canada" column Geografic code.

In Alteryx,
I changed the column names as the shp file truncates them, and changed some of the data types.

Total private dwellings, 2016 = PRIV_DW
Province / teritory, french = PR_FR
Province / teritory, english = PR_EN
Private dwellings occupied by usual residents, 2016 = PRIV_U
Population, 2016 = POPULATION
Population density per square kilometre, 2016 = POP_DN_KM2
Land area in square kilometres, 2016 = AREA_KM2
Incompletely enumerated Indian reserves and Indian settlements, 2016 = I removed this column
Geographic code, Province / territory = PR_GEO_CODE
Geographic code, Census subdivision = Census_subdiv
Geographic code, Census division = Census_div
Geographic code = GEO_CODE


In Tableau,
I added the surface of each dissemination area in km2, and population as dimensions on the map, for reference.


