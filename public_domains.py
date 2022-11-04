import string
import sys

import requests
import whois

from nltk import tokenize

BOOKFILE = sys.argv[1]
OUTPUTFILE = BOOKFILE + '.possible-domains.txt'

tlds = []
known_unavailable = ['smile', 'windows','active','amazon','apple','audible',
                     'bank','baseball','basketball','boots','case','drive',
                     'fast','fire','fly','museum','origins','post','prime',
                     'silk','weather']

r = requests.get("https://data.iana.org/TLD/tlds-alpha-by-domain.txt")
for d in r.text.splitlines():
    if d.startswith("#") or d.startswith('XN--'):
        continue
    d = d.lower()
    if d not in known_unavailable:
        tlds.append(d)

with open(BOOKFILE, 'r') as f:
    md = ' '.join([l.strip() for l in f.readlines()])

md_sents = tokenize.sent_tokenize(md)

possible_domains = {}

for s in md_sents:
     wl = tokenize.word_tokenize(s)
     wl = [w.lower() for w in wl]
     wl = [''.join([c for c in w if c in string.ascii_lowercase]) for w in wl]
     wl = [w for w in wl if w]
     for i, w in enumerate(wl):
         if (i > 1 and w in tlds and len(w) > 3 
                 and len(wl[i-1]) > 5 and len(wl[i-2]) > 5):
             full_domain = '.'.join([wl[i-2], wl[i-1], w])
             
             try:
                 d = whois.query(full_domain.split('.',1)[1])
                 possible_domains[full_domain] = 'reg' if d else 'unreg'
             except (whois.exceptions.UnknownTld,
                     whois.exceptions.FailedParsingWhoisOutput):
                 possible_domains[full_domain] = 'unknown'
             
emoji_prefix = {'reg':'❌', 'unreg':'✔️', 'unknown':'❔'}

with open(OUTPUTFILE, 'w') as f:
    for d in possible_domains:
        f.write(f'{emoji_prefix[possible_domains[d]]} {d}\n')