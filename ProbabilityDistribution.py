import random
import bisect
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, uniform, binom

class ProbabilityDistribution:
    def __init__(self, probabilities=None, pdf=None, support=None):
        """
        Initializes a ProbabilityDistribution object.

        Parameters:
        - probabilities (dict): Dictionary of probabilities for discrete distributions.
        - pdf (function): Probability density function for continuous distributions.
        - support (tuple): Tuple defining the range of the support for continuous distributions.
        """
        self.is_continuous = pdf is not None
        if self.is_continuous:
            self.pdf = pdf
            self.support = support
            self.probabilities = self._discretize_pdf(pdf, support)
        else:
            self.probabilities = probabilities
        self.cdf = self._create_cdf()

    def _discretize_pdf(self, pdf, support, num_points=1000):
        """
        Discretizes a continuous probability density function (pdf) over a given support range.

        Parameters:
        - pdf (function): Probability density function.
        - support (tuple): Tuple defining the range of the support.
        - num_points (int): Number of points to discretize the pdf.

        Returns:
        - probabilities (dict): Discretized probabilities as a dictionary.
        """
        start, end = support
        step = (end - start) / num_points
        probabilities = {}
        for i in range(num_points):
            x = start + i * step
            probabilities[x] = pdf(x) * step
        return probabilities

    def _create_cdf(self):
        """
        Creates the cumulative distribution function (CDF) from probabilities.
        
        Returns:
        - cdf (list): List of tuples (cumulative probability, value).
        """
        items, probs = zip(*self.probabilities.items())
        total = sum(probs)
        if total != 1:
            probs = [p / total for p in probs]  # Normalize probabilities
        cdf = [sum(probs[:i + 1]) for i in range(len(probs))]
        return list(zip(cdf, items))

    def sample(self):
        """
        Samples from the probability distribution using the CDF.
        
        Returns:
        - value (float or int): Sampled value from the distribution.
        """
        r = random.random()
        idx = bisect.bisect(self.cdf, (r,))
        return self.cdf[idx][1]

    def expected_value(self):
        """
        Computes the expected value of the distribution.

        Returns:
        - ev (float or int): Expected value.
        """
        if all(isinstance(item, (int, float)) for item in self.probabilities):
            return sum(item * prob for item, prob in self.probabilities.items())
        else:
            raise ValueError("Expected value is not defined for categorical distributions")

    def variance(self):
        """
        Computes the variance of the distribution.

        Returns:
        - var (float): Variance.
        """
        if all(isinstance(item, (int, float)) for item in self.probabilities):
            mean = self.expected_value()
            return sum(prob * (item - mean) ** 2 for item, prob in self.probabilities.items())
        else:
            raise ValueError("Variance is not defined for categorical distributions")

    def std_dev(self):
        """
        Computes the standard deviation of the distribution.

        Returns:
        - std (float): Standard deviation.
        """
        return self.variance() ** 0.5

    def moment(self, k):
        """
        Computes the k-th moment of the distribution.

        Parameters:
        - k (int): Order of the moment.

        Returns:
        - moment (float or int): k-th moment.
        """
        if all(isinstance(item, (int, float)) for item in self.probabilities):
            return sum(prob * (item ** k) for item, prob in self.probabilities.items())
        else:
            raise ValueError("Moments are not defined for categorical distributions")

    def plot(self):
        """
        Plots the probability distribution.

        This method uses matplotlib to visualize either a bar chart for discrete distributions
        or a line plot for continuous distributions.
        """
        items, probs = zip(*self.probabilities.items())
        plt.bar(items, probs, width=0.1 if self.is_continuous else 0.5)
        plt.xlabel('Value')
        plt.ylabel('Probability')
        plt.title('Probability Distribution')
        plt.show()

    def __str__(self):
        """
        Returns a string representation of the ProbabilityDistribution object.
        """
        return f"ProbabilityDistribution({self.probabilities})"

    @staticmethod
    def from_continuous(pdf, support, num_points=1000):
        """
        Creates a ProbabilityDistribution object from a continuous probability density function.

        Parameters:
        - pdf (function): Probability density function.
        - support (tuple): Tuple defining the range of the support.
        - num_points (int): Number of points to discretize the pdf.

        Returns:
        - ProbabilityDistribution: Instance of ProbabilityDistribution for the given continuous distribution.
        """
        return ProbabilityDistribution(pdf=pdf, support=support)

    @staticmethod
    def normal(mean=0, std_dev=1, num_points=1000):
        """
        Creates a ProbabilityDistribution object for a normal distribution.

        Parameters:
        - mean (float): Mean of the normal distribution.
        - std_dev (float): Standard deviation of the normal distribution.
        - num_points (int): Number of points to discretize the pdf.

        Returns:
        - ProbabilityDistribution: Instance of ProbabilityDistribution for the normal distribution.
        """
        pdf = lambda x: norm.pdf(x, mean, std_dev)
        support = (mean - 4*std_dev, mean + 4*std_dev)
        return ProbabilityDistribution.from_continuous(pdf, support, num_points)

    @staticmethod
    def uniform(start=0, end=1, num_points=1000):
        """
        Creates a ProbabilityDistribution object for a uniform distribution.

        Parameters:
        - start (float): Start of the uniform distribution range.
        - end (float): End of the uniform distribution range.
        - num_points (int): Number of points to discretize the pdf.

        Returns:
        - ProbabilityDistribution: Instance of ProbabilityDistribution for the uniform distribution.
        """
        pdf = lambda x: uniform.pdf(x, start, end - start)
        support = (start, end)
        return ProbabilityDistribution.from_continuous(pdf, support, num_points)

    @staticmethod
    def binomial(n, p):
        """
        Creates a ProbabilityDistribution object for a binomial distribution.

        Parameters:
        - n (int): Number of trials.
        - p (float): Probability of success in each trial.

        Returns:
        - ProbabilityDistribution: Instance of ProbabilityDistribution for the binomial distribution.
        """
        probabilities = {k: binom.pmf(k, n, p) for k in range(n + 1)}
        return ProbabilityDistribution(probabilities)

# Example usage for discrete distribution
'''discrete_dist = ProbabilityDistribution({"A": 0.5, "B": 0.3, "C": 0.2})
print(discrete_dist)
print("Sample:", discrete_dist.sample())

try:
    print("Expected Value:", discrete_dist.expected_value())
except ValueError as e:
    print(e)

try:
    print("Variance:", discrete_dist.variance())
except ValueError as e:
    print(e)

discrete_dist.plot()'''

# Example usage for continuous distribution (Normal distribution)
'''continuous_dist = ProbabilityDistribution.normal(mean=0, std_dev=1)
print(continuous_dist)
print("Sample:", continuous_dist.sample())
continuous_dist.plot()'''

# Example usage for continuous distribution (Uniform distribution)
'''uniform_dist = ProbabilityDistribution.uniform(start=0, end=10)
print(uniform_dist)
print("Sample:", uniform_dist.sample())
uniform_dist.plot()'''

# Example usage for discrete distribution (Binomial distribution)
'''binom_dist = ProbabilityDistribution.binomial(n=10, p=0.5)
print(binom_dist)
print("Sample:", binom_dist.sample())
binom_dist.plot()'''
