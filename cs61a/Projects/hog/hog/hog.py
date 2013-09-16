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
    return get_statistical_max(score,opponent_score) # Replace this statement

### EXPECTED VALUES
from operator import sub, add
def get_expected_value(opponent_score, dice=six_sided):
    """ based on 100k rolls """
    six_list = [getBaconScore(opponent_score),
                3.50332,
                5.86032,
                7.36786, 
                8.25786,
                8.59203,
                8.74338,
                8.50806,
                8.17981,
                7.78308, 
                7.33582]
    four_list = [getBaconScore(opponent_score),
                2.50498,
                3.80794,
                4.37158,
                4.49637,
                4.3196,
                4.02963,
                3.67541,
                3.33545,
                2.9528,
                2.64403]

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
    percent_one = .8333 #change of rolling a "1" with rolling 10 dice

    def adjust_expected_values_based_on_scores(score, opponent_score, eplist):
        """
        eplist is list of expected values
        """
        #adjust based on swine swap 
        def adjust_swine_swap(score, opponent_score, eplist):
            score_with_zero = score + getBaconScore(opponent_score)
            score_with_one = score + 1  #chances of rolling a 1 with 10 dice is 83%
            
            #if 0 causes swine swap, calculate benefit and put in eplist
            def is_beneficial(old_diff, expected):
                return (expected > old_diff)

            if (causes_swine_swap(score_with_zero, opponent_score)):
                #if is_beneficial(eplist[0], opponent_score - score_with_zero):
                #    eplist[0] = opponent_score - score_with_zero
                    #print(eplist)
                eplist[0] = max(eplist[0], opponent_score - score_with_zero) 
                #print(eplist)

            if (causes_swine_swap(score_with_one, opponent_score)):
                #if is_beneficial(eplist[10], opponent_score - score_with_one):
                #    eplist[10] = opponent_score - score_with_one
                    #print(eplist)
                eplist[10] = max(eplist[10], 
                    (opponent_score - score_with_one) * percent_one)
                #print(eplist)
            return eplist
            
        #adjust based on trying to force a four dice
        def adjust_try_four(score, opponent_score, eplist):
            score_with_zero = score + getBaconScore(opponent_score)
            score_with_one = score + 1

            #if 0 could cause opponent to have to roll a four_sided dice, add x to 0
            if ((score_with_zero + opponent_score) % 7 == 0):
                diff = score_with_zero + 4
                eplist[0] = max(eplist[0], diff)

            if ((score_with_one + opponent_score) % 7 == 0):
                diff = score_with_zero + 4
                eplist[10] = max(eplist[10], diff * percent_one)

            return eplist

        eplist = adjust_swine_swap(score, opponent_score, eplist)
        eplist = adjust_try_four(score, opponent_score, eplist)
        return eplist

    eplist = get_expected_value(opponent_score, select_dice(score, opponent_score))

    adjusted = adjust_expected_values_based_on_scores(score, opponent_score, eplist)

    num_dice = adjusted.index(max(adjusted))
    
    return num_dice

def is_score_swap_within_realm_of_possibility(score, opponent_score):
    """ Returns true if a score_swap is within a certain threshold (e.g. 40 - 60%)
    """

def attempt_score_swap(score, opponent_score):
    """ This function returns the dice roll that will attempt to get a score swap
    1)  It is meant to be used when the chips are down (e.g. opponent score is over 50)
        and your score is within a certain threshold (e.g. 40 to 60% of opponent score)
    2)  Will calculate what you need to trigger a score swap 
        a)  Will consider how many dice to roll to maximize this chance (e.g. if zero
            dice will work, then you can just return swap_strategy)
        b)  Otherwise, attempt to find the number of dice to roll to maximize chance
    """

def attempt_to_roll_x(x, dice=six_sided):
    """ This function attempts to roll x, based on a certain number of dice and
        rolling from 1 - 10 dice max. """


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
