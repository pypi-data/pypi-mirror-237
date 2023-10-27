
def hello():
    print("Package is available!")

    
def compute_valence(deck_result, W):
  '''
  This function computes the valence as denoted above.

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
  valence = W * win + (1-W) * loss # YOUR ANSWER GOES HERE (win + loss)

  return valence


def test_compute_valence(student_valence):
    """ Returns True if The student implemented valence function returns same values 
    as the correct solution."""
    # Defining a parameter space for deck_results and w to test
    for deck_result in range(-25,5,1):
        for w in range(10):
            w = w/10 # scaling w to [0,1] 
            
            if student_valence(deck_result, w) != compute_valence(deck_result,w):
                return False #break loops, return false
    return True      