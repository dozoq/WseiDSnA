import random
import logging
from typing import List

# Set up logging
logger = logging.getLogger( __name__ )
logging.basicConfig( level=logging.INFO )

# Constants
N = 100
TASK_RANGE = (10, 90)
PROCESSORS = 3
POPULATION_SIZE = 100
GENERATIONS = 1000
MUTATION_RATE = 0.01

# Generate random task times
tasks = [random.randint( *TASK_RANGE ) for _ in range( N )]


def calculate_total_time ( solution: List[int] ) -> int:
    processor_times = [0] * PROCESSORS
    for i in range( N ):
        processor_times[solution[i]] += tasks[i]
    return max( processor_times )


def init_solution () -> List[int]:
    return [random.randint( 0, PROCESSORS - 1 ) for _ in range( N )]


def mutate ( solution: List[int] ) -> List[int]:
    new_solution = solution[:]
    if random.random() < MUTATION_RATE:
        mutation_index = random.randint( 0, N - 1 )
        new_solution[mutation_index] = random.randint( 0, PROCESSORS - 1 )
    return new_solution


def crossover ( parent1: List[int], parent2: List[int] ) -> List[int]:
    crossover_point = random.randint( 0, N - 1 )
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child


def genetic_algorithm () -> List[int]:
    population = [init_solution() for _ in range( POPULATION_SIZE )]
    best_solution = min( population, key=calculate_total_time )
    best_time = calculate_total_time( best_solution )

    for generation in range( GENERATIONS ):
        new_population = []
        for _ in range( POPULATION_SIZE ):
            parent1 = random.choice( population )
            parent2 = random.choice( population )
            child = crossover( parent1, parent2 )
            child = mutate( child )
            new_population.append( child )

        population = sorted( new_population, key=calculate_total_time )[:POPULATION_SIZE]
        current_best_solution = min( population, key=calculate_total_time )
        current_best_time = calculate_total_time( current_best_solution )

        if current_best_time < best_time:
            best_solution = current_best_solution
            best_time = current_best_time

        logger.debug( f"Generation {generation + 1}: Best Time: {best_time}" )

    return best_solution


def main ():
    best_solution = genetic_algorithm()
    best_time = calculate_total_time( best_solution )

    logger.info( "Task times:" )
    logger.info( [f"Task {i + 1}, Time: {task}ms" for i, task in enumerate( tasks )] )
    logger.info( f"Best solution: {best_solution}" )
    logger.info( f"Best solution total time: {best_time.__str__()}" )


if __name__ == '__main__':
    main()