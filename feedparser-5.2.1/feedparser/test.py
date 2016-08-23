import feedparser
d = feedparser.parse("https://www.us-cert.gov/ncas/alerts.xml")

print d['feed']['title']

print d.feed.subtitle

print d['entries']

