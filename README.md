# public_domains

*public_domains* searches through a text file (preferably a novel like Moby Dick) and looks for possible host names to use. For more about why it was created see:

https://parkerhiggins.net/2022/11/public-sub-domains

## Install

```
$ pip3 install public_domains
```

## Use

Get a text, e.g. from [Project Gutenberg](https://www.gutenberg.org/):

```
wget https://www.gutenberg.org/files/2701/2701-0.txt
```

Run:

```
public_domains 2701-0.txt

tattooing.burned.like
fishermen.technically.call
violent.scraping.contact
irregular.between.here
verbally.developed.here
mizzen.rigging.like
eepeningly.contracted.like
tropic.whaling.life
trailing.behind.like
certain.fragmentary.parts
redundant.yellow.hair
personality.stands.here
wicked.miserable.world
...
```

If you'd like *public_domains* to check if the domain is available use the the `--check` option:





