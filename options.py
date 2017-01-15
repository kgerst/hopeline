def ask_feeling():
    return {
        'id': 1,
        'message': "Are you planning to harm yourself? Reply Yes or No"
    }

def suggest_911():
    return {
        'id': 2,
        'message': "Please call 911."
    }

def ask_to_reach_out():
	return {
        'id': 3,
        'message': "Have you talked to someone about this feeling? Reply Yes or No"
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
	return {
        'id': 7,
        'message': "DEARMAN How to"
    }

def suggest_skills():
	return {
        'id': 8,
        'message': "Want to try a skill to help yourself? Reply Yes or No"
    }