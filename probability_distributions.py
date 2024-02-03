import scipy.stats as stats

def fit_binomial_distribution(data, trials, success_prob):
    successes = data.sum()
    estimated_p = successes / (trials * len(data))
    binom_dist = stats.binom(n=trials, p=estimated_p)
    return {"n": trials, "p": estimated_p, "distribution": binom_dist}
