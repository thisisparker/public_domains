import logging
import public_domains

logging.basicConfig(filename="test.log", level=logging.DEBUG)

def test_get_hosts():
    hosts = public_domains.get_hosts('test-data/moby-dick.txt', quiet=True)
    assert len(hosts) == 145
    assert "almost.looked.next" in hosts

def test_available():
    assert public_domains.available("this.parkerhiggins.net") == False
    assert public_domains.available("choo.choo.choo") == True

def test_get_tlds():
    tlds = public_domains.get_tlds()
    assert len(tlds) > 0
    assert "org" in tlds

def test_gutenberg():
    text = public_domains.gutenberg('origin of the species')
    assert len(text) > 0
    assert "I shall discuss the complex and little known laws" in text
