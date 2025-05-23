filename = "scores.txt"

score_list = []
score_data= []


def display_scores(scores):
    print(f"{'Name':20} {'score':^20}")
    for score,name in scores:
        print(f"{name:20} {score:^20}")


file_handle = open(filename,"r")
score_data = file_handle.readlines()
file_handle.close()

for score_and_name in score_data:
    score_and_name = score_and_name.split(",")

    score = int(score_and_name[1].strip())
    name = score_and_name[0].strip()

    score_list.append((score,name))

print("Before Sort")
print("-"*40)
display_scores(score_list)

score_list.sort(reverse=True)

print("After Sort")
print("-"*40)
display_scores(score_list)

print("-"*40)

save_scores = ""
while save_scores not in ["y","n"]:
    save_scores = input("Do you want to save the scores (Y/N)?").lower()

if save_scores == "y":
    score_file = open("scores.txt", "w")
    for score in score_list:
        a_score = score[1]
        a_name = score[0]
        score_file.write(f"{a_name}, {a_score}\n")
