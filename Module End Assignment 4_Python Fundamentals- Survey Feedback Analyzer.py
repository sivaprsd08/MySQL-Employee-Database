feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj',
             'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],

    'Feedback': [
        '   Very GOOD Service!!!',
        'poor support,        not happy   ',
        'GREAT experience! will come again.',
        'okay     okay...',
        '   not    BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],

    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}


print("====================================")
print("       SURVEY FEEDBACK ANALYZER")
print("====================================")

# STEP 2: ADD MORE FEEDBACKS
# -----------------------------------------------------

n = int(input("\nHow many additional feedbacks do you want to add? "))

for i in range(n):

    print("\nEnter details for feedback", i + 1)

    name = input("Enter customer name: ")

    feedback = input("Enter written feedback: ")

    rating = int(input("Enter rating (1-5): "))

    # Generate serial number automatically
    s_no = len(feedback_data['S_No']) + 1

    # Add new data to dictionary
    feedback_data['S_No'].append(s_no)

    feedback_data['Name'].append(name)

    feedback_data['Feedback'].append(feedback)

    feedback_data['Rating'].append(rating)


print("\nNew feedbacks added successfully!")

# STEP 3: TEXT CLEANING
# -----------------------------------------------------

for i in range(len(feedback_data['Feedback'])):

    text = feedback_data['Feedback'][i]

    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('!', '')
    text = text.replace('?', '')

    # Remove extra spaces
    text = ' '.join(text.split())

    # Update cleaned feedback
    feedback_data['Feedback'][i] = text


print("\nAll feedbacks cleaned successfully!")

# STEP 4: WORD COUNT INSIGHTS
# -----------------------------------------------------

def count_word_in_feedbacks(word):

    count = 0

    for feedback in feedback_data['Feedback']:

        words = feedback.split()

        if word.lower() in words:

            count += 1

    return count


print("\n====================================")
print("          WORD COUNT INSIGHTS")
print("====================================")

print("Feedbacks containing 'good':",
      count_word_in_feedbacks("good"))

print("Feedbacks containing 'poor':",
      count_word_in_feedbacks("poor"))

print("Feedbacks containing 'excellent':",
      count_word_in_feedbacks("excellent"))

# STEP 5: FINAL SUMMARY AND INSIGHTS
# -----------------------------------------------------

# 5.1 Display final cleaned feedback data

print("\n====================================")
print("      FINAL CLEANED FEEDBACK DATA")
print("====================================")

print(feedback_data)


# 5.2 Calculate average rating

total_rating = sum(feedback_data['Rating'])

total_feedbacks = len(feedback_data['Rating'])

average_rating = total_rating / total_feedbacks

print("\nAverage Rating:", round(average_rating, 2))


# 5.3 Find feedback with the longest comment

longest_feedback = ""

max_words = 0

for feedback in feedback_data['Feedback']:

    word_count = len(feedback.split())

    if word_count > max_words:

        max_words = word_count

        longest_feedback = feedback


print("\n====================================")
print("          LONGEST FEEDBACK")
print("====================================")

print("Feedback:", longest_feedback)

print("Word Count:", max_words)


# 5.4 Find unique words across all feedbacks

unique_words = []

for feedback in feedback_data['Feedback']:

    words = feedback.split()

    for word in words:

        if word not in unique_words:

            unique_words.append(word)


print("\n====================================")
print("             UNIQUE WORDS")
print("====================================")

print(unique_words)
