"""
authors: Sebastian Musslick (smusslick@uos.de),
         Deniz M. Gun (dguen@uos.de)

This module contains helper and test functions for Problemset 1
 of the course "Cognitive Modeling" at the University of Osnabrueck.
 This module exists in order to load certain functionality into the 
 assignment notebooks without involuntarily giving students access to
 solutions.
"""


def compute_valence(deck_result, w):
    '''
    This function computes the valence as denoted in the notebook script.

    Input arguments:
      deck_result: The result of the selected deck (in points)
      W: The valence parameter
    '''

    # first compute win and loss depending on points received
    if deck_result > 0:
        win = deck_result
        loss = 0
    else:
        win = 0
        loss = deck_result

    # compute valence term
    valence = w * win + (1-w) * loss  # YOUR ANSWER GOES HERE (win + loss)

    return valence


def test_compute_valence(student_valence, print_feedback=True):
    """ Returns True if The student implemented 
    valence function returns same values as the correct solution.

    Args
        student_valence (method) :  
            The compute_valence method defined in the notebook and edited by students.
        print_feedback (bool) : 
            If True, this method prints feedback to the console.
    Returns
        correct (bool): 
            True, if student_valence returns the same values as compute_valence
    """

    correct = True

    # Search for all reck rewards between -25 and 10
    for deck_result in range(-25, 10, 1):
        for w in range(11):
            w = w/10  # scaling w to [0,1]
            student_result = student_valence(deck_result, w)
            correct_result = compute_valence(deck_result, w)

            if student_result != correct_result:
                correct = False
                break

        if not correct:
            break  # exit search

    if not print_feedback:
        return correct

    if correct:
        print("Your compute_valence function creates correct outputs!")
    else:
        print(
            "Your compute_valence function generates incorrect outputs. Check for mistakes.")
    return correct
