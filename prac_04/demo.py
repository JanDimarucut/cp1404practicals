def main():
    score_file = open("scores.csv")
    score_data = score_file.readlines()
    subjects = score_data[0].strip().split(",")
    score_values = []
    for score_line in score_data:
        score_strings = score_line.strip()
        print(score_strings)
        score_numbers = []
        for value in score_strings:
            score_numbers.append(int(value))
            score_values.append(score_numbers)
            print(score_values)
    score_file.close()
# score_numbers = [int(value) for value in score_strings]
# score_values.append(score_numbers)
# print(score_numbers)

#    scores_by_subject = reorganise_scores_by_subjects(score_values)
#    display_subject_details(scores_by_subject, subjects)


# def reorganise_scores_by_subjects(score_value):
#    subject_scores = []
#    number_of_subjects = len(score_value[0])
#    for i in range(number_of_subjects):
#        scores_for_one_subject = []
#        for scores in score_value:
#            scores_for_one_subject.append(scores.pop(0))
#        subject_scores.append(scores_for_one_subject)
#    return subject_scores


# def display_subject_details(scores_by_subject, subject_name):
#    for i, scores_for_one_subject in enumerate(scores_by_subject):
#        print(subject_name[i], "Scores:")
#        for score in scores_for_one_subject:
#            print("{:>2}".format(score))
#        print("Max: {:3}".format(max(scores_for_one_subject)))
#        print("Min: {:3}".format(min(scores_for_one_subject)))
#        print("Avg: {:6.2f}\n".format(
#            (sum(scores_for_one_subject) / len(scores_for_one_subject))))


main()
