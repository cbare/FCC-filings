"""
Command-line script to retrieve filings from the FCC's
Electronic Comment Filing System (ECFS).
"""
import click
import json
import os
import requests
import time

endpoint = 'https://publicapi.fcc.gov/ecfs/filings'

## read in API key from separate file
with open('.api_key') as f:
    api_key = f.read().strip()


def get_batch_of_filings(limit=100, offset=0, output_dir='data', retry=3):
    params = {
        'api_key': api_key,
        'sort': 'date_received,ASC',
        'proceedings.name': '17-108',
        'limit': limit,
        'offset': offset}
    url = endpoint + '?' + '&'.join(k+'='+str(v) for k,v in params.items())
    backoff = 1
    while retry > 0:
        response = requests.get(url)
        if response.status_code == 200:
            path = os.path.join(output_dir, 'filings_{offset:07d}.json'.format(**params))
            with open(path, 'wb') as f:
                f.write(response.content)
            return response.json()
        retry -= 1
        time.sleep(backoff)
        backoff *= 2
    else:
        response.raise_for_status()


@click.command()
@click.option('--limit', default=100, help='How many filings to retrieve at once.')
@click.option('--start', default=0, help='Start at an offset into the list of filings ordered by date_received.')
@click.option('--max', '--max_to_retrieve', default=1000, help='How many filings to retrieve in total.')
@click.option('-o', '--output-dir', default='data')
def main(limit=100, start=0, max_to_retrieve=1000, output_dir='data'):
    for offset in range(start, max_to_retrieve,limit):
        data = get_batch_of_filings(limit=limit, offset=offset, output_dir=output_dir)
        print(f'read offset {offset}')
        time.sleep(1)


if __name__ == '__main__':
    main()
