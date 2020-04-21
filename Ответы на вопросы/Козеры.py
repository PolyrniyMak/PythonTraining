json = {"bomonque": [{"iu": [{"iu-1": []}, {"iu10": [{"cozers": ["Zversky", "GoldGem", "Cnya176"]}]}]},
                     {"fn": [{"fn-12": [{"obercozers": [], "cozers": ["Ivanov", "Petrov"]}]}]}]}

for bomonque in json:
    for group in json[bomonque]:
        for iu in group:
            for kaf in group[iu]:
                for kaf2 in kaf:
                    for cors in kaf[kaf2]:
                        for cozerog in cors:
                            for people in cors[cozerog]:
                                print(people)
