import subprocess

countries = ["ad", "ae", "af", "ag", "ai", "al", "am", "ao", "aq", "ar", "as", "at", "au", "aw", "ax", "az", "ba", "bb", "bd", "be", "bf", "bg", "bh", "bi", "bj", "bl", "bm", "bn", "bo", "bq", "br", "bs", "bt", "bv", "bw", "by", "bz", "ca", "cc", "cd", "cf", "cg", "ch", "ci", "ck", "cl", "cm", "cn", "co", "cr", "cu", "cv", "cw", "cx", "cy", "cz", "de", "dj", "dk", "dm", "do", "dz", "ec", "ee", "eg", "eh", "er", "es", "et", "fi", "fj", "fk", "fm", "fo", "fr", "ga", "gb", "gd", "ge", "gf", "gg", "gh", "gi", "gl", "gm", "gn", "gp", "gq", "gr", "gs", "gt", "gu", "gw", "gy", "hk", "hm", "hn", "hr", "ht", "hu", "id", "ie", "il", "im", "in", "io", "iq", "ir", "is", "it", "je", "jm", "jo", "jp", "ke", "kg", "kh", "ki", "km", "kn", "kp", "kr", "kw", "ky", "kz", "la", "lb", "lc", "li", "lk", "lr", "ls", "lt", "lu", "lv", "ly", "ma", "mc", "md", "me", "mf", "mg", "mh", "mk", "ml", "mm", "mn", "mo", "mp", "mq", "mr", "ms", "mt", "mu", "mv", "mw", "mx", "my", "mz", "na", "nc", "ne", "nf", "ng", "ni", "nl", "no", "np", "nr", "nu", "nz", "om", "pa", "pe", "pf", "pg", "ph", "pk", "pl", "pm", "pn", "pr", "ps", "pt", "pw", "py", "qa", "re", "ro", "rs", "ru", "rw", "sa", "sb", "sc", "sd", "se", "sg", "sh", "si", "sj", "sk", "sl", "sm", "sn", "so", "sr", "ss", "st", "sv", "sx", "sy", "sz", "tc", "td", "tf", "tg", "th", "tj", "tk", "tl", "tm", "tn", "to", "tr", "tt", "tv", "tw", "tz", "ua", "ug", "um", "us", "uy", "uz", "va", "vc", "ve", "vg", "vi", "vn", "vu", "wf", "ws", "xk", "ye", "yt", "za", "zm", "zw"]  # noqa

for country in countries:
    """
    Loop through each country (2-digit ISO), and download asset into respective folder.
    wget -P [path-to-save-in] [url to download]
    """
    # subprocess.call(["wget", "-P", "world-flags/svg/", f"https://assets.2bn.dev/flags/svg/{country}.svg"])    # /svg/
    # subprocess.call(["wget", "-P", "world-flags/icon/", f"https://assets.2bn.dev/flags/icon/{country}.png"])  # /icon/
    # subprocess.call(["wget", "-P", "world-flags/sm/", f"https://assets.2bn.dev/flags/sm/{country}.png"])      # /sm/
    # subprocess.call(["wget", "-P", "world-flags/md/", f"https://assets.2bn.dev/flags/md/{country}.png"])      # /md/
    # subprocess.call(["wget", "-P", "world-flags/lg/", f"https://assets.2bn.dev/flags/lg/{country}.png"])      # /lg/
    # subprocess.call(["wget", "-P", "world-flags/xl/", f"https://assets.2bn.dev/flags/xl/{country}.png"])      # /xl/
    # subprocess.call(["wget", "-P", "world-flags/full/", f"https://assets.2bn.dev/flags/full/{country}.png"])  # /full/
    pass
