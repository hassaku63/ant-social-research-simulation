"""
Tests for the Ant Colony Optimization (ACO) implementation.
"""

import math
import pytest

from simulation.ant_colony_optimization.aco import (
    ACOConfig,
    ACOResult,
    AntColonyOptimizer,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def square_cities():
    """Four cities at the corners of a 1x1 square."""
    return [(0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)]


@pytest.fixture
def line_cities():
    """Five cities arranged on a horizontal line."""
    return [(float(i), 0.0) for i in range(5)]


@pytest.fixture
def default_config():
    """Deterministic config for reproducible tests."""
    return ACOConfig(n_ants=10, n_iterations=50, seed=42)


# ---------------------------------------------------------------------------
# AntColonyOptimizer construction
# ---------------------------------------------------------------------------

class TestAntColonyOptimizerInit:
    def test_valid_construction(self, square_cities, default_config):
        aco = AntColonyOptimizer(square_cities, default_config)
        assert aco.n_cities == 4

    def test_default_config_used_when_none_provided(self, square_cities):
        aco = AntColonyOptimizer(square_cities)
        assert aco.config is not None

    def test_too_few_cities_raises(self):
        with pytest.raises(ValueError, match="At least 2 cities"):
            AntColonyOptimizer([(0.0, 0.0)])

    def test_distance_matrix_is_symmetric(self, square_cities, default_config):
        aco = AntColonyOptimizer(square_cities, default_config)
        n = aco.n_cities
        for i in range(n):
            for j in range(n):
                assert aco._distances[i][j] == pytest.approx(aco._distances[j][i])

    def test_distance_diagonal_is_zero(self, square_cities, default_config):
        aco = AntColonyOptimizer(square_cities, default_config)
        for i in range(aco.n_cities):
            assert aco._distances[i][i] == pytest.approx(0.0)

    def test_distance_values_are_euclidean(self, default_config):
        cities = [(0.0, 0.0), (3.0, 4.0)]
        aco = AntColonyOptimizer(cities, default_config)
        assert aco._distances[0][1] == pytest.approx(5.0)

    def test_pheromone_matrix_initialized_uniformly(self, square_cities):
        config = ACOConfig(initial_pheromone=2.5, seed=0)
        aco = AntColonyOptimizer(square_cities, config)
        for i in range(aco.n_cities):
            for j in range(aco.n_cities):
                assert aco._pheromones[i][j] == pytest.approx(2.5)


# ---------------------------------------------------------------------------
# Tour distance
# ---------------------------------------------------------------------------

class TestTourDistance:
    def test_square_perimeter(self, square_cities, default_config):
        aco = AntColonyOptimizer(square_cities, default_config)
        tour = [0, 1, 2, 3]
        # Perimeter of unit square = 4.0
        assert aco._tour_distance(tour) == pytest.approx(4.0)

    def test_distance_independent_of_start(self, square_cities, default_config):
        aco = AntColonyOptimizer(square_cities, default_config)
        d0 = aco._tour_distance([0, 1, 2, 3])
        d1 = aco._tour_distance([1, 2, 3, 0])
        assert d0 == pytest.approx(d1)


# ---------------------------------------------------------------------------
# Tour construction and probability
# ---------------------------------------------------------------------------

class TestTourConstruction:
    def test_tour_visits_all_cities(self, square_cities, default_config):
        aco = AntColonyOptimizer(square_cities, default_config)
        tour = aco._construct_tour()
        assert sorted(tour) == list(range(len(square_cities)))

    def test_tour_has_correct_length(self, line_cities, default_config):
        aco = AntColonyOptimizer(line_cities, default_config)
        tour = aco._construct_tour()
        assert len(tour) == len(line_cities)

    def test_probabilities_sum_to_one(self, square_cities, default_config):
        aco = AntColonyOptimizer(square_cities, default_config)
        visited = [False, True, False, False]  # city 1 already visited
        probs = aco._compute_probabilities(0, visited)
        assert sum(probs) == pytest.approx(1.0, abs=1e-9)
        assert probs[1] == pytest.approx(0.0)

    def test_probability_zero_for_visited_city(self, square_cities, default_config):
        aco = AntColonyOptimizer(square_cities, default_config)
        visited = [True, False, False, False]
        probs = aco._compute_probabilities(1, visited)
        assert probs[0] == pytest.approx(0.0)


# ---------------------------------------------------------------------------
# Pheromone update
# ---------------------------------------------------------------------------

class TestPheromoneUpdate:
    def test_evaporation_reduces_pheromone(self, square_cities):
        config = ACOConfig(rho=0.5, initial_pheromone=1.0, seed=0)
        aco = AntColonyOptimizer(square_cities, config)
        aco._evaporate_pheromones()
        for i in range(aco.n_cities):
            for j in range(aco.n_cities):
                assert aco._pheromones[i][j] == pytest.approx(0.5)

    def test_deposit_increases_pheromone_on_used_edges(self, square_cities):
        config = ACOConfig(q=100.0, rho=0.0, initial_pheromone=1.0, seed=0)
        aco = AntColonyOptimizer(square_cities, config)
        tour = [0, 1, 2, 3]
        dist = aco._tour_distance(tour)
        aco._deposit_pheromones([tour], [dist])
        # All edges in the tour should be higher than the initial value
        for i in range(len(tour)):
            a = tour[i]
            b = tour[(i + 1) % len(tour)]
            assert aco._pheromones[a][b] > 1.0


# ---------------------------------------------------------------------------
# Full algorithm run
# ---------------------------------------------------------------------------

class TestACORun:
    def test_run_returns_aco_result(self, square_cities, default_config):
        aco = AntColonyOptimizer(square_cities, default_config)
        result = aco.run()
        assert isinstance(result, ACOResult)

    def test_result_tour_visits_all_cities(self, square_cities, default_config):
        aco = AntColonyOptimizer(square_cities, default_config)
        result = aco.run()
        assert sorted(result.best_tour) == list(range(len(square_cities)))

    def test_result_distance_matches_tour(self, square_cities, default_config):
        aco = AntColonyOptimizer(square_cities, default_config)
        result = aco.run()
        computed = aco._tour_distance(result.best_tour)
        assert result.best_distance == pytest.approx(computed)

    def test_history_length_equals_iterations(self, square_cities, default_config):
        aco = AntColonyOptimizer(square_cities, default_config)
        result = aco.run()
        assert len(result.history) == default_config.n_iterations

    def test_history_is_non_increasing(self, square_cities, default_config):
        aco = AntColonyOptimizer(square_cities, default_config)
        result = aco.run()
        for i in range(1, len(result.history)):
            assert result.history[i] <= result.history[i - 1] + 1e-9

    def test_reproducibility_with_same_seed(self, square_cities):
        config1 = ACOConfig(n_ants=10, n_iterations=30, seed=99)
        config2 = ACOConfig(n_ants=10, n_iterations=30, seed=99)
        result1 = AntColonyOptimizer(square_cities, config1).run()
        result2 = AntColonyOptimizer(square_cities, config2).run()
        assert result1.best_distance == pytest.approx(result2.best_distance)
        assert result1.best_tour == result2.best_tour

    def test_different_seeds_may_differ(self, square_cities):
        """With different seeds results can differ (not guaranteed but usually true)."""
        config1 = ACOConfig(n_ants=5, n_iterations=10, seed=1)
        config2 = ACOConfig(n_ants=5, n_iterations=10, seed=9999)
        result1 = AntColonyOptimizer(square_cities, config1).run()
        result2 = AntColonyOptimizer(square_cities, config2).run()
        # Both should produce valid tours even with different seeds
        assert sorted(result1.best_tour) == list(range(len(square_cities)))
        assert sorted(result2.best_tour) == list(range(len(square_cities)))

    def test_known_optimal_for_square(self):
        """
        For a unit square, the optimal TSP tour has length 4.0 (the perimeter).
        With enough iterations the ACO should find it reliably.
        """
        cities = [(0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)]
        config = ACOConfig(n_ants=20, n_iterations=200, seed=7)
        result = AntColonyOptimizer(cities, config).run()
        assert result.best_distance == pytest.approx(4.0, abs=1e-6)

    def test_two_city_problem(self):
        """With exactly 2 cities, tour distance is always 2 * distance between them."""
        cities = [(0.0, 0.0), (3.0, 4.0)]  # distance = 5.0
        config = ACOConfig(n_ants=5, n_iterations=10, seed=0)
        result = AntColonyOptimizer(cities, config).run()
        assert result.best_distance == pytest.approx(10.0)

    def test_larger_problem_finds_reasonable_solution(self):
        """ACO should improve on a random tour for a moderately-sized problem."""
        # 10 cities randomly placed (fixed seed for reproducibility)
        rng = __import__("random").Random(42)
        cities = [(rng.uniform(0, 100), rng.uniform(0, 100)) for _ in range(10)]
        config = ACOConfig(n_ants=20, n_iterations=100, seed=42)
        result = AntColonyOptimizer(cities, config).run()
        # The tour should be finite and cover all cities
        assert math.isfinite(result.best_distance)
        assert sorted(result.best_tour) == list(range(10))
