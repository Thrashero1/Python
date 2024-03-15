statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


def online_count(status):
    people_online = 0
    for key in status:
        if status[key] == 'online':
            people_online += 1
    return people_online


print(online_count(statuses))