import numpy as np
from matplotlib import pyplot as plt
from scipy import stats, optimize
from math import log, exp

msi = [30.1, 36.3, 37.4, 37.5, 38.8, 41.9, 42.5, 42.6, 44.3, 44.3, 47.2, 49, 49.1, 50.3, 51.6, 52.5, 53.8, 56.7, 57.1, 59.8, 59.8, 61.6, 63.1, 67.3, 82.2, 98.5, 159.7, 161.8, 282.8, 681.5]
inverse_percentiles = [72.26, 64.3, 62.78, 62.58, 59.94, 56.17, 54.49, 54.27, 50.58, 48.33, 44.06, 40.28, 39.54, 38.18, 36.31, 35.3, 34.26, 29.9, 29.6, 26.77, 26.57, 25.46, 24.58, 22.15, 16.46, 10.06, 2.22, 1.98, 0.68, 0.3]
percentiles = [(100 - inverse_percentile)/100 for inverse_percentile in inverse_percentiles]


def mse(actual, expected):
    return (np.square(np.array(actual) - np.array(expected))).mean()


def gamma_parameters(x1, p1, x2, p2):
    # Standardize so that x1 < x2 and p1 < p2
    if p1 > p2:
        (p1, p2) = (p2, p1)
        (x1, x2) = (x2, x1)

    # function to find roots of for gamma distribution parameters
    def objective(alpha):
        return stats.gamma.ppf(p2, alpha) / stats.gamma.ppf(p1,
                                                            alpha) - x2 / x1

    # The objective function we're wanting to find a root of is decreasing.
    # We need to find an interval over which is goes from positive to negative.
    left = right = 1.0
    while objective(left) < 0.0:
        left /= 2
    while objective(right) > 0.0:
        right *= 2
    alpha = optimize.bisect(objective, left, right)
    beta = x1 / stats.gamma.ppf(p1, alpha)

    return alpha, beta


def lognormal_parameters(x1, p1, x2, p2):
    """Find parameters for a lognormal random variable X so that P(X < x1) = p1 and P(X < x2) = p2."""
    denom = stats.norm.ppf(p2) - stats.norm.ppf(p1)
    sigma = (log(x2) - log(x1)) / denom
    mu = exp((log(x1)*stats.norm.ppf(p2) - log(x2)*stats.norm.ppf(p1)) / denom)
    return mu, sigma


def normal_parameters(x1, p1, x2, p2):
    """Find parameters for a normal random variable X so that P(X < x1) = p1 and P(X < x2) = p2."""
    denom = stats.norm.ppf(p2) - stats.norm.ppf(p1)
    sigma = (x2 - x1) / denom
    mu = (x1*stats.norm.ppf(p2) - x2*stats.norm.ppf(p1)) / denom
    return mu, sigma


def eval_distrib():
    a, b = gamma_parameters(44.3, 0.495, 98.5, 0.9)
    print(a, b)

    log_mu, log_sigma = lognormal_parameters(44.3, 0.495, 98.5, 0.9)
    print(log_mu, log_sigma)

    mu, sigma = normal_parameters(44.3, 0.495, 98.5, 0.9)
    print(mu, sigma)

    gamma_percentiles = stats.gamma.cdf(msi, a=a, scale=b)
    gamma_error = mse(gamma_percentiles, percentiles)
    print(gamma_error)

    lognorm_percentiles = stats.lognorm.cdf(msi, s=log_sigma, scale=log_mu)
    lognorm_error = mse(lognorm_percentiles, percentiles)
    print(lognorm_error)

    norm_percentiles = stats.norm.cdf(msi, loc=mu, scale=sigma)
    norm_error = mse(norm_percentiles, percentiles)
    print(norm_error)

    # x = np.linspace(0, 600, 150)
    # y1 = stats.gamma.pdf(x, a=a, scale=b)
    # plt.plot(x, y1)
    # plt.show()

    # x = np.linspace(0, 600, 150)
    # y1 = stats.lognorm.pdf(x, s=log_sigma, scale=log_mu)
    # plt.plot(x, y1)
    # plt.show()

    # x = np.linspace(-100, 200, 150)
    # y1 = stats.norm.pdf(x, loc=mu, scale=sigma)
    # plt.plot(x, y1)
    # plt.show()


eval_distrib()
