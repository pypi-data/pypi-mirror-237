# My Favorite Things
 Convenient functions and classes I use too often. If Coltrane was a programmer (_shudder_) and much worse.

## Installation
Install with
```
pip install my-favorite-things
```

## Current Methods (by file)
### save
#### `save(name, savedir="", savepath="", stype="npz", absolute=False, parents=0, overwrite=False, append=False, dryrun=False, save_kwargs={}, **kwargs)`
**Import by**
```python
from my_favorite_things import save
```
This method is used for saving data to a file. You can save as an `.npz`/`.npy` file for numpy array(s) or as a `.pkl` file for dictionaries and other odd python objects. By default, it will not overwrite existing files but instead append a number onto the end of file name (the keywords being, by default, `overwite=False` and `append=True`). You can save relative to your current directory (`absolute=False`) or as an absolute path (`absolute=True`). Addtionally, double check that you're saving to the correct directory with `dryrun=True`. Check the doc string for more info.

---

### ddicts
#### `nested_ddict(depth, endtype)`
**Import by**
```python
from my_favorite_things import nested_ddict
```
This method allows for creating a nested defaultdictionary. This is useful if you have data that is dependent on multiple parameters that are heirarchical. For example, if we do
```python
d = nested_ddict(3, list)
```
then we can use it as
```python
d['zero']['one']['two']['three'].append(datum)
```

#### `format_ddict(ddict, make_nparr=True, sort_lists=False)`
**Import by**
```python
from my_favorite_things import format_ddict
```
This method will format your (nested) defaultdictionary into dictionaries. Additionally, it can turns lists in numpy arrays and/or sort the lists too.

---

### plots
#### `log_bins(*arrs, num_bins)`
**Import by**
```python
from my_favorite_things import log_bins
```
This method is used for binning for histograms logarithmically. In `plt.hist`, setting the keyword `bins` to the output of this function (where `arrs` are the arrays being plotted) and `ax.set_xscale("log")` will give equally spaced bins (for multiple data sets over the logarithmic x-axis).

#### `cumulative_bins(*arrs, num_bins)`
**Import by**
```python
from my_favorite_things import cumulative_bins
```
This is similar to the previous method but for a linear scale. When plotting multiple data sets on the same plot, they may have different ranges and, thus, bin sizes. So this method will create the bin values so that the bars of the histogram will all have the same width.

#### `bar_count(ax, counts, labels, label_bars, sort_type, *, bar_params, **kwargs)`
**Import by**
```python
from my_favorite_things import bar_count
```
This method will create a bar plot for the data passed using strings as labels (either as the keys of a dictionary passed for `counts` or as a list passed from `labels`) with various conveniences like specifying the format of the label strings or the order of the plotted data.

---

### colors
#### `fader(color1, color2, fraction)`
**Import by**
```python
from my_favorite_things import fader
```
This method will return a color in hex code as a `fraction` between the two given colors `color1` and `color2`.

#### `multifader(colors, fractions)`
```python
from my_favorite_things import multifader
```
Like above, but intermediate colors can also be defined in the `colors` list. These colors are equally spaced.
