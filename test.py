import numpy as np
import matplotlib.pyplot as plt

# Parameters
n = 10
num_trials = 100000

# Bernoulli variables {-0.5, 0.5}
X_vals = np.array([-0.5, 0.5])
probs = [0.5, 0.5]

# Moment calculations
E_absX3 = np.sum([abs(x)**3 * p for x, p in zip(X_vals, probs)])
E_X4 = np.sum([x**4 * p for x, p in zip(X_vals, probs)])
f_prime_bound = 1
f_double_prime_bound = 1

# Theoretical Stein bound from Lemma 3.4
term1 = (f_double_prime_bound / (2 * n**(3/2))) * n * E_absX3
term2 = f_prime_bound * np.sqrt(n * np.var([x**2 for x in X_vals])) / n
stein_bound = term1 + term2

# Define the functions
def f(x):
    return np.sin(x)

def f_prime(x):
    return np.cos(x)

# Monte Carlo simulation
f_prime_minus_Wf_vals = []

for _ in range(num_trials):
    X = np.random.choice(X_vals, size=n, replace=True)
    W = np.sum(X) / np.sqrt(n)
    fp = f_prime(W)
    Wf = W * f(W)
    f_prime_minus_Wf_vals.append(fp - Wf)

f_prime_minus_Wf_vals = np.array(f_prime_minus_Wf_vals)
empirical_mean = np.mean(f_prime_minus_Wf_vals)

# Plot
plt.figure(figsize=(10, 6))
plt.hist(f_prime_minus_Wf_vals, bins=100, density=True, alpha=0.7, color='skyblue', label="Empirical Distribution")
plt.axvline(empirical_mean, color='blue', linestyle='--', label=f"Empirical Mean ≈ {empirical_mean:.4f}")
plt.axvline(stein_bound, color='red', linestyle='-', label=f"Theoretical Bound ≈ {stein_bound:.4f}")
plt.axvline(-stein_bound, color='red', linestyle='-')
plt.title("Distribution of $f'(W) - W f(W)$")
plt.xlabel("$f'(W) - W f(W)$")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
