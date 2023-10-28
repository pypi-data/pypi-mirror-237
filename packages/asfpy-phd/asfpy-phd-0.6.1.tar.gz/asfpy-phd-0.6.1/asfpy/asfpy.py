"""
ASFP Allocation

Say some things about it here.
"""

from operator import itemgetter
import random
import csv

#################################################
# CONSTANTS
#
# NOTE: These constants refer to data fields that
#	are collected in forms, so may be changed
#	accordingly. The forms should also be
#	preprocesseed to have the same labels.
#
#
#################################################

# field identifiers
FLEXIBLE = "flexible"
URM = "urm"
LIM = "lim"
CATEGORIES = "categories"
CAPACITY = "capacity"
COI_FACULTY = "conflicts-faculty"
COI_UNIVERSITY = "conflicts-university"

# null options for applicants to select on required questions
NO_CONFLICTS_FACULTY= "I am not applying to any of these faculty."
NO_CONFLICTS_UNIVERSITY = "My submitted statement is not for ANY of these institutions."

#################################################
# FILE HANDLERS
#################################################

def faculty_conflicts(faculty):
    """
    Extract faculty conflict of interest names and create set containing those
    names. First remove the no_conflict statement, if any. Then return faculty.
    """
    faculty = set(faculty.split(", "))
    return {fac for fac in faculty if NO_CONFLICTS_FACULTY not in fac}

def university_conflicts(universities):
    """
    Extract university conflict of interest names and create set containing those
    names. First remove the no_conflict statement, if any. Then return universities.
    """
    universities = set(universities.split(", "))
    return {uni for uni in universities if NO_CONFLICTS_UNIVERSITY not in uni}

def categories(categories):
    """
    Extract categories from stated categories of respondent.
    """
    return set(categories.split(", "))

def get_element_by_id(_id, group_list):
    """
    Use next generator to find element in a group's list by identifier.
    """
    return next(e for e in group_list if _id == e["id"])

def read_list_csv(filename):
    """
    Use Python's native CSV reader to load list.
    """
    with open(filename) as f:
        loaded = [{k: v for k, v in row.items()}
                for row in csv.DictReader(f, skipinitialspace=True)]
    return loaded

def read_preprocessed_editors_list_csv(filename):
    """
    Use Python's native CSV reader to load the editors list. Also,
    convert category stringlists to sets and endow an identifier.
    """
    editors = read_list_csv(filename)

    n = 1
    for editor in editors:
        editor[CATEGORIES] = categories(editor[CATEGORIES])
        editor[CAPACITY] = int(editor[CAPACITY])
        editor["matchable"] = int(editor["matchable"])
        
        n += 1

    return editors

def read_preprocessed_applicants_list_csv(filename):
    """
    Use Python's native CSV reader to load the applicant submissions list. Also,
    convert category stringlists to sets and endow an identifier.
    """
    applicants = read_list_csv(filename)

    n = 1
    for applicant in applicants:
        applicant[CATEGORIES] = categories(applicant[CATEGORIES])
        applicant[COI_UNIVERSITY] = university_conflicts(applicant[COI_UNIVERSITY])
        applicant[COI_FACULTY] = faculty_conflicts(applicant[COI_FACULTY])

        applicant[FLEXIBLE] = bool(int(applicant[FLEXIBLE]))
        applicant[URM] = bool(int(applicant[URM]))
        applicant[LIM] = bool(int(applicant[LIM]))

        n += 1

    return applicants

def write_list_to_csv(lst, filename):
    """
    Save list of dict elements to file.
    """
    headers = lst[0].keys()
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f, headers)
        w.writeheader()
        w.writerows(lst)

#################################################
# APPLICANT PRIORITY METHODS
#################################################

def asfp_rank(applicant):
    """
    Rank an applicant by attribute combinations by the standard ASFP method of
    ranking by underrepresented minority (URM) status, whether an applicant has
    limited access (LIM) to informed mentors.

    Parameters
    ----------
    applicant: dict
        An object that represents an applicant (often within a list) with 
        attributes including:
            - "id" a unique string identifier
            - "urm" a boolean designation of URM status
            - "lim" a boolean designation of LIM status

    Returns
    -------
    rank: integer
        A ranking that represents an applicant's pool relative to an
        ASFP-designed schema, as clarified through boolean logic in code below.
    """
    is_urm = applicant[URM]
    is_lim = applicant[LIM]

    if (is_urm and is_lim):
        rank = 0
    elif (is_urm or is_lim):
        rank = 1
    else:
        rank = 2

    return rank

def randomize(applicants):
    """
    Random permutation of applicant list. Typical usage is before
    prioritization.
    """
    return random.sample(applicants, k = len(applicants))

def prioritize(applicants, rank_method = asfp_rank):
    """
    Prioritize applicants by rank of attributes. Applicants are randomized
    prior to running the ranking and sorting.

    Parameters
    ----------
    applicants: list
        The list `applicants` of dicts of each applicant.
    rank_method: function
        The method of assinging ranks under label "rank" based on attributes
        that are necessarily present in items of `applicants`.

    Returns
    -------
    applicants: list
        A copy of applicants is returned, sorted by rank as determined by
        `rank_method`.
    """
    for a in applicants:
        a.update({
            "rank": rank_method(a)
        })

    return sorted(applicants, key = itemgetter("rank"))

#################################################
# EDITOR-ONLY METHODS
#################################################

def faculty_editors(editors):
    """
    Get a sublist of faculty editors.
    """
    return [e for e in editors if e["role"] == "Faculty"]

def non_faculty_editors(editors):
    """
    Get a sublist of non-faculty editors.
    """
    return [e for e in editors if e["role"] != "Faculty"]

def editors_by_categories(editors, categories):
    """
    Get a sublist of editors by categories
    """
    return [e for e in editors if e[CATEGORIES].intersection(categories)]

def editors_by_universities(editors, universities):
    """
    Get sublist of editors by universities
    """
    return [e for e in editors if e["university"].intersection(universities)]

def capacity(editors):
    """
    Compute editing capacity, the number of statements an editor
    can read, for a list of editors.
    """
    return sum(e[CAPACITY] for e in editors)

def find_highest_capacity_category(applicant, editors):
    """
    Find the highest capacity category based on editors'
    availability given stated category preferences of an applicant.

    Parameters
    ----------
    applicant: dict
        The dict object representing an applicant that has categories
        in a set.
    editors: list
        The editors list of dicts is some subset of editors.

    Returns
    -------
    Returns the highest capacity category given applicant category preferences
    as listed in the set.
    """
    
    capacities = [{
        "capacity": capacity(editors_by_categories(editors, {category})),
        "category": category
    } for category in applicant[CATEGORIES]]

    sorted_capacities = sorted(capacities, 
                               key = itemgetter(CAPACITY), 
                               reverse = True)

    return sorted_capacities[0]["category"]

def find_match(applicant, editors):
    """
    Match an applicant to editors, if possible.
    """
    if capacity(editors) > 0:
    # If at least one editor in a list is available for an applicant,
    # find the best possible match and assign.

        highest_capacity_category = find_highest_capacity_category(applicant, editors)

        highest_capacity_editors = sorted(
            editors_by_categories(editors, {highest_capacity_category}),
            key = itemgetter(CAPACITY),
            reverse = True
        )

        editor_id = highest_capacity_editors[0]["id"]

        return highest_capacity_editors[0]["id"]

    else:
    # If no editors have capacity within the group, return None
        return None

def update_capacity(editor_id, editors):
    """
    Update capacity of editor within a list by id.
    """
    for editor in editors:
        if editor["id"] == editor_id:
            editor[CAPACITY] -= 1

# TODO: handle both faculty and university editors
def remove_conflicts(applicant, potential_editors):
    """
    Remove editors from potential editors who might be sources of conflict of
    interest. These are typically by name or university.
    """
    return [editor for editor in potential_editors if
                not (editor["name"] in applicant["conflicts-faculty"] or 
                    editor["universities"] in applicant["conflicts-university"])]

def find_potential_editors(applicant, editors):
    """
    Find potential editors given applicant categories and conflicts.
    """
    category_editors = editors_by_categories(editors, applicant[CATEGORIES])
    return remove_conflicts(applicant, category_editors)

def allocate(applicants, editors):
    """
    Allocate applicants to editors.
    """
    unmatched = [applicant["id"] for applicant in applicants]
    matchings = []

    for applicant in applicants:

        potential_editors = find_potential_editors(applicant, editors)

        if capacity(potential_editors) < 2:
        # If the editing capacity for an applicant is less than 2, continue to next applicant
            continue
        else:

            _match = {
                "applicant": applicant["id"],
                "editors": []
            }

            _faculty_editors = faculty_editors(potential_editors)
            _non_faculty_editors = non_faculty_editors(potential_editors)

            faculty_editor_match = find_match(applicant, _faculty_editors)

            if (faculty_editor_match is not None) and (capacity(_non_faculty_editors) > 0):
            # If a faculty editor match is possible and at least one student editor
            # match is possible, then add a faculty editor match and update capacity.
                _match["editors"].append(faculty_editor_match)
                update_capacity(faculty_editor_match, _faculty_editors)
            else:
                if capacity(_non_faculty_editors) < 2:
                # If fewer than 2 student editors are available, skip to next
                # applicant.
                    continue
                elif applicant[FLEXIBLE]:
                # If an applicant is flexible and prefers to be matched with two
                # student editors, find first match here.
                    non_faculty_editor_match = find_match(applicant, _non_faculty_editors)
                    if non_faculty_editor_match is not None:
                        _match["editors"].append(non_faculty_editor_match)
                        update_capacity(non_faculty_editor_match, _non_faculty_editors)
                else:
                # If applicant prefers not to have a match if at least one faculty
                # editor is not available, then continue to next applicant.
                    continue

            # Add a second editor: A student editor match. Then update
            # capacity of that editor.
            non_faculty_editor_match = find_match(applicant, [e for e in _non_faculty_editors if e["id"] not in _match["editors"]])
            _match["editors"].append(non_faculty_editor_match)
            update_capacity(non_faculty_editor_match, _non_faculty_editors)

            #if ('Clinical Psychology' not in applicant[CATEGORIES]):
                # Add a third editor: A student editor match. Then update
                # capacity of that editor.

            #    non_faculty_editor_match = find_match(applicant, [e for e in _non_faculty_editors if e["id"] not in _match["editors"]])
            #    _match["editors"].append(non_faculty_editor_match)
            #    update_capacity(non_faculty_editor_match, _non_faculty_editors)

            # Append the match to matchings and remove this applicant
            # from the list of unmatched applicants.
            matchings.append(_match)
            unmatched.remove(applicant["id"])

    if capacity(editors) > 0:
    # After assigning 2-pieces-of-feedback-per-applicant, check for extra
    # capacity by editors, then try to allocate to highest priority applicants again

        matched_applicants_ids = [a['applicant'] for a in matchings]
        matched_applicants = [a for a in applicants if a['id'] in matched_applicants_ids]

        available_editors = [e for e in editors if e['capacity'] > 0]

        for applicant in matched_applicants:

            curr_match = [a for a in matchings if a['applicant'] == applicant['id']][0]
            curr_editors = curr_match['editors']
            potential_editors = find_potential_editors(applicant, available_editors)
            if capacity(potential_editors) > 0:
                extra_editors = non_faculty_editors(potential_editors)
                extra_match = find_match(
                    applicant,
                    [e for e in extra_editors if e["id"] not in curr_match["editors"]]
                )
                if (extra_match is not None):
                    curr_match['editors'].append(extra_match)
                    update_capacity(extra_match, extra_editors)
                else:
                    continue

    return {
        "matchings": matchings,
        "unmatched": unmatched,
        "editors": editors,
    }


def format_matchings(matchings, applicants, editors):
    """
    Create dyadic format matchings, returning list of dicts with
    pairings of editors and applicants, including categories and
    statements with notes from applicants.

    NOTE: The applicants and editors list args expect the original lists with
        detailed information, not just the output of allocate.
    """
    dyads = []
    for matching in matchings:
        # Get applicant id from match and then get applicant details
        # from applicants list
        applicant_id = matching["applicant"]
        applicant = get_element_by_id(applicant_id, applicants)

        # Get editor ids and then get both detailed editor elements from list
        editor_ids = matching["editors"]
        for editor_id in editor_ids:
            editor = get_element_by_id(editor_id, editors)

            dyads.append({
                "editor_id": editor["id"],
                "editor_email": editor["email"],
                "editor_first_name": editor["first"],
                "editor_last_name": editor["last"],
                "editor_categories": ", ".join(str(c) for c in editor[CATEGORIES]),
                "applicant_id": applicant["id"],
                "applicant_first_name": applicant["first"],
                "applicant_last_name": applicant["last"],
                "applicant_email": applicant["email"],
                "applicant_statement": applicant["statement"],
                "applicant_notes": applicant["notes"],
                "applicant_categories": ", ".join(str(c) for c in applicant[CATEGORIES]),
            })
            
    return dyads
    
def compile_unmatched(unmatched, applicants):
    """
    Compile list of unmatched applicants after allocation, using the
      output unmatched IDs from allocate.
    """
    return [a for a in applicants if a["id"] in unmatched]

def format_unmatched(unmatched_applicants):
    """
    Format unmatched for CSV save. Use result from compile unmatched.
    """
    formatted = []
    for a in unmatched_applicants:
        formatted.append({
            "applicant_id": a["id"],
            "applicant_email": a["email"],
            "applicant_categories": ', '.join(str(c) for c in a[CATEGORIES]),
            "applicant_rank": a["rank"]
        })
    return formatted

def format_applicant_id_manifest(applicants):
    """
    Format list of identified applicants and return sorted list by
      the identifier.
    """
    manifest = []
    for a in applicants:
        manifest.append({
            "applicant_id": a["id"],
            "applicant_first_name": a["first"],
            "applicant_last_name": a["last"],
            "applicant_email": a["email"],
            "applicant_categories": ", ".join(c for c in a[CATEGORIES]),
            "applicant_rank": a["rank"]
        })
    return sorted(manifest, key = itemgetter("applicant_id"))
