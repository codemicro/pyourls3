import pyourls3

your_site = "https://example.com/"

urls = pyourls3.Yourls(your_site, user="username", passwd="password123")

# Shorten a link, giving it a custom keyword and title
r = urls.shorten("https://www.jetbrains.com", keyword="bestides", title="JetBrains makes nice IDEs")
print(r["shorturl"])

# Expand a link
r = urls.expand("bestides")
print(r)

# Get stats for a shortened link
r = urls.url_stats("bestides")
print(r)

# Get global installation stats
r = urls.stats()
print(r)