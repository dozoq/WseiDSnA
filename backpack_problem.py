import random
import logging

# Set up logging
logger = logging.getLogger( __name__ )
logging.basicConfig( level=logging.INFO )

# Constants
BACKPACK_CAPACITY = 2500
NUMBER_OF_ITEMS = 100
MIN_ITEM_VOLUME = 10
MAX_ITEM_VOLUME = 90
NUMBER_OF_GENERATIONS = 300000

# Generate random item volumes
items_volume = [random.randint( MIN_ITEM_VOLUME, MAX_ITEM_VOLUME ) for _ in range( NUMBER_OF_ITEMS )]


def calculate_volume ( element ):
    volume = sum( items_volume[i] for i in range( NUMBER_OF_ITEMS ) if element[i] == 1 )
    return volume if volume <= BACKPACK_CAPACITY else 0


def init_element ():
    return [random.choice( [0, 1] ) for _ in range( NUMBER_OF_ITEMS )]


def mutate ( element ):
    new_element = element[:]
    mutation_index = random.randint( 0, NUMBER_OF_ITEMS - 1 )
    new_element[mutation_index] = 1 - new_element[mutation_index]
    return new_element


def evolutionary_algorithm ():
    best_solution = init_element()
    best_evaluation = calculate_volume( best_solution )

    for generation in range( NUMBER_OF_GENERATIONS ):
        offspring = mutate( best_solution )
        new_evaluation = calculate_volume( offspring )

        if new_evaluation > best_evaluation:
            best_solution = offspring
            best_evaluation = new_evaluation

        logger.debug( f"Generation {generation + 1}: Best solution: {best_solution}, Value: {best_evaluation}" )

    return best_solution


def main ():
    best_solution = evolutionary_algorithm()
    best_evaluation = calculate_volume( best_solution )

    logger.info( "Item list:" )
    logger.info( [f"Item {i + 1}, Volume: {volume}" for i, volume in enumerate( items_volume )] )
    logger.info( f"Best solution: {best_solution}" )
    logger.info( f"Best solution value: {best_evaluation.__str__()}" )


if __name__ == '__main__':
    main()
