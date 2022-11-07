# public_domains

[![Build Status](https://github.com/thisisparker/public_domains/workflows/tests/badge.svg)](https://github.com/thisisparker/public_domains/actions/workflows/main.yml)

*public_domains* searches through a text (such as a novel like [Moby Dick](https://www.gutenberg.org/files/2701/2701-0.txt)) and looks for possible host names to use. For more context about why such a thing was created see:

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

```bash
$ public_domains 2701-0.txt

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

Or if you prefer to do a "feeling lucky" search of gutenberg.org you can enter a title:

```bash
$ public_domains "Treasure Island"

famous.buccaneer.here
maroon.wriggling.like
keeping.better.watch
little.mountain.stream
admiral.benbow.black
breathing.loudly.like
breath.hanging.like
shirts.thrown.open
promontory.without.fail
feverish.unhealthy.spot
something.almost.like
following.important.news
lookout.shouted.land
spirits.eating.like
resumed.silver.here
stranded.beyond.help
trebly.worthless.life
including.checks.online
canvas.cracking.like
almost.entirely.exposed
flowers.ablowing.like
counting.hawkins.here
little.stranger.here
foliage.compact.like
strange.collection.like
seamen.aboard.here
creature.flitted.like
nighhand.fainting.doctor
crying.johnny.black
enough.little.place
```


If you'd like *public_domains* to check if the domain is available use the the `--check` option:

<img width="800" src="https://raw.githubusercontent.com/edsu/public_domains/main/screenshot.gif">

