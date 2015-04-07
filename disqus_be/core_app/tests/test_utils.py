from core_app import utils
from sure import expect


def test_url_parse1():
    samples = [
        ("https://www.google.kz/?gws_rd="
         "cr&ei=OowNVaPxIdXdavjsgcgH", "google.kz/"),
        ("https://www.google.kz", "google.kz/"),
        ("http://www.google.kz", "google.kz/"),
        ("http://google.kz", "google.kz/"),
        ("google.kz", "google.kz/"),
        ("google.kz/index.html", "google.kz/index.html"),
    ]
    for tst, ans in samples:
        res = utils.clear_uri(tst)
        expect(res).should.be.equal(ans)


def test_url_parse2():
    utils.clear_uri.when.called_with('').should.throw(AssertionError)
