# friendsは直近14日以内に会った人
friends = []
friend = {"condition": "Saiaku", "body_temperature": 40}
friends.append(friend)
friends[0] = friend
for friend in friends:
    if friend["condition"] == "COVID-19":
        print("外出ダメ")
    elif friend["body_temperature"] >= 37.5:
        print("わかるまで看病も控える")
        print(friend["condition"])
    else:
        print("外出OK")