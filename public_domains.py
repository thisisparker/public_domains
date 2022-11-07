import os
import re
import nltk
import time
import tqdm
import whois
import string
import logging
import argparse
import requests

# this should be a no-op if it has already been run
nltk.download('punkt', quiet=True)

known_unavailable = [

    # these are known to not openly accept registrations
    'active',
    'amazon',
    'apple',
    'arte',
    'audi',
    'audible',
    'bank',
    'baseball',
    'basketball',
    'boots',
    'case',
    'dell',
    'drive',
    'fast',
    'fire',
    'fly',
    'gallo',
    'globo',
    'infiniti',
    'museum',
    'natura',
    'origins',
    'post',
    'prime',
    'silk',
    'smile',
    'star',
    'va',
    'vana',
    'visa',
    'viva',
    'vivo',
    'weather',
    'windows',

    # these appear to be proposed but are not available yet
    'data',
    'latino',
    'mobile'
]

nic = whois.NICClient()

def main():
    args = get_args()
    logging.basicConfig(filename=args.log, level=logging.INFO)
    hosts = get_hosts(args.text_file, args.quiet)
    if args.check:
        hosts = available_hosts(hosts, args.quiet, args.sleep)
    for host in hosts:
        print(host)

def get_args():
    parser = argparse.ArgumentParser(
        prog="public_domains", 
        description="Get possible hostnames from a text"
    )
    parser.add_argument("text_file", help="A text file to look for hostnames in or a title to look up in gutenberg.org")
    parser.add_argument("--check", action="store_true", help="Check if the domain is actually available")
    parser.add_argument("--quiet", action="store_true", help="Silence diagnostic messages on the console.")
    parser.add_argument("--sleep", type=float, default=0.5, help="Time to sleep between whois requests")
    parser.add_argument("--log", default="public_domains.log", help="Log file to write to.")
    return parser.parse_args()

def get_hosts(input_text, quiet=False):
    tlds = get_tlds()

    # if it's a file use it as input or look up the text in gutenberg
    if os.path.isfile(input_text):
        with open(input_text, 'r') as f:
            md = ' '.join([l.strip() for l in f.readlines()])
    else:
        md = gutenberg(input_text)

    md_sents = nltk.tokenize.sent_tokenize(md)

    possible_domains = set()

    for s in md_sents:
         wl = nltk.tokenize.word_tokenize(s)
         wl = [w.lower() for w in wl]
         wl = [''.join([c for c in w if c in string.ascii_lowercase]) for w in wl]
         wl = [w for w in wl if w]
         for i, w in enumerate(wl):
             if (i > 1 and w in tlds and len(w) > 3 
                     and len(wl[i-1]) > 5 and len(wl[i-2]) > 5):
                 full_domain = '.'.join([wl[i-2], wl[i-1], w])
                 possible_domains.add(full_domain)

    return possible_domains

def get_tlds():
    tlds = []
    r = requests.get("https://data.iana.org/TLD/tlds-alpha-by-domain.txt")

    for d in r.text.splitlines():
        if d.startswith("#") or d.startswith('XN--'):
            continue
        d = d.lower()
        if d not in known_unavailable:
            tlds.append(d)
    return tlds

def available_hosts(hosts, quiet, sleep):
    av = []
    with tqdm.tqdm(disable=quiet, total=len(hosts)) as progress:
        for host in hosts:
            progress.update()
            progress.set_postfix_str("found %s" % len(av))
            if available(host) in [None, True]:
                av.append(host)
            time.sleep(sleep)
    return av

def available(hostname): 
    domain = hostname.split('.', 1)[1]
    logging.info("whois look up for %s" % domain)
    try:
        response = nic.whois_lookup(None, domain, flags=0, quiet=True)
        entry = whois.WhoisEntry.load(domain, response)
        logging.info("got: %s" % entry)
        return entry['domain_name'] is None
    except whois.parser.PywhoisError as e:
        logging.warn("whois parse error: %s", e)
        return None

def gutenberg(title):
    params = {"query": title, "format": "json"}
    results = requests.get('https://www.gutenberg.org/ebooks/search/', params).json()

    if len(results) != 4 or len(results[3]) <= 1:
        logging.warn("No Gutenberg results for %s" % title)
        return None

    match = re.match(r'^/ebooks/(\d+)\.json$', results[3][1])
    if not match:
        logging.warn("Unexpected JSON from Gutenberg")

    guten_id = match.group(1)
    url = "https://www.gutenberg.org/cache/epub/%s/pg%s.txt" % (guten_id, guten_id)

    logging.info("fetching text from %s" % url)
    return requests.get(url).text

if __name__ == "__main__":
    main()

