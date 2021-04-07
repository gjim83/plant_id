# Thoughts/notes:
#
# 1. Maybe if there is no text/image/etc, don't have the field at all as opposed to an empty string?
# 2. If a question has "Other" as a possible answer, should matching plants either:
#    - Not have that property at all and the code matches plants without that property if that was the option that was chosen?
#    - Have that property explicitly set as "Other"?


# ======================================================================
# Simplified decision system
# ======================================================================
decision_system = {
    "questions": [
        {  # Question 1
            "q_id": "shape",
            "q_title": "Shape",
            "q_text": "What is the shape of the plant?"
            "q_options": [  # possible answers
                {
                    "opt_id": "flower",
                    "opt_title": "Blooming Flower",
                    "opt_text": "",
                    "opt_image": "",
                    "opt_suboptions": [
                        {
                            "subopt_id": "red-pink",
                            "subopt_title": "Reddish/Pink",
                            "subopt_text": "",
                            "subopt_image": ""
                        },
                        {
                            "subopt_id": "blue-purple",
                            "subopt_title": "Blue/Purple",
                            "subopt_text": "",
                            "subopt_image": ""
                        },
                        {
                            "subopt_id": "other",
                            "subopt_title": "Other",
                            "subopt_text": "",
                            "subopt_image": ""
                        }
                    ]
                },
                {
                    "opt_id": "tree",
                    "opt_title": "Tree",
                    "opt_text": "Some explanatory text and a clickable image",
                    "opt_img": "/path/or/reference/to/image.svg"
                },
                {
                    "opt_id": "shurb",
                    "opt_title": "Shrub",
                    "opt_text": "Some explanatory text and a clickable image",
                    "opt_img": "/path/or/reference/to/image.svg"
                },
                {
                    "opt_id": "palm",
                    "opt_title": "Palm/Palm-like",
                    "opt_text": "Some explanatory text and a clickable image",
                    "opt_img": "/path/or/reference/to/image.svg"
                }
            ]
        },
        {  # Question 2
            "q_id": "leaves",
            "q_title": "Leaves",
            "q_text": "What is the shape of the leaves?"
            "q_options": [  # possible answers
                {
                    "opt_id": "simple",
                    "opt_title": "Simple",
                    "opt_text": "",
                    "opt_image": "",
                    "opt_suboptions": [
                        {
                            "subopt_id": "articular",
                            "subopt_title": "Articular (needle-like)",
                            "subopt_text": "",
                            "subopt_image": ""
                        },
                        {
                            "subopt_id": "linear",
                            "subopt_title": "Linear",
                            "subopt_text": "",
                            "subopt_image": ""
                        },
                        {
                            "subopt_id": "other",
                            "subopt_title": "Simple with other shape",
                            "subopt_text": "",
                            "subopt_image": ""
                        }
                    ]
                },
                {
                    "opt_id": "compound",
                    "opt_title": "Compound",
                    "opt_text": "",
                    "opt_image": "",
                    "opt_suboptions": [
                        {
                            "subopt_id": "mono-unifoliolate",
                            "subopt_title": "Mono- or Unifoliolate",
                            "subopt_text": "",
                            "subopt_image": ""
                        },
                        {
                            "subopt_id": "bifoliolate",
                            "subopt_title": "Bifoliolate",
                            "subopt_text": "",
                            "subopt_image": ""
                        }
                    ]
                },
            ]
        },
        {  # Question 3
            "q_id": "margin",
            "q_title": "Margin",
            "q_text": "What does the margin of the leaves look like?"
            "q_options": [  # possible answers
                {
                    "opt_id": "entire",
                    "opt_title": "Entire",
                    "opt_text": "",
                    "opt_image": "",
                    "opt_suboptions": []  # question 1 on top
                },
                {
                    "opt_id": "serrate",
                    "opt_title": "Serrate or serrulate",
                    "opt_text": "",
                    "opt_image": "",
                    "opt_suboptions": []  # question 1 on top
                },
                {
                    "opt_id": "crenate",
                    "opt_title": "Crenate, Dentate, or Denticulate",
                    "opt_text": "",
                    "opt_image": "",
                    "opt_suboptions": []  # question 1 on top
                },
                {
                    "opt_id": "other",  # question 2 on top
                    "opt_title": "Other",
                    "opt_text": "",
                    "opt_image": "",
                    "opt_suboptions": []
                }
            ]
        }
    ]
}


# ======================================================================
# Mock data
# ======================================================================

# Notes about display:
#
# I'd like to keep a code-friendly ip for all parameters, but also have the ability to
# define a display format. The display can either be set explicitly with the ``display`` key, or
# can be inferred from the name by doing ``string.replace('_', ' ').title()``
#
# If a value is a string, display as is, if it's a list then ``', '.join(...)``

# Notes about tests with mock data:
#
# 1. If a user selects shape as "shrub", they should be taken directly to the 3rd option of the mock data below
#    because there are no further options possible (this wouldn't happen in the real version so early in the decision
#    process, but it may further down)
# 2. If a user selects shape as "tree", then they should get some feedback (maybe a quickly disappearing interstitial-like element?)
#    that gives them feedback about how many plants match what they have answered so far
# 3. In the same event as 2., for question 2 they should only get "simple-other" and "compound" as possible answers, as those are the only
#    two that are possible, along with a 3rd option "None of the above", which if chosen should display a message that there are no matching
#    plants. Same thing if they get to question 3, it should only display "entire", "serrate" and "None of the above" as potential answers,
#    even if there are more in the decision system.

mock_plant_data = [
    {
        "profile_text": {
            "scientific_name": {
                "value": "Coffea arabica"
            },
            "common_name": {
                "value": "Coffee plant"
            },
            "family": {
                "display": "Family Name",
                "value": "Rubiaceae"
            },
            "other_names": {
                "value": ["café", "cafeto"]
            },
            "long_text": {
                "description": {
                    "value": "The genus Coffea, contains about 25 species. Coffea arabica is a small tree, up to 5 meters tall when unpruned."
                },
                "cultivation": {
                    "value": "Propagation is usually by seed following well programmed methods. Coffee growers raise seedlings which are planted on rows in the coffee fields."
                }
            }
        },
        "profile_images": [
            "/path/to/img1.svg",
            "/path/to/img2.svg"
        ],
        "metadata": {
            "shape:": "tree",
            "leaves": {"simple": "other"},
            "margin": "serrate"
        }
    },
    {
        "profile_text": {
            "scientific_name": {
                "value": "Mangifera Indica"
            },
            "common_name": {
                "value": "Mango"
            },
            "family": {
                "display": "Family Name",
                "value": "Anacardiaceae"
            },
            "other_names": {
                "value": "manga"
            },
            "long_text": {
                "description": {
                    "value": "Mango tree grows to be 9 to 13 m tall and almost 15 m wide. All green parts of the plant yield translucent or yellowish or whitish resinous exudate."
                },
                "climate_and_soils": {
                    "value": "Mango trees grow best in full sun with ample moisture, fertile and well drained soils; but they can tolerate clayish, loamy, sandy, acidic and alkaline soils."
                }
            }
        },
        "profile_images": [
            "/path/to/img1.svg",
            "/path/to/img2.svg"
        ],
        "metadata": {
            "shape:": "tree",
            "leaves": "compound",
            "margin": "entire"
        }
    },
    {
        "profile_text": {
            "scientific_name": {
                "value": "Nomis Scientificus"
            },
            "common_name": {
                "value": "Made up shrub"
            },
            "family": {
                "display": "Family Name",
                "value": "Familiaceae"
            },
            "other_names": {
                "value": "Idunno"
            },
            "long_text": {
                "description": {
                    "value": "I'd add something funny if I had the creativity"
                },
                "climate_and_soils": {
                    "value": "All sorts, you name it."
                }
            }
        },
        "profile_images": [
            "/path/to/img1.svg",
            "/path/to/img2.svg"
        ],
        "metadata": {
            "shape:": "shrub",
            "leaves": {"compound": "bifoliolate"},
            "margin": "other"
        }
    }
]