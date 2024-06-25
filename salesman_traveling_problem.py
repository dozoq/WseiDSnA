import random
import itertools
import logging

# Set up logging
logger = logging.getLogger( __name__ )
logging.basicConfig( level=logging.INFO )

# Constants
NUM_CITIES = 100
MIN_DISTANCE = 10
MAX_DISTANCE = 90


# Generate a random distance matrix
def generate_distance_matrix ( num_cities, min_distance, max_distance ):
    matrix = [[0 if i == j else random.randint( min_distance, max_distance ) for j in range( num_cities )] for i in
              range( num_cities )]
    return matrix


distance_matrix = generate_distance_matrix( NUM_CITIES, MIN_DISTANCE, MAX_DISTANCE )


def nearest_neighbor_tsp ( distance_matrix ):
    num_cities = len( distance_matrix )
    visited = [False] * num_cities
    tour = [0]  # Start from the first city
    visited[0] = True

    for _ in range( num_cities - 1 ):
        last_city = tour[-1]
        next_city = None
        min_distance = float( 'inf' )

        for city in range( num_cities ):
            if not visited[city] and distance_matrix[last_city][city] < min_distance:
                next_city = city
                min_distance = distance_matrix[last_city][city]

        tour.append( next_city )
        visited[next_city] = True

    tour.append( 0 )  # Return to the starting city
    return tour


def calculate_tour_length ( tour, distance_matrix ):
    total_length = 0
    for i in range( len( tour ) - 1 ):
        total_length += distance_matrix[tour[i]][tour[i + 1]]
    return total_length


def main ():
    tour = nearest_neighbor_tsp( distance_matrix )
    total_length = calculate_tour_length( tour, distance_matrix )

    logger.info( "Distance matrix:" )
    for row in distance_matrix:
        logger.info( row )
    logger.info( f"Optimal tour: {tour}" )
    logger.info( f"Total tour length: {total_length}" )


if __name__ == '__main__':
    main()
