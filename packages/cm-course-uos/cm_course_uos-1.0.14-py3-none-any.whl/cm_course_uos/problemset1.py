"""
authors: Sebastian Musslick (smusslick@uos.de),
         Deniz M. Gun (dguen@uos.de)

This module contains helper and test functions for Problemset 1
 of the course "Cognitive Modeling" at the University of Osnabrueck.
 This module exists in order to load certain functionality into the 
 assignment notebooks without involuntarily giving students access to
 solutions.
"""
import numpy as np


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
    valence = w * win + (1-w) * loss  # YOUR ANSWER GOES HERE

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


def compute_expectancy(previous_expectancy, alpha, valence):
  '''
  This function computes the expectancy as denoted above.

  Input arguments:
    previous_expectancy: expectancy of current deck on previous trial
    alpha: update parameter
    valence: valence of current deck on current trial
  '''

  # compute expectancy term
  new_expectancy = (1-alpha) * previous_expectancy + alpha * valence # YOUR ANSWER GOES HERE
  return new_expectancy


def test_compute_expectancy(student_expectancy, print_feedback=True):
    """ Returns True if The student implemented
    expectancy function returns same values as the correct solution.

    Args
        student_expectancy (method) :
            The compute_expectancy method defined in the notebook and edited by students.
        print_feedback (bool) :
            If True, this method prints feedback to the console.
    Returns
        correct (bool):
            True, if student_valence returns the same values as compute_valence
    """

    correct = True

    for previous_expectancy in range(-10, 10, 1):
        for alpha in range(11):
            alpha = alpha / 10  # scaling to [0,1]
            for valence in range(11):
                valence = valence/10  # scaling to [0,1]
                student_result = student_expectancy(previous_expectancy, alpha, valence)
                correct_result = compute_expectancy(previous_expectancy, alpha, valence)

                if student_result != correct_result:
                    correct = False
                    break

        if not correct:
            break  # exit search

    if not print_feedback:
        return correct

    if correct:
        print("Your compute_expectancy function creates correct outputs!")
    else:
        print(
            "Your compute_expectancy function generates incorrect outputs. Check for mistakes.")
    return correct


def compute_choice_probabilities(expectancies, trial_number, c):
  '''
  This function computes the choice probabilities for each deck based on the
  current expectancies

  Input arguments:
    expectancies: a list of expectancies for all four decks
    trial_number: number of the current trial
    c: parameter used to compute beta
  '''
  # compute beta
  beta = pow((trial_number+1)/10, c)

  # compute softmaxed choice proabbilities
  choice_probs = np.exp(expectancies * beta) / np.sum(np.exp(expectancies * beta)) # YOUR ANSWER GOES HERE

  return choice_probs


def test_compute_choice_probs(student_choice_probabilities, print_feedback=True):
    """ Returns True if The student implemented
    choice probability function returns same values as the correct solution.

    Args
        student_choice_probabilities (method) :
            The compute_choice_probabilities method defined in the notebook and edited by students.
        print_feedback (bool) :
            If True, this method prints feedback to the console.
    Returns
        correct (bool):
            True, if student_valence returns the same values as compute_valence
    """

    correct = True

    for expectancy_idx in range(11):
        for trial_number in range(11):
            for c in np.linspace(-2, 2, 11):

                expectancies = np.array([np.random.randint(-5, 5),
                                        np.random.randint(-5, 5),
                                        np.random.randint(-5, 5),
                                         np.random.randint(-5, 5)])
                student_result = student_choice_probabilities(expectancies, trial_number, c)
                correct_result = compute_choice_probabilities(expectancies, trial_number, c)

                for choice in range(len(student_result)):
                    if np.round(student_result[choice], decimals=8) != np.round(correct_result[choice], decimals=8):
                        correct = False
                        break

        if not correct:
            break  # exit search

    if not print_feedback:
        return correct

    if correct:
        print("Your compute_expectancy function creates correct outputs!")
    else:
        print(
            "Your compute_expectancy function generates incorrect outputs. Check for mistakes.")
    return correct