# MontrealFireSafetyProject
 Tracking progress of our study to determine potential fire safety issues in the city of Montreal

### Strategy
	Evaluate the risk and preparedness of fire incidents for all areas in Montreal

### Methodology
	1) Make the geo index
		Snap all incidents & buildings to one coordinate system
		Flatten the dataset to be fed to a classifier later
	2) Create the dataset w features
		Snap the researched features to our created coordinate system
	3) Classification with a window
		Predict next-year incidents
	4) Predict for next year
	5) Create heat map for "at-risk" areas
	6) Compare with heat map for "preparedness" areas

### Data Catalogue
	- 2006-2016 total population & dwellings & census by postal code (FSA)
		- Some of that data was extrapolated (census)
		- Linear interpolation for missing years
		- Everything was extrapolated to a one-year basis
	- 2015-2019 crime data
	- 2005-2019 Fire incidents data
	- (constant) Building data
	- Casernes data

### Data Methodology
	- Baseline:
		- Use population, dwellings, census, building data to predict all fire department respondant incidents ranging from 2005-2019
	
