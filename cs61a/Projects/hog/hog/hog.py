"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

# Taking turns

def roll_dice(num_rolls, dice=six_sided):
    """Roll DICE for NUM_ROLLS times.  Return either the sum of the outcomes,
    or 1 if a 1 is rolled (Pig out). This calls DICE exactly NUM_ROLLS times.

    num_rolls:  The number of dice rolls that will be made; at least 1.
    dice:       A zero-argument function that returns an integer outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    "*** YOUR CODE HERE ***"
    k, total = 0, 0
    one = False
    while (k < num_rolls): 
        num = dice()
        if (num == 1):
            one = True
        total, k = num + total, k+1
    if (one):
        return 1
    else:
        return total


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.

    #returns the number of points 
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    "*** YOUR CODE HERE ***"
    if (num_rolls == 0):
        return getBaconScore(opponent_score)
    else:
        return roll_dice(num_rolls, dice)


#returns the number of points for rolling 0
def getBaconScore(opponent_score):
    def getMaxDigit(num):
        digits = str(num)
        l = list(digits)
        high = int(max(l))
        return high
    return getMaxDigit(opponent_score) + 1

# Playing a game

def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).

    >>> select_dice(4, 24) == four_sided
    True
    >>> select_dice(16, 64) == six_sided
    True
    >>> select_dice(0, 0) == four_sided
    True
    """
    "*** YOUR CODE HERE ***"
    if (score + opponent_score) % 7 == 0:
        return four_sided
    return six_sided

def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

PLAY1_WIN_COUNT = 0
PLAY0_WIN_COUNT = 0

def play(strategy0, strategy1, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    """
    def getScore(who):
        if who == 0:
            return score
        return opponent_score

    def whichDice(dice):
        if dice == six_sided:
            return "six-sided"
        return "four-sided"

    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    score, opponent_score = 0, 0
    numDice, selectDice = 0, 0
    "*** YOUR CODE HERE ***"
    while (score < goal and opponent_score < goal):
        #take turn
        if who == 0:
            numDice = strategy0(score, opponent_score)
            selectDice = select_dice(score, opponent_score)
            score += take_turn(numDice, opponent_score, selectDice)
        else:
            numDice = strategy1(opponent_score, score)
            selectDice = select_dice(opponent_score, score)
            opponent_score += take_turn(numDice, score, selectDice)
        
        #print("Player {} is rolling {} {} dice.  New score: {}".format(who, 
         #   numDice, whichDice(selectDice), getScore(who)))

        #swine swap
        if (causes_swine_swap(score, opponent_score)):
            score, opponent_score = opponent_score, score

        #switch players
        who = other(who)

    who = other(who)
    inc_win_count(who)
    #print("Player {} wins!  Final score {} to {}.  Win Count: {} to {}"
    #    .format(who, score, opponent_score, PLAY0_WIN_COUNT, PLAY1_WIN_COUNT))

    return score, opponent_score  # You may wish to change this line.

def inc_win_count(who):
    if (who == 0):
        global PLAY0_WIN_COUNT
        PLAY0_WIN_COUNT += 1
    else:
        global PLAY1_WIN_COUNT
        PLAY1_WIN_COUNT += 1

def causes_swine_swap(score1, score2):
    if (score1 * 2 == score2 or score2 * 2 == score1):
        return True
    return False

#######################
# Phase 2: Strategies #
#######################

# Basic Strategy

BASELINE_NUM_ROLLS = 5
BACON_MARGIN = 8

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy

# Experiments

def make_averaged(fn, num_samples=4000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    6.0

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 1.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 6.0.
    """
    "*** YOUR CODE HERE ***"
    def get_avg(*args):
        k, result = 0, 0
        while (k < num_samples):
            result, k = result + fn(*args), k + 1
        #print("Result {} and average of {} runs: {}".format(result, num_samples, result / num_samples))
        return result / num_samples
    return get_avg
    #

def max_scoring_num_rolls(dice=six_sided):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE.  Print all averages as in
    the doctest below.  Assume that dice always returns positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    1 dice scores 3.0 on average
    2 dice scores 6.0 on average
    3 dice scores 9.0 on average
    4 dice scores 12.0 on average
    5 dice scores 15.0 on average
    6 dice scores 18.0 on average
    7 dice scores 21.0 on average
    8 dice scores 24.0 on average
    9 dice scores 27.0 on average
    10 dice scores 30.0 on average
    10
    """
    "*** YOUR CODE HERE ***"
    k, avg, high, num_die = 1, 0, 0, 0
    while (k <= 10):
        avg  = make_averaged(roll_dice, 100000)(k, dice) 
        print("{} dice scores {} on average".format(k, avg))
        if (high < avg):
            high = avg
            num_die = k
        k = k + 1
    return num_die



def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1

#this calculates the win percentage against the baseline strategy
# first playing with the strategy as player 0
# then playing with the strategy as player 1
def average_win_rate(strategy, baseline=always_roll(BASELINE_NUM_ROLLS)):
    """Return the average win rate (0 to 1) of STRATEGY against BASELINE."""
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)
    print("win rate as player 0: {}".format(win_rate_as_player_0))
    print("win rate as player 1: {}".format(win_rate_as_player_1))
    return (win_rate_as_player_0 + win_rate_as_player_1) / 2 # Average results

def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False: # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False: # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(6)))

    if False: # Change to False to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False: # Change to False to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    if False:
        compute_probabilities(7, six_sided)
        compute_probabilities(8, four_sided)

    if True: # Change to False to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"

# Strategies

def bacon_strategy(score, opponent_score):
    """This strategy rolls 0 dice if that gives at least BACON_MARGIN points,
    and rolls BASELINE_NUM_ROLLS otherwise.

    BASELINE_NUM_ROLLS = 5
    BACON_MARGIN = 8

    >>> bacon_strategy(0, 0)
    5
    >>> bacon_strategy(70, 50)
    5
    >>> bacon_strategy(50, 70)
    0
    """
    "*** YOUR CODE HERE ***"
    if (getBaconScore(opponent_score) >= BACON_MARGIN):
        return 0
    else:
        return BASELINE_NUM_ROLLS

def swap_strategy(score, opponent_score):
    """This strategy rolls 0 dice when it would result in a beneficial swap and
    rolls BASELINE_NUM_ROLLS if it would result in a harmful swap. It also rolls
    0 dice if that gives at least BACON_MARGIN points and rolls
    BASELINE_NUM_ROLLS otherwise.

    >>> swap_strategy(23, 60) # 23 + (1 + max(6, 0)) = 30: Beneficial swap
    0
    >>> swap_strategy(27, 18) # 27 + (1 + max(1, 8)) = 36: Harmful swap
    5
    >>> swap_strategy(50, 80) # (1 + max(8, 0)) = 9: Lots of free bacon
    0
    >>> swap_strategy(12, 12) # Baseline
    5
    """
    "*** YOUR CODE HERE ***"
    def is_beneficial_swap(score, opponent_score):
        if (opponent_score > score):
            return True
        else:
            return False
    score_with_zero = score + getBaconScore(opponent_score)

    #If no swine swap, follow bacon_strategy
    if (not causes_swine_swap(score_with_zero, opponent_score)):
        return bacon_strategy(score, opponent_score)

    #Otherwise roll 0 on beneficial swap, roll BASELINE otherwise
    elif (is_beneficial_swap(score_with_zero, opponent_score)):
        return 0
    else:
        return BASELINE_NUM_ROLLS

#### ADVANCED STRATEGY

def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    There are four buckets of potential moves:
        1) If behind and your score and opponent score < 50
            - you're not too far behind, go for the statistical max
        2) If behind and opponent score > 50 
            - if a score swap is within realm of possibility (i.e. > threshold),
            attempt the score swap
            - if not, then keep going for statistical max
                (alternatively, could try to wait it out and keep going for score swap)
        3) If ahead and your score and opponent score < 50
            - you're not too far ahead, go for the statistical max
        4) If ahead and your score > 50
            - keep charging ahead, go for statistical max
                (alternatively, could try to minimize chance of score_swap)

    """

    "*** YOUR CODE HERE ***"
    def am_behind(score, opponent_score):
        return opponent_score > score

    def by_a_lot(score, opponent_score, threshold):
        return opponent_score - score > threshold

    def close_enough_to_swap(score, opponent_score, threshold):
        if (abs(score - opponent_score)/score > threshold or
            abs(score - opponent_score)/opponent_score > threshold):
            return True
        else:
            return False

    def be_risky(score, opponent_score, dice):
        if close_enough_to_swap(score, opponent_score, .9):
            #what do i need
            ineed = score * 2 - opponent_score
            if dice == six_sided:
                if ineed == 1:
                    return 10
                if ineed >= 2 and ineed <= 6:
                    return 1
                else:
                    return be_safe(score, opponent_score)
            else:
                if ineed == 1:
                    return 10
                elif ineed >= 2 and ineed <= 4:
                    return 10  #25% chance, everything else too risky
                else:
                    return be_safe(score, opponent_score)
        else:
            return be_safe(score, opponent_score)

    def be_safe(score, opponent_score):
        return get_statistical_max(score,opponent_score)

    dice = select_dice(score, opponent_score)

    if am_behind(score, opponent_score):
        if by_a_lot(score, opponent_score, 30):
            return be_risky(score, opponent_score, dice)
        else:
            return be_safe(score, opponent_score)
    else:   #i'm ahead
        if by_a_lot(opponent_score, score, 30):
            return be_safe(score, opponent_score)
        else:
            return be_safe(score, opponent_score)

### EXPECTED VALUES
def get_expected_value(opponent_score, dice=six_sided):
    """ based on 100k rolls """
    six_list = [getBaconScore(opponent_score),3.50332,5.86032,7.36786, 8.25786,8.59203,8.74338,8.50806,8.17981,7.78308, 7.33582]
    four_list = [getBaconScore(opponent_score),2.50498,3.80794,4.37158,4.49637,4.3196,4.02963,3.67541,3.33545,2.9528,2.64403]

    if (dice == six_sided):
        return six_list
    else: 
        return four_list

def get_statistical_max(score, opponent_score):
    """ This function returns the statistical max score based on a few factors:
    1)  Calculates what expected value of a dice roll would be based on 
        the hypothetical roll (with a six-sided die or a four-sided die)
        a)  Compares this with rolling a zero-argument
    2)  Adjusts the statistical max based on whether it would cause a score_swap
        a)  If it does cause a score swap (beneficial), then attempt it
        b)  If it causes a harmfuls core swap, avoid it
        c)  Otherwise just keep the best roll as is
    """

    def adjust_expected_values_based_on_scores(score, opponent_score, eplist):
        """
        eplist is list of expected values
        """
        #adjust based on swine swap 
        def adjust_swine_swap(score, opponent_score, eplist):
            score_with_zero = score + getBaconScore(opponent_score)
            score_with_one = score + 1  #chances of rolling a 1 with 10 dice is 83%
            
            #if 0 causes swine swap, calculate benefit and put in eplist

            if (causes_swine_swap(score_with_zero, opponent_score)):
                eplist[0] = max(eplist[0], opponent_score - score_with_zero) 

            if (causes_swine_swap(score_with_one, opponent_score)):
                eplist[10] = max(eplist[10], 
                    (opponent_score - score_with_one) * percent_one)

            return eplist
            
        #adjust based on trying to force a four dice
        def adjust_try_four(score, opponent_score, eplist):
            score_with_zero = score + getBaconScore(opponent_score)
            score_with_one = score + 1

            #if we can cause opponent to have to roll a four_sided dice, calc the benefit
            if ((score_with_zero + opponent_score) % 7 == 0):
                eplist[0] = max(eplist[0], eplist[0] + 4)

            if ((score_with_one + opponent_score) % 7 == 0):
                eplist[10] = max(eplist[10], (eplist[10] + 4) * percent_one)

            return eplist

        eplist = adjust_swine_swap(score, opponent_score, eplist)
        eplist = adjust_try_four(score, opponent_score, eplist)
        return eplist

    dice = select_dice(score, opponent_score)

    if (dice == six_sided):
        percent_one = .833 #chance of rolling a "1" with rolling 10 six-sided dice
    else:
        percent_one = .944 #chance of rolling a "1" when rolling 10 four-sided dice

    eplist = get_expected_value(opponent_score, dice)

    adjusted = adjust_expected_values_based_on_scores(
        score, opponent_score, eplist)

    num_dice = adjusted.index(max(adjusted))
    
    return num_dice

##########################
# Command Line Interface #
##########################

# Note: Functions in this section do not need to be changed.  They use features
#       of Python not yet covered in the course.

def get_int(prompt, min):
    """Return an integer greater than or equal to MIN, given by the user."""
    choice = input(prompt)
    while not choice.isnumeric() or int(choice) < min:
        print('Please enter an integer greater than or equal to', min)
        choice = input(prompt)
    return int(choice)

def interactive_dice():
    """A dice where the outcomes are provided by the user."""
    return get_int('Result of dice roll: ', 1)

def make_interactive_strategy(player):
    """Return a strategy for which the user provides the number of rolls."""
    prompt = 'Number of rolls for Player {0}: '.format(player)
    def interactive_strategy(score, opp_score):
        if player == 1:
            score, opp_score = opp_score, score
        print(score, 'vs.', opp_score)
        choice = get_int(prompt, 0)
        return choice
    return interactive_strategy

def roll_dice_interactive():
    """Interactively call roll_dice."""
    num_rolls = get_int('Number of rolls: ', 1)
    turn_total = roll_dice(num_rolls, interactive_dice)
    print('Turn total:', turn_total)

def take_turn_interactive():
    """Interactively call take_turn."""
    num_rolls = get_int('Number of rolls: ', 0)
    opp_score = get_int('Opponent score: ', 0)
    turn_total = take_turn(num_rolls, opp_score, interactive_dice)
    print('Turn total:', turn_total)

def play_interactive():
    """Interactively call play."""
    strategy0 = make_interactive_strategy(0)
    strategy1 = make_interactive_strategy(1)
    score0, score1 = play(strategy0, strategy1)
    print('Final scores:', score0, 'to', score1)

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--interactive', '-i', type=str,
                        help='Run interactive tests for the specified question')
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')
    args = parser.parse_args()

    if args.interactive:
        test = args.interactive + '_interactive'
        if test not in globals():
            print('To use the -i option, please choose one of these:')
            print('\troll_dice', '\ttake_turn', '\tplay', sep='\n')
            exit(1)
        try:
            globals()[test]()
        except (KeyboardInterrupt, EOFError):
            print('\nQuitting interactive test')
            exit(0)
    elif args.run_experiments:
        run_experiments()

#################################################################
#POSSIBILITY possibility_matrix
#################################################################

# this function tries to roll a ____, based on the best way to do it
def compute_probabilities(num_rolls, dice=six_sided):
    #compute possibilities
    k = 1
    global possibilities
    def f(dice, k):
        if (dice == six_sided):
            return pow(6,k)
        return pow(4,k)

    while (k <= num_rolls):
        print("Rolling {} dice possibilities.".format(k))
        possibilities = list()
        get_possibilities("", k, dice)
        convert_possibilities_to_matrix(possibilities, f(dice, k))
        k += 1
    
possibilities = list()
def get_possibilities(total, num_rolls, dice):
    i = 1
    global possibilities
    if (num_rolls == 0):
        return total

    if (dice == six_sided):
        sides = 6
    else:
        sides = 4
    while (i <= sides):
        mystr = get_possibilities(str(total) + str(i), num_rolls-1, dice)
        if (not mystr == None):
            possibilities.append(mystr)
        i += 1

import json 
def convert_possibilities_to_matrix(possibilities, max_possibilities):
    def get_total(roll):
        l = list(roll)
        total = 0
        for i in l:
            if (int(i) == 1):
                return 1
            total += int(i)
        return total

    def convert_possibility_to_probability(possibility_matrix, max_possibilities):
        for k in possibility_matrix.keys():
            possibility_matrix[k] = possibility_matrix[k] / max_possibilities
        return possibility_matrix

    possibility_matrix = {}
    for item in possibilities:
        total = get_total(item)
        if total in possibility_matrix:
            possibility_matrix[total] += 1
        else:
            possibility_matrix[total] = 1

    #print(json.dumps(possibility_matrix, indent=4))

    possibility_matrix = convert_possibility_to_probability(possibility_matrix, max_possibilities)
    print(json.dumps(possibility_matrix, indent=4))

""" - BASICALLY, rolling anything but 1 is really hard to do

****    SIX SIDED DICE  ****

Rolling 1 dice possibilities.
{
    "1": 0.16666666666666666, 
    "2": 0.16666666666666666, 
    "3": 0.16666666666666666, 
    "4": 0.16666666666666666, 
    "5": 0.16666666666666666, 
    "6": 0.16666666666666666
}
Rolling 2 dice possibilities.
{
    "1": 0.3055555555555556, 
    "4": 0.027777777777777776, 
    "5": 0.05555555555555555, 
    "6": 0.08333333333333333, 
    "7": 0.1111111111111111, 
    "8": 0.1388888888888889, 
    "9": 0.1111111111111111, 
    "10": 0.08333333333333333, 
    "11": 0.05555555555555555, 
    "12": 0.027777777777777776
}
Rolling 3 dice possibilities.
{
    "1": 0.4212962962962963, 
    "6": 0.004629629629629629, 
    "7": 0.013888888888888888, 
    "8": 0.027777777777777776, 
    "9": 0.046296296296296294, 
    "10": 0.06944444444444445, 
    "11": 0.08333333333333333, 
    "12": 0.08796296296296297, 
    "13": 0.08333333333333333, 
    "14": 0.06944444444444445, 
    "15": 0.046296296296296294, 
    "16": 0.027777777777777776, 
    "17": 0.013888888888888888, 
    "18": 0.004629629629629629
}
Rolling 4 dice possibilities.
{
    "1": 0.5177469135802469, 
    "8": 0.0007716049382716049, 
    "9": 0.0030864197530864196, 
    "10": 0.007716049382716049, 
    "11": 0.015432098765432098, 
    "12": 0.02700617283950617, 
    "13": 0.040123456790123455, 
    "14": 0.05246913580246913, 
    "15": 0.06172839506172839, 
    "16": 0.06558641975308642, 
    "17": 0.06172839506172839, 
    "18": 0.05246913580246913, 
    "19": 0.040123456790123455, 
    "20": 0.02700617283950617, 
    "21": 0.015432098765432098, 
    "22": 0.007716049382716049, 
    "23": 0.0030864197530864196, 
    "24": 0.0007716049382716049
}
Rolling 5 dice possibilities.
{
    "1": 0.5981224279835391, 
    "10": 0.0001286008230452675, 
    "11": 0.0006430041152263374, 
    "12": 0.0019290123456790122, 
    "13": 0.0045010288065843625, 
    "14": 0.009002057613168725, 
    "15": 0.015560699588477367, 
    "16": 0.023791152263374485, 
    "17": 0.03279320987654321, 
    "18": 0.0411522633744856, 
    "19": 0.04693930041152263, 
    "20": 0.048996913580246916, 
    "21": 0.04693930041152263, 
    "22": 0.0411522633744856, 
    "23": 0.03279320987654321, 
    "24": 0.023791152263374485, 
    "25": 0.015560699588477367, 
    "26": 0.009002057613168725, 
    "27": 0.0045010288065843625, 
    "28": 0.0019290123456790122, 
    "29": 0.0006430041152263374, 
    "30": 0.0001286008230452675
}
Rolling 6 dice possibilities.
{
    "1": 0.6651020233196159, 
    "12": 2.143347050754458e-05, 
    "13": 0.0001286008230452675, 
    "14": 0.0004501028806584362, 
    "15": 0.0012002743484224967, 
    "16": 0.002700617283950617, 
    "17": 0.005272633744855967, 
    "18": 0.009130658436213992, 
    "19": 0.01427469135802469, 
    "20": 0.020383230452674896, 
    "21": 0.02670610425240055, 
    "22": 0.03227880658436214, 
    "23": 0.03613683127572016, 
    "24": 0.037530006858710566, 
    "25": 0.03613683127572016, 
    "26": 0.03227880658436214, 
    "27": 0.02670610425240055, 
    "28": 0.020383230452674896, 
    "29": 0.01427469135802469, 
    "30": 0.009130658436213992, 
    "31": 0.005272633744855967, 
    "32": 0.002700617283950617, 
    "33": 0.0012002743484224967, 
    "34": 0.0004501028806584362, 
    "35": 0.0001286008230452675, 
    "36": 2.143347050754458e-05
}

Rolling 7 dice possibilities.
{
    "1": 0.7209183527663466, 
    "14": 3.5722450845907635e-06, 
    "15": 2.5005715592135344e-05, 
    "16": 0.00010002286236854138, 
    "17": 0.00030006858710562417, 
    "18": 0.0007501714677640603, 
    "19": 0.0016253715134887975, 
    "20": 0.003125714449016918, 
    "21": 0.005429812528577961, 
    "22": 0.008626971879286694, 
    "23": 0.01262788637402835, 
    "24": 0.01712891518061271, 
    "25": 0.021629943987197073, 
    "26": 0.025505829903978053, 
    "27": 0.028131430041152265, 
    "28": 0.02906021376314586, 
    "29": 0.028131430041152265, 
    "30": 0.025505829903978053, 
    "31": 0.021629943987197073, 
    "32": 0.01712891518061271, 
    "33": 0.01262788637402835, 
    "34": 0.008626971879286694, 
    "35": 0.005429812528577961, 
    "36": 0.003125714449016918, 
    "37": 0.0016253715134887975, 
    "38": 0.0007501714677640603, 
    "39": 0.00030006858710562417, 
    "40": 0.00010002286236854138, 
    "41": 2.5005715592135344e-05, 
    "42": 3.5722450845907635e-06
}
Rolling 8 dice possibilities.
{
    "1": 0.7674319606386222, 
    "16": 5.953741807651273e-07, 
    "17": 4.762993446121018e-06, 
    "18": 2.143347050754458e-05, 
    "19": 7.144490169181528e-05, 
    "20": 0.000196473479652492, 
    "21": 0.0004667733577198598, 
    "22": 0.0009835581466239903, 
    "23": 0.0018718564243255602, 
    "24": 0.003259673639689072, 
    "25": 0.00523929279073312, 
    "26": 0.007823216735253772, 
    "27": 0.010907254991617132, 
    "28": 0.014253257887517147, 
    "29": 0.017504000914494743, 
    "30": 0.020242722146014327, 
    "31": 0.02207647462277092, 
    "32": 0.02272245560890108, 
    "33": 0.02207647462277092, 
    "34": 0.020242722146014327, 
    "35": 0.017504000914494743, 
    "36": 0.014253257887517147, 
    "37": 0.010907254991617132, 
    "38": 0.007823216735253772, 
    "39": 0.00523929279073312, 
    "40": 0.003259673639689072, 
    "41": 0.0018718564243255602, 
    "42": 0.0009835581466239903, 
    "43": 0.0004667733577198598, 
    "44": 0.000196473479652492, 
    "45": 7.144490169181528e-05, 
    "46": 2.143347050754458e-05, 
    "47": 4.762993446121018e-06, 
    "48": 5.953741807651273e-07
}
Rolling 9 dice possibilities.
{
    "1": 0.8061933005321852, 
    "18": 9.92290301275212e-08, 
    "19": 8.930612711476909e-07, 
    "20": 4.465306355738455e-06, 
    "21": 1.6372789971041e-05, 
    "22": 4.9118369913123e-05, 
    "23": 0.0001268147005029721, 
    "24": 0.000289947226032617, 
    "25": 0.0005983510516689529, 
    "26": 0.001129722508001829, 
    "27": 0.0019701923931819336, 
    "28": 0.0031962662894375856, 
    "29": 0.004850215763603109, 
    "30": 0.006913782674135041, 
    "31": 0.009287837219935985, 
    "32": 0.01178840877914952, 
    "33": 0.014163951760402377, 
    "34": 0.016133151863283037, 
    "35": 0.017437021319158665, 
    "36": 0.017893474857745263, 
    "37": 0.017437021319158665, 
    "38": 0.016133151863283037, 
    "39": 0.014163951760402377, 
    "40": 0.01178840877914952, 
    "41": 0.009287837219935985, 
    "42": 0.006913782674135041, 
    "43": 0.004850215763603109, 
    "44": 0.0031962662894375856, 
    "45": 0.0019701923931819336, 
    "46": 0.001129722508001829, 
    "47": 0.0005983510516689529, 
    "48": 0.000289947226032617, 
    "49": 0.0001268147005029721, 
    "50": 4.9118369913123e-05, 
    "51": 1.6372789971041e-05, 
    "52": 4.465306355738455e-06, 
    "53": 8.930612711476909e-07, 
    "54": 9.92290301275212e-08
}
    10 times out lol

***** FOUR SIDED DICE   ***********

Rolling 1 dice possibilities.
{
    "1": 0.25, 
    "2": 0.25, 
    "3": 0.25, 
    "4": 0.25
}
Rolling 2 dice possibilities.
{
    "1": 0.4375, 
    "4": 0.0625, 
    "5": 0.125, 
    "6": 0.1875, 
    "7": 0.125, 
    "8": 0.0625
}
Rolling 3 dice possibilities.
{
    "1": 0.578125, 
    "6": 0.015625, 
    "7": 0.046875, 
    "8": 0.09375, 
    "9": 0.109375, 
    "10": 0.09375, 
    "11": 0.046875, 
    "12": 0.015625
}
Rolling 4 dice possibilities.
{
    "1": 0.68359375, 
    "8": 0.00390625, 
    "9": 0.015625, 
    "10": 0.0390625, 
    "11": 0.0625, 
    "12": 0.07421875, 
    "13": 0.0625, 
    "14": 0.0390625, 
    "15": 0.015625, 
    "16": 0.00390625
}
Rolling 5 dice possibilities.
{
    "1": 0.7626953125, 
    "10": 0.0009765625, 
    "11": 0.0048828125, 
    "12": 0.0146484375, 
    "13": 0.029296875, 
    "14": 0.0439453125, 
    "15": 0.0498046875, 
    "16": 0.0439453125, 
    "17": 0.029296875, 
    "18": 0.0146484375, 
    "19": 0.0048828125, 
    "20": 0.0009765625
}
Rolling 6 dice possibilities.
{
    "1": 0.822021484375, 
    "12": 0.000244140625, 
    "13": 0.00146484375, 
    "14": 0.005126953125, 
    "15": 0.01220703125, 
    "16": 0.02197265625, 
    "17": 0.03076171875, 
    "18": 0.034423828125, 
    "19": 0.03076171875, 
    "20": 0.02197265625, 
    "21": 0.01220703125, 
    "22": 0.005126953125, 
    "23": 0.00146484375, 
    "24": 0.000244140625
}
Rolling 7 dice possibilities.
{
    "1": 0.86651611328125, 
    "14": 6.103515625e-05, 
    "15": 0.00042724609375, 
    "16": 0.001708984375, 
    "17": 0.00469970703125, 
    "18": 0.00982666015625, 
    "19": 0.0162353515625, 
    "20": 0.02178955078125, 
    "21": 0.02398681640625, 
    "22": 0.02178955078125, 
    "23": 0.0162353515625, 
    "24": 0.00982666015625, 
    "25": 0.00469970703125, 
    "26": 0.001708984375, 
    "27": 0.00042724609375, 
    "28": 6.103515625e-05
}
Rolling 8 dice possibilities.
{
    "32": 1.52587890625e-05, 
    "1": 0.8998870849609375, 
    "16": 1.52587890625e-05, 
    "17": 0.0001220703125, 
    "18": 0.00054931640625, 
    "19": 0.001708984375, 
    "20": 0.004058837890625, 
    "21": 0.0076904296875, 
    "22": 0.011962890625, 
    "23": 0.0155029296875, 
    "24": 0.0168914794921875, 
    "25": 0.0155029296875, 
    "26": 0.011962890625, 
    "27": 0.0076904296875, 
    "28": 0.004058837890625, 
    "29": 0.001708984375, 
    "30": 0.00054931640625, 
    "31": 0.0001220703125
}


}
"""