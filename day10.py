careers = [
    {"career": "Software Engineer", "salary": 30, "remote": True},
    {"career": "Cybersecurity", "salary": 25, "remote": True},
    {"career": "Web Developer", "salary": 20, "remote": True},
    {"career": "IT Support", "salary": 18, "remote": False}
]

for job in careers:
    if job["salary"] >= 25 and job["remote"]:
        print(f"{job["career"]} - ${job["salary"]}/hr -  Remote")