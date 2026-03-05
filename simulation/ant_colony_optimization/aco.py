"""
Ant Colony Optimization (ACO) for the Traveling Salesman Problem (TSP)

This module implements the Ant System (AS) algorithm, the original ACO algorithm
proposed by Marco Dorigo (1992), applied to the Traveling Salesman Problem.

Background:
    Ants find the shortest path between their nest and a food source by laying
    pheromones on the ground. Shorter paths accumulate stronger pheromone trails
    because ants traverse them more frequently before evaporation occurs.
    This emergent behavior can be used to solve combinatorial optimization problems.

References:
    Dorigo, M., & Stützle, T. (2004). Ant Colony Optimization. MIT Press.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ACOConfig:
    """Configuration parameters for the ACO algorithm.

    Attributes:
        n_ants: Number of ants per iteration.
        n_iterations: Number of iterations to run.
        alpha: Pheromone influence weight (higher = more pheromone influence).
        beta: Heuristic influence weight (higher = more distance influence).
        rho: Pheromone evaporation rate (0 < rho < 1).
        q: Pheromone deposit constant (amount deposited per unit of tour quality).
        initial_pheromone: Initial pheromone level on all edges.
        seed: Optional random seed for reproducibility.
    """

    n_ants: int = 20
    n_iterations: int = 100
    alpha: float = 1.0
    beta: float = 2.0
    rho: float = 0.5
    q: float = 100.0
    initial_pheromone: float = 1.0
    seed: Optional[int] = None


@dataclass
class ACOResult:
    """Result of running the ACO algorithm.

    Attributes:
        best_tour: Ordered list of city indices for the best tour found.
        best_distance: Total distance of the best tour.
        history: Best distance found at each iteration.
    """

    best_tour: list[int]
    best_distance: float
    history: list[float] = field(default_factory=list)


class AntColonyOptimizer:
    """Ant Colony Optimizer for the Traveling Salesman Problem.

    Implements the classic Ant System (AS) algorithm where all ants deposit
    pheromones at the end of each iteration, proportional to the quality of
    their tour.

    Example:
        >>> cities = [(0, 0), (1, 0), (1, 1), (0, 1)]
        >>> aco = AntColonyOptimizer(cities)
        >>> result = aco.run()
        >>> len(result.best_tour) == len(cities)
        True
    """

    def __init__(self, cities: list[tuple[float, float]], config: Optional[ACOConfig] = None):
        """Initialize the optimizer.

        Args:
            cities: List of (x, y) coordinates for each city.
            config: ACO configuration parameters. Uses defaults if not provided.

        Raises:
            ValueError: If fewer than 2 cities are provided.
        """
        if len(cities) < 2:
            raise ValueError("At least 2 cities are required.")
        self.cities = cities
        self.config = config or ACOConfig()
        self.n_cities = len(cities)
        self._rng = random.Random(self.config.seed)
        self._distances = self._compute_distances()
        self._pheromones = self._initialize_pheromones()

    def _compute_distances(self) -> list[list[float]]:
        """Compute the Euclidean distance matrix between all cities."""
        n = self.n_cities
        dist = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                dx = self.cities[i][0] - self.cities[j][0]
                dy = self.cities[i][1] - self.cities[j][1]
                d = math.sqrt(dx * dx + dy * dy)
                dist[i][j] = d
                dist[j][i] = d
        return dist

    def _initialize_pheromones(self) -> list[list[float]]:
        """Initialize the pheromone matrix with the configured initial value."""
        n = self.n_cities
        return [[self.config.initial_pheromone] * n for _ in range(n)]

    def _tour_distance(self, tour: list[int]) -> float:
        """Compute the total distance of a tour (returns to start).

        Args:
            tour: Ordered list of city indices.

        Returns:
            Total tour distance including return to starting city.
        """
        total = 0.0
        n = len(tour)
        for i in range(n):
            total += self._distances[tour[i]][tour[(i + 1) % n]]
        return total

    def _construct_tour(self) -> list[int]:
        """Construct a single ant's tour using pheromone-guided probabilistic selection.

        Returns:
            A permutation of city indices representing the ant's tour.
        """
        start = self._rng.randint(0, self.n_cities - 1)
        visited = [False] * self.n_cities
        tour = [start]
        visited[start] = True

        for _ in range(self.n_cities - 1):
            current = tour[-1]
            probabilities = self._compute_probabilities(current, visited)
            next_city = self._select_next_city(probabilities)
            tour.append(next_city)
            visited[next_city] = True

        return tour

    def _compute_probabilities(self, current: int, visited: list[bool]) -> list[float]:
        """Compute selection probabilities for unvisited cities.

        Uses the ACO probability formula:
            p(i,j) = [τ(i,j)]^α * [η(i,j)]^β / Σ [τ(i,l)]^α * [η(i,l)]^β

        Args:
            current: Index of the current city.
            visited: Boolean list indicating visited cities.

        Returns:
            List of selection probabilities for each city (0.0 for visited cities).
        """
        alpha = self.config.alpha
        beta = self.config.beta
        weights = []
        for j in range(self.n_cities):
            if visited[j]:
                weights.append(0.0)
            else:
                dist = self._distances[current][j]
                heuristic = 1.0 / dist if dist > 0 else 1e10
                weight = (self._pheromones[current][j] ** alpha) * (heuristic ** beta)
                weights.append(weight)

        total = sum(weights)
        if total == 0:
            # Fallback: uniform probability over unvisited cities
            n_unvisited = sum(1 for v in visited if not v)
            return [0.0 if visited[j] else 1.0 / n_unvisited for j in range(self.n_cities)]

        return [w / total for w in weights]

    def _select_next_city(self, probabilities: list[float]) -> int:
        """Select the next city using roulette-wheel (fitness proportionate) selection.

        Args:
            probabilities: Selection probability for each city.

        Returns:
            Index of the selected city.
        """
        r = self._rng.random()
        cumulative = 0.0
        for city, prob in enumerate(probabilities):
            cumulative += prob
            if r <= cumulative:
                return city
        # Fallback: return the last city with non-zero probability
        for city in range(len(probabilities) - 1, -1, -1):
            if probabilities[city] > 0:
                return city
        raise RuntimeError("No city could be selected; all probabilities are zero.")

    def _evaporate_pheromones(self) -> None:
        """Apply pheromone evaporation to all edges."""
        rho = self.config.rho
        for i in range(self.n_cities):
            for j in range(self.n_cities):
                self._pheromones[i][j] *= (1.0 - rho)

    def _deposit_pheromones(self, tours: list[list[int]], distances: list[float]) -> None:
        """Deposit pheromones for all ants proportional to tour quality.

        Shorter tours receive more pheromone per edge (Q / L_k).

        Args:
            tours: List of tours constructed by each ant this iteration.
            distances: Corresponding tour distances.
        """
        for tour, dist in zip(tours, distances):
            deposit = self.config.q / dist
            n = len(tour)
            for i in range(n):
                a = tour[i]
                b = tour[(i + 1) % n]
                self._pheromones[a][b] += deposit
                self._pheromones[b][a] += deposit

    def run(self) -> ACOResult:
        """Run the ACO algorithm.

        Returns:
            ACOResult containing the best tour, its distance, and iteration history.
        """
        best_tour: list[int] = []
        best_distance = float("inf")
        history: list[float] = []

        for _ in range(self.config.n_iterations):
            tours = [self._construct_tour() for _ in range(self.config.n_ants)]
            distances = [self._tour_distance(t) for t in tours]

            # Find the best tour this iteration
            iteration_best_idx = min(range(len(distances)), key=lambda i: distances[i])
            if distances[iteration_best_idx] < best_distance:
                best_distance = distances[iteration_best_idx]
                best_tour = tours[iteration_best_idx][:]

            history.append(best_distance)

            # Update pheromones
            self._evaporate_pheromones()
            self._deposit_pheromones(tours, distances)

        return ACOResult(best_tour=best_tour, best_distance=best_distance, history=history)
