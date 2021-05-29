import random
import matplotlib.pyplot as plt


def error(candidate, dataX, dataY):
    """
    This function computes the sum of vertical square distances of a data set from a line.
    param: candidate: Dictionary containing gradient "m" and y-intercept "c", defining a line.
    return: The sum of vertical square distances between data and line.
    """
    err = 0
    for x, y in zip(dataX, dataY):
        y_ = candidate["m"] * x + candidate["c"]
        err = err + (y-y_)**2
    return err


## Set the random seed to allow repeatable random number generation.
random.seed(15)

## Choose m and c, and generate (x, y) pairs at random.
m = 0.25
c = 3
X = [random.random()*10 for _ in range(20)]
Y = [m * x + c + (random.random()-0.5)*0.2 for x in X]

## Plot the data points.
plt.scatter(X, Y, label="Data")

## Randomly generate the first generation of candidate solutions.
candidates = [{
    "m": (random.random() - 0.5) * 10,
    "c": (random.random() - 0.5) * 10
} for _ in range(100)]

## Compute the error for each candidate.
for candidate in candidates:
    candidate["error"] = error(candidate, X, Y)

## Sort the candidates from best to worst, and display the attributes of the best.
candidates.sort(key=lambda x: x["error"])
print(
    "m:", round(candidates[0]["m"], 2),
    "c:", round(candidates[0]["c"], 2),
    "e:", round(candidates[0]["error"], 2)
)

## Draw the best candidate line from the first generation.
plt.plot([0, 10], [candidates[0]['c'], 10*candidates[0]['m']+candidates[0]['c']], label="First candidate solution")

## Iteratively improve the solution.
for index in range(50):
    ## Keep the best 25% of candidates and throw away the rest.
    candidates = candidates[:25]

    ## Generate new candidates by randomly perturbing those we kept from the previous generation.
    for i in range(25):
        for _ in range(3):
            new_candidate = {
                "m": candidates[i]["m"] + (random.random()-0.5)*10/100,
                "c": candidates[i]["c"] + (random.random()-0.5)*10/100
            }
            candidates.append(new_candidate)

    ## Compute the error for each candidate.
    for candidate in candidates:
        candidate["error"] = error(candidate, X, Y)

    ## Sort the candidates from best to worst, and display the attributes of the best.
    candidates.sort(key=lambda x: x["error"])
    print(
        "m:", round(candidates[0]["m"], 2),
        "c:", round(candidates[0]["c"], 2),
        "e:", round(candidates[0]["error"], 2)
    )

## Draw the best candidate line from the final generation.
plt.plot([0, 10], [candidates[0]['c'], 10*candidates[0]['m']+candidates[0]['c']], label="Final solution")

## Display the plot.
plt.legend()
plt.show()
