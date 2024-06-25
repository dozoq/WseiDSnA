import random
import math
import logging

# Set up logging
logger = logging.getLogger( __name__ )
logging.basicConfig( level=logging.INFO )

# Constants
POPULATION_SIZE = 200
NUM_GENERATIONS = 1000
MUTATION_RATE = 0.01
SELECTION_RATE = 0.5


def fitness_function ( x, y ):
    return abs( math.sin( x ) + math.sin( 2 * x ) + math.sin( 3 * x ) + math.sin( 4 * x ) +
                math.cos( y ) + math.cos( 2 * y ) + math.cos( 3 * y ) + math.cos( 4 * y ) )


def initialize_population ( size ):
    population = []
    for _ in range( size ):
        x = random.uniform( 0, 2 * math.pi )
        y = random.uniform( 0, 2 * math.pi )
        population.append( (x, y) )
    return population


def select_parents ( population, fitnesses ):
    selected = []
    for _ in range( len( population ) ):
        i, j = random.sample( range( len( population ) ), 2 )
        selected.append( population[i] if fitnesses[i] < fitnesses[j] else population[j] )
    return selected


def crossover ( parent1, parent2 ):
    alpha = random.random()
    x = alpha * parent1[0] + (1 - alpha) * parent2[0]
    y = alpha * parent1[1] + (1 - alpha) * parent2[1]
    return x, y


def mutate ( solution ):
    x, y = solution
    if random.random() < MUTATION_RATE:
        x += random.uniform( -0.01, 0.01 )
        y += random.uniform( -0.01, 0.01 )
        x = min( max( x, 0 ), 2 * math.pi )
        y = min( max( y, 0 ), 2 * math.pi )
    return x, y


def genetic_algorithm ():
    population = initialize_population( POPULATION_SIZE )
    best_solution = None
    best_fitness = float( 'inf' )

    for generation in range( NUM_GENERATIONS ):
        fitnesses = [fitness_function( x, y ) for x, y in population]
        best_index = fitnesses.index( min( fitnesses ) )

        if fitnesses[best_index] < best_fitness:
            best_solution = population[best_index]
            best_fitness = fitnesses[best_index]

        if best_fitness <= 8:
            break

        parents = select_parents( population, fitnesses )
        population = [mutate( crossover( parents[i], parents[i + 1] ) ) for i in range( 0, POPULATION_SIZE, 2 )]

        logger.info( f"Generation {generation + 1}: Best Fitness: {best_fitness}" )

    return best_solution, best_fitness


def main ():
    best_solution, best_fitness = genetic_algorithm()
    logger.info( f"Best solution: x = {best_solution[0]}, y = {best_solution[1]}" )
    logger.info( f"Best solution fitness: {best_fitness}" )


if __name__ == '__main__':
    main()
