import yaml
import random

with open("Settings.yaml", "r") as s:
    y = yaml.safe_load(s)

    account1 = random.choice(y["Fake_Credentials"]["firstname"]) + random.choice(y["Fake_Credentials"]["punctuations"]) + random.choice(y["Fake_Credentials"]["lastname"]) + "@" + random.choice(y["Fake_Credentials"]["emails"]) + "." + random.choice(y["Fake_Credentials"]["domain"])
    account2 = random.choice(y["Fake_Credentials"]["firstname"]) + random.choice(y["Fake_Credentials"]["punctuations"]) + random.choice(y["Fake_Credentials"]["lastname"]) + "@" + random.choice(y["Fake_Credentials"]["extra"]) + "." + random.choice(y["Fake_Credentials"]["domain"])
    account3 = random.choice(y["Fake_Credentials"]["extra"]) + "@" + random.choice(y["Fake_Credentials"]["company"]) + "." + random.choice(y["Fake_Credentials"]["domain"])

    password1 = random.choice(y["Fake_Credentials"]["password"]) + random.choice([y["Fake_Credentials"]["punctuation"], y["Fake_Credentials"]["symbols"]]) + random.choice(y["Fake_Credentials"]["password"])
    password2 = random.choice(y["Fake_Credentials"]["password"]) + random.choice([y["Fake_Credentials"]["punctuation"], y["Fake_Credentials"]["symbols"]]) + random.choice(y["Fake_Credentials"]["password"]) + random.choice([y["Fake_Credentials"]["punctuation"], y["Fake_Credentials"]["symbols"]]) + random.choice(y["Fake_Credentials"]["password"])
    password3 = random.choice(y["Fake_Credentials"]["punctuation"]) + random.choice(y["Fake_Credentials"]["password"]) + "@" + random.choice(y["Fake_Credentials"]["company"])

    print(random.choice([account1 + " :: " + password1, account2 + " :: " + password2, account3 + " :: " + password3]))
