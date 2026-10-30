import random
import matplotlib.pyplot as plt
# imports aan de top want das gewoon de norm


# Stap 1: Virusgenoom
def generate_virus(length: int) -> str:
    """Generate a random genome.

    >>> len(generate_virus(4))
    4
    >>> generate_virus(0)
    ''
    >>> type(generate_virus(3))
    <class 'str'>
    >>> all([len(generate_virus(x)) == x for x in range(8)])
    True
    >>> set(generate_virus(1000)) <= set("ACGT")
    True
    """
    return "".join(random.choices("ACGT", k=length))


# Stap 2: Muteren
def mutate(virus: str) -> str:
    """Change one nucleotide at random.

    >>> mutate("")
    ''
    >>> mutate("A") in ["C", "G", "T"]
    True
    >>> len(mutate("ACGT"))
    4
    >>> sum([a != b for a, b in zip("ACGTAC", mutate("ACGTAC"))])
    1
    >>> viruses = [generate_virus(5) for _ in range(1000)]
    >>> all([mutate(virus) != virus for virus in viruses])
    True
    """
    if not virus:
        return virus

    index = random.randrange(len(virus))
    alternatives = "".join(
        nucleotide for nucleotide in "ACGT" if nucleotide != virus[index]
    )
    return virus[:index] + random.choice(alternatives) + virus[index + 1:]


# Stap 3: Afsterven
def kill(viruses: list[str], mortality_prob: float) -> list[str]:
    """Remove viruses according to the mortality probability.

    >>> kill(["A", "C"], 1)
    []
    >>> kill(["A", "C"], 0)
    ['A', 'C']
    >>> kill([], 0.5)
    []
    >>> 700 < len(kill(["A"] * 1000, 0.2)) < 900
    True
    """
    return [virus for virus in viruses if random.random() >= mortality_prob]


# Stap 4: Reproductie
def reproduce(viruses: list[str], mutation_prob: float, reproduction_prob: float) -> list[str]:
    """Return the population with any new offspring.

    >>> reproduce(["AC"], 0, 0)
    ['AC']
    >>> reproduce(["AC"], 0, 1)
    ['AC', 'AC']
    >>> reproduce([], 0.5, 0.5)
    []
    >>> population = reproduce(["AAAA"], 1, 1)
    >>> population[0] == "AAAA" and population[1] != "AAAA"
    True
    >>> 1100 < len(reproduce(["A"] * 1000, 0, 0.2)) < 1300
    True
    """
    population = viruses.copy()
    for virus in viruses:
        if random.random() < reproduction_prob:
            child = mutate(virus) if random.random() < mutation_prob else virus
            population.append(child)
    return population


# Stap 5: Resistentie
def is_resistant(virus: str) -> bool:
    """Return whether the genome contains the resistance sequence.

    >>> is_resistant("ACAAAG")
    True
    >>> is_resistant("ACAG")
    False
    >>> is_resistant("AATAA")
    False
    >>> is_resistant("")
    False
    """
    return "AAA" in virus


# Stap 6: Reproductiekans
def reproduction_probability(viruses: list[str], max_reproduction_prob: float, max_population: int) -> float:
    """Calculate reproduction probability from the current population size.

    >>> reproduction_probability([], 0.5, 100)
    0.5
    >>> reproduction_probability([], 0.5, 0)
    0
    >>> reproduction_probability(["A"] * 50, 0.5, 100)
    0.25
    >>> reproduction_probability(["A"] * 100, 0.5, 100)
    0.0
    """
    return (
        (1 - (len(viruses) / max_population)) * max_reproduction_prob
        if max_population > 0
        else 0
    )


# Stap 7: Simuleren met een virusremmer
def simulate(viruses: list[str], mortality_prob: float, mutation_prob: float, max_reproduction_prob: float,
             max_population: int, timesteps: int = 500) -> list[int]:
    """Simulate a population and return its size at each timestep.

    >>> simulate(["ACGT"], 0.1, 0.1, 0.5, 100, timesteps=0)
    [1]
    >>> viruses = [generate_virus(4) for _ in range(100)]
    >>> len(simulate(viruses, 1, 0, 0, 0))
    501
    >>> simulate(["ACGT"] * 10, 1, 0, 0.5, 100, timesteps=3)
    [10, 0, 0, 0]
    >>> simulate(["AAAA"], 0, 0, 0, 100, timesteps=2)
    [1, 1, 1]
    """
    viruses = viruses.copy()
    population_sizes = [len(viruses)]

    for timestep in range(timesteps):
        viruses = kill(viruses, mortality_prob)
        reproduction_prob = reproduction_probability(
            viruses, max_reproduction_prob, max_population
        )

        if timestep >= 100:
            resistant = [virus for virus in viruses if is_resistant(virus)]
            non_resistant = [virus for virus in viruses if not is_resistant(virus)]
            viruses = non_resistant + reproduce(
                resistant, mutation_prob, reproduction_prob
            )
        else:
            viruses = reproduce(viruses, mutation_prob, reproduction_prob)

        population_sizes.append(len(viruses))

    return population_sizes


if __name__ == "__main__":
    n_simulations = 100
    n_simulations_cured = 0

    for i in range(n_simulations):
        viruses = [generate_virus(4) for _ in range(100)]
        result = simulate(viruses, 0.1, 0.1, 0.5, 100, timesteps=500)

        if result[-1] == 0:
            n_simulations_cured += 1

    labels = ["Cured", "Not Cured"]
    sizes = [n_simulations_cured, n_simulations - n_simulations_cured]

    fig1, ax1 = plt.subplots(figsize=(8, 8))
    ax1.pie(sizes, labels=labels, autopct="%1i%%", startangle=90)
    ax1.axis("equal")
    plt.title("Pie chart of cured and non cured simulations")
    plt.show()
