domains = {
    "Ukraine": "UA",
    "USA": "US",
    "United Kingdom": "UK",
    "Russia": "RU",
    "Poland": "PL"
}

capitals = {
    "UA": "Kyiv",
    "US": "Washington",
    "UK": "London",
    "RU": "Moscow",
    "PL": "Warsaw"
}

domains["China"] = "CN"
capitals["CN"] = "Peking"


for each in domains:
    print("Domain for", each, "is", domains[each])
    print("The capital of", each, "is", capitals[domains[each]])

domains = {key: [value, "COM", "GOV"] for key, value in domains.items()} 