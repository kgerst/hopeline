def ask_feeling():
    return {
        'id': 1,
        'message': "Are you planning to harm yourself? Reply Yes or No"
    }

def suggest_911():
	response = "Please call 911."
	info = "Additional Resources"

	d1 = "National Suicide Prevention Lifeline"
	r1 = "https://suicidepreventionlifeline.org/"
	n1 = "1-800-273-8255"

	d2 = "Suicide Awareness Voices of Education (SAVE)"
	r2 = "http://www.save.org/"

	d3 = "American Foundation for Suicide Prevention (AFSP)"
	r3 = "https://afsp.org/"

	d4 = "National Alliance on Mental Illness (NAMI)"
	r4 = "http://www.nami.org/"
	return {
        'id': 2,
        'message': "{0} \n\n{1}:\n\n{2}:\n{3}\n{4} \n\n{5}:\n{6} \n\n{7}:\n{8} \n\n{9}:\n{10}".format(response, info, d1, r1, n1, d2, r2, d3, r3, d4, r4)
    }

def ask_to_reach_out():
	return {
        'id': 3,
        'message': "You may be feeling sad or anxious. Have you talked to someone about this feeling? Reply Yes or No"
    }

def ask_willingness():
	return {
        'id': 4,
        'message': "Are you willing to? Reply Yes or No"
    }

def ask_type_of_contact():
	return {
        'id': 5,
        'message': "Do you want help connecting with a Professional or reaching out to someone you have a personal connection to? Reply Professional or Personal"
    }

def give_resources():
	d1 = "Find a Mental Health Professional"
	r1 = "https://afsp.org/find-support/find-mental-health-professional/"
	d2 = "SAMHSA/Substance Abuse and Mental Health Services Administration"
	r2 = "https://findtreatment.samhsa.gov/"
	d3 = "MHA/Mental Health America"
	r3 = "http://www.mentalhealthamerica.net/finding-help"
	d4 = "National Suicide Prevention Lifeline"
	r4 = "https://suicidepreventionlifeline.org/help-yourself/"
	return {
        'id': 6,
        'message': "Here are some resources:\n\n {0}: {1}\n\n {2}: {3}\n\n {4}: {5}\n\n {6}:{7}".format(d1, r1, d2, r2, d3, r3, d4, r4)
    }

def suggest_how_to_start_convo():
	quote = '“… WHEN “I” IS REPLACED WITH “WE”, ILLNESS BECOMES WELLNESS.” -Shannon L. Alder'
	intro = "steps to get a conversation started: "
	l1 = "1. Write down your current emotions and thoughts."
	l2 = "2. Write down a list of people who bring you joy."
	l3 = "3. Pick a person from your list and write down ways they could help you. Could it help if they just listen? Could they help you problem solve? Could they help you do something like go for a walk or eat with you?"
	l4 = "4. Reach out! If they aren't available, you can pick another person from your list and go back to step 3. Did this help? Reply Yes or No"
	return {
        'id': 7,
        'message': "{0} \n\n{1} \n\n{2} \n\n{3} \n\n{4} \n\n{5}".format(quote, intro, l1, l2, l3, l4)
    }

def suggest_skills():
	return {
        'id': 8,
        'message': "Want to try a skill to help yourself? Reply Yes or No"
    }