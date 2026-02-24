class patient:
    def __init__(self, name, age, walk, resp, bleeding):
        self . name = name
        self . age = age
        self . can_walk = walk
        self . respiration_rate = resp
        self . has_severe_bleeding = bleeding
        self . color = "Uncertain"

    def triage(self):
        if self.respiration_rate == 0 :
            self.color = "(Deceased)Black"
        elif self.can_walk :
            self.color = "(Outpatient)Green"
        elif self.has_severe_bleeding or self.respiration_rate > 30 :
            self.color = "(Urgent)Red"
        else:
            self.color = "(Delayed)yellow"

all_patients = []
print("Welcome to the crisis management system.")
print("To finish the task, type exit in the name field.")

while True:
    name = input("\nName of the injured person:")
    if name.lower() == "exit" :
        break

    try:
        age = int(input("Age: "))


        walk_input = input("Does he walk? (yes/no): ").lower().strip()
        can_walk = True if walk_input == "yes" else False

        resp = int(input("Number of breaths: "))

        bleed_input = input("Is there heavy bleeding? (yes/no): ").lower().strip()
        has_bleeding = True if bleed_input == "yes" else False

        p = patient(name, age, can_walk, resp, has_bleeding)
        p.triage()

        all_patients.append(p)
        print(f" {name} Triaged successfully: {p.color}")

    except ValueError:
        print("Error: please enter a number for Age and Breaths. ")

print("\n" + "=" * 30)
print("Final report of the injured on the scene:")
for p in all_patients :
    print(f"- {p.name} ({p.age} Year old ) -> {p.color}  ")

import matplotlib.pyplot as plt

if len(all_patients) > 0 :
    total_age = sum(p.age for p in all_patients)
    average_age = total_age / len(all_patients)
    print(f"\n Average age of all injured: {average_age:.1f}")

colors_list = [p.color for p in all_patients]
categories = ["(Deceased)Black", "(Outpatient)Green", "(Urgent)Red", "(Delayed)yellow"]
counts = [colors_list.count(cat) for cat in categories]

plt.figure(figsize= (10, 6))
plt.bar(categories, counts, color=['black', 'green', 'red', 'yellow'])
plt.title("Triage Statistics on Scene")
plt.xlabel("Triage Category")
plt.ylabel("Number of Patients")

print("\n Opening the statistics chart... ")
plt.show()