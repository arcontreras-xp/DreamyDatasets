# DreamyDatasets
Datasets that I use for testing, approximately 10000 rows each.

## Cloud_Data_Generator()

### Parameters

**cloud_no** - number of clouds to generate

**n** - total number of data points

**naxs** - number of axes to generate in (equiv. dimension)

**stretch_par** - list of *stretch* parameters, essentially a scalar multiplier on each *axis*

**dist_par** - list of *split_dist* parameters, essentially a scalar multiplier on the distance that splits each cloud

## To Do

**[DONE]** upload python code that generates the datasets

**[ ]** adjust code so that *stretch* and *split_dist* parameters are applied to each *cloud* instead of each axis

**[ ]** create sine wave generator with parameters: magnitude, wavelength, y-range, x-range, 90-deg-rotation, variance/noise

**[ ]** add feature to sine wave generator that introduces linear increase

**[ ]** add feature to sine wave generator that introduces multiple sine waves with parameters: phase-shift, y-shift
