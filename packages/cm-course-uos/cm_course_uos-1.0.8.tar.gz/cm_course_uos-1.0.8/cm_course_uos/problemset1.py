import io
import random
import numpy as np   
import matplotlib.pyplot as plt
import pandas as pd

from matplotlib.ticker import MaxNLocator


def hello():
    print("Package is available!")

# PLOT DECK CHOICES


# load data
data = pd.read_csv(io.BytesIO(uploaded['experiment_data.csv']))

def plot_deck_choices(data, block_size = 10):
    # some analysis parameters
    num_blocks = len(data.index) // block_size

    # Create a new column 'block' by dividing 'trial_index' by 25 and rounding up to create blocks
    data['block'] = (data['trial_index']) // block_size + 1

    # Group the DataFrame by 'block' and 'risky_deck', and calculate the proportions
    block_proportions = data.groupby(['block', 'type'])['type'].count() / block_size

    # Convert the Series to a DataFrame and drop the 'risky_deck' column
    proportion_safe = list()

    # compute proportion safe choices per block
    for i in range(num_blocks):
      condition = (data['block'] == i + 1) & (data['type'] == 'safe')
      proportion_safe.append(condition.sum())

    # arrange data
    proportion_safe = np.array(proportion_safe)/block_size
    proportion_risky = 1 - proportion_safe
    blocks = np.arange(1, num_blocks+1)

    # Create a line plot
    plt.figure(figsize=(10, 6))
    plt.plot(blocks, proportion_safe, label='Proportion Safe Choices')
    plt.plot(blocks, proportion_risky, label='Proportion Risky Choices')

    # Customize the plot
    plt.xlabel('Block')
    plt.ylabel('Proportion')
    plt.title('Proportion of Risky vs. Safe Choices per Block')
    plt.legend()

    ax = plt.gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    
    
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


def test_valence(student_valence):
    """ Returns True if The student implemented valence function returns same values 
    as the correct solution."""
    # Defining a parameter space for deck_results and w to test
    for deck_result in range(-25,5,1):
        for w in range(10):
            w = w/10 # scaling w to [0,1] 
            
            if student_valence(deck_result, w) != compute_valence(deck_result,w):
                return False #break loops, return false
    return True      