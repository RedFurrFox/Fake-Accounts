# Required Packages/Modules
import os
import yaml
import random

# Main Function
def Main():
    # Opens "Settings.yaml" For The Required Datas
    with open("Settings.yaml", "r") as s:
        y = yaml.safe_load(s)

        # Dictionaries
        First_Name = y["Fake_Credentials"]["Firstname"]
        Last_Name = y["Fake_Credentials"]["Lastname"]
        Extra = y["Fake_Credentials"]["Extra"]
        Punctuation = y["Fake_Credentials"]["Punctuations"]
        Email = y["Fake_Credentials"]["Emails"]
        Company = y["Fake_Credentials"]["Company"]
        Domain = y["Fake_Credentials"]["Domain"]
        Password = y["Fake_Credentials"]["Password"]
        Symbol = y["Fake_Credentials"]["Symbols"]

    # Loop
    for Loop in range(0, 1000):

        # Randomazer
        Random_FN = random.choice(First_Name)
        Random_LN = random.choice(Last_Name)
        Random_Ex = random.choice(Extra)
        Random_Pu = random.choice(Punctuation)
        Random_Em = random.choice(Email)
        Random_Co = random.choice(Company)
        Random_Do = random.choice(Domain)
        Random_Pa = random.choice(Password)
        Random_Sy = random.choice(Symbol)

        # Making The Given Data Valid
        Username_1 = random.choice([Random_FN + random.choice([Random_Pu, Random_Sy]) + Random_LN, Random_LN + random.choice([Random_Pu, Random_Sy]) + Random_FN]) + "@" + Random_Em + "." + Random_Do
        Username_2 = random.choice([Random_FN + random.choice([Random_Pu, Random_Sy]) + Random_LN, Random_LN + random.choice([Random_Pu, Random_Sy]) + Random_FN]) + "@" + Random_Ex + "." + Random_Do
        Username_3 = Random_Ex + "@" + random.choice([Random_FN, Random_LN, Random_Co]) + "." + Random_Do
        Password_1 = Random_Pa + random.choice([Random_Pu, Random_Sy]) + random.choice([Random_FN, Random_LN, random.choice([Random_FN + Random_LN]) + random.choice([Random_FN + Random_LN])])
        Password_2 = random.choice([Random_FN, Random_LN]) + random.choice([Random_Pu, Random_Sy]) + Random_Co
        Password_3 = random.choice([Random_FN + Random_LN, Random_LN + Random_FN]) + random.choice([Random_Pu, Random_Sy]) + Random_Pa + random.choice([Random_Pu, Random_Sy]) + random.choice([Random_Em, Random_Do, Random_Co])

        # Random Choosing
        Username = random.choice([Username_1, Username_2, Username_3])
        Password = random.choice([Password_1, Password_2, Password_3])

        print(f'({Loop + 1}) Username: {Username} || Password: {Password}')


if __name__ == "__main__":
    if os.path.exists("Settings"):
        Main()
    else:
        with open("Settings.yaml", "w") as Writer:
            Writer.write("""Fake_Credentials:

  # Changeable
  Firstname:
      - "james"
      - "mary"
      - "robert"
      - "patricia"
      - "john"
      - "jennifer"
      - "michael"
      - "linda"
      - "william"
      - "elizabeth"
      - "david"
      - "barbara"
      - "richard"
      - "susan"
      - "joseph"
      - "jessica"
      - "thomas"
      - "sarah"
      - "charles"
      - "karen"
      - "christopher"
      - "nancy"
      - "daniel"
      - "lisa"
      - "matthew"
      - "betty"
      - "anthony"
      - "margare"
      - "mark"
      - "sandra"
      - "donald"
      - "ashley"
      - "steven"
      - "kimberly"
      - "paul"
      - "emily"
      - "andrew"
      - "donna"
      - "joshua"
      - "michelle"
      - "kenneth"
      - "dorothy"
      - "kevin"
      - "carol"
      - "brian"
      - "amanda"
      - "george"
      - "melissa"
      - "edward"
      - "deborah"
      - "ronald"
      - "stephanie"
      - "timothy"
      - "rebecca"
      - "jason"
      - "sharon"
      - "jeffrey"
      - "laura"
      - "ryan"
      - "cynthia"

  # Changeable
  Lastname:
      - "jacob"
      - "kathleen"
      - "gary"
      - "amy"
      - "nicholas"
      - "shirley"
      - "eric"
      - "angela"
      - "jonathan"
      - "helen"
      - "stephen"
      - "anna"
      - "larry"
      - "brenda"
      - "justin"
      - "pamela"
      - "scott"
      - "nicole"
      - "brandon"
      - "emma"
      - "benjamin"
      - "samantha"
      - "samuel"
      - "katherine"
      - "gregory"
      - "christine"
      - "frank"
      - "debr"
      - "alexander"
      - "rachel"
      - "raymond"
      - "catherine"
      - "patrick"
      - "carolyn"
      - "jack"
      - "janet"
      - "dennis"
      - "ruth"
      - "jerry"
      - "maria"
      - "tyler"
      - "heather"
      - "aaron"
      - "diane"
      - "jose"
      - "virginia"
      - "adam"
      - "julie"
      - "henry"
      - "joyce"
      - "nathan"
      - "victoria"
      - "douglas"
      - "olivia"
      - "zachary"
      - "kelly"
      - "peter"
      - "christina"
      - "kyle"
      - "lauren"

  # Changeable
  Extra:
      - "community"
      - "help"
      - "support"
      - "gaming"
      - "admin"
      - "team"
      - "group"

  # DO NOT CHANGE THIS, IT WILL MAKE YOUR GENERATED EMAILS LOOKS INVALID!!!
  Punctuations:
      - "-"
      - "."
      - "_"
      - ""

  # Changeable
  Emails:
      - "gmail"
      - "outlook"
      - "yahoo"
      - "horde"
      - "samsung"
      - "vivo"
      - "oppo"

  # Changeable
  Company:
      - "lulz"
      - "crocks"
      - "minions"
      - "genteng"
      - "lienshng"
      - "kiss"
      - "lips"

  # Changeable
  Domain:
      - "com"
      - "me"
      - "tk"
      - "msn"
      - "shop"
      - "xyz"

  # Changeable
  Password:
      - "123456789"
      - "987654321"
      - "qwerty"
      - "QWERTY"
      - "dragon"
      - "DRAGON"
      - "Admin"
      - "User"
      - "Windows"
      - "Linux"
      - "Android"
      - "Apple"
      - "ILoveYou"
      - "LoveLetter"
      - "Hentai"
      - "Heaven"
      - "ILove"
      - "IHate"
      - "Dirt"

  # Changeable
  Symbols:
      - "!"
      - "#"
      - "$"
      - "%"
      - "^"
      - "&"
      - "*"
      - "("
      - ")"
      - ">"
      - "<"
      - "?"
      - "/"
      - '\'
      - '"'
      - "'"
      - " " """)
            Writer.close()
        Main()
