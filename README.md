# FCC-filings

A project to look at [public comments to the FCC on net neutrality](https://www.fcc.gov/ecfs/search/filings?proceedings_name=17-108&sort=date_disseminated,DESC).

The FCC takes public comment through its Electronic Comment Filing Systems and also makes available a nice [API for the ECFS](https://www.fcc.gov/ecfs/public-api-docs.html), at least for now. To use it, you'll need to [sign up for an API key](https://api.data.gov/).

## Getting the filings

You know you want them. Here's how to get them as a series of `.json` files with 1000 filings each.

```bash
python3 python/get_filings.py --limit 1000 --max 10000 --start 500000 -o my_directory
```

## Read in the filings

OK, now fire up ipython and read them and concatenate them into an array.

```python
import glob
import json
import os

def read_filings(output_dir):
    filings = []
    path = os.path.join(output_dir, '*.json')
    for filename in glob.iglob(path):
        print(filename)
        with open(filename, encoding='utf-8') as f:
            filings += json.load(f)['filings']
    return filings
```

...profit! No, wait. I don't actually know what to do with them at this point...

