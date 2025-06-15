def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hod" in user_input:
        return "The HOD is Dr. Karthikeyan, available in room 302."
    elif "mentor" in user_input:
        return "Your mentor is Mrs. Lavanya. Office hours: Wednesday."
    elif "timetable" in user_input:
        return "Timetable is available on the department website."
    elif "exam" in user_input:
        return "Mid-sem exams begin July 10th."
    else:
        return "Sorry, I didn’t get that. Try asking about HOD, mentor, or exams."
