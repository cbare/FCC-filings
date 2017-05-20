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

filings = read_filings('data/may_15')
```

### There are some nice analyses of this data set by these folks:

 * [Jeffrey Fossett](http://jeffreyfossett.com/2017/05/13/fcc-filings.html)
 * [Nathaniel Fruchter](https://medium.com/@nhf/whats-up-with-all-of-those-identical-comments-on-the-fcc-net-neutrality-docket-105835f59c3e)
 * [Chris Sinchok](https://medium.com/@csinchok/an-analysis-of-the-anti-title-ii-bots-463f184829bc)

### The issue of spam-bots in the comment filings got some press coverage:

 * [Anti-net neutrality spammers are flooding FCC's pages with fake comments](http://www.zdnet.com/article/a-bot-is-flooding-the-fccs-website-with-fake-anti-net-neutrality-comments/)
 * [FCC Buried By Fake and Hate-Filled Comments on Net Neutrality](http://fortune.com/2017/05/10/fcc-net-neutrality-spammers/)
 * [FCC Is Honoring Fake Anti-Net Neutrality Rants Left By Bots](http://www.vocativ.com/431065/fcc-ajit-pai-net-neutrality-bots/)

### More general information on net neutrality:

 * [EFF on Net Neutrality](https://www.eff.org/issues/net-neutrality)
 * [Don't Get Fooled: The Plan Is To Kill Net Neutrality While Pretending It's Being Protected](https://www.techdirt.com/blog/netneutrality/articles/20170502/17212137292/dont-get-fooled-plan-is-to-kill-net-neutrality-while-pretending-being-protected.shtml)
 * [FCC votes to begin overturning net neutrality](https://www.theverge.com/2017/5/18/15657916/fcc-kill-net-neutrality-proposal-vote-passes)
