
def takeStep(n):
    if n == 1:  # base case
        return "Easy"
    else:
        thisStep = "step(" + str(n) + ")"
        previousSteps = takeStep(n-1)      # recursive call
        return thisStep + " + " + previousSteps


