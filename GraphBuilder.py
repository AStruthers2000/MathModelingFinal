class GraphGenerator():
    def LinearFit(self):
        #linear fit
        points = LinearFit(xVals, yVals)
        modelName = "linear fit"
        mse = CalculateMSE(points, yVals)
        if mse < minMSE:
            minMSE = mse
            bestModel = modelName
        print("Mean-Square Error for {0}: {1}".format(modelName, mse))
        plt.figure(1)
        plt.plot(xVals, points,'red')


    def ExponentialFit(self):
        #exponential fit
        points = ExponentialFit(xVals, yVals)
        modelName = "exponential fit"
        mse = CalculateMSE(points, yVals)
        if mse < minMSE:
            minMSE = mse
            bestModel = modelName
        print("Mean-Square Error for {0}: {1}".format(modelName, mse))
        plt.figure(1)
        plt.plot(xVals, points, 'green')


    def LogisticLinearFit(self):
        #logistic linear fit
        points = LogisticLinearFit(xVals, yVals, pPrime)
        modelName = "logistic linear fit"
        mse = CalculateMSE(points, yVals)
        if mse < minMSE:
            minMSE = mse
            bestModel = modelName
        print("Mean-Square Error for {0}: {1}".format(modelName, mse))
        plt.figure(1)
        plt.plot(xVals, points, 'orange')


    def LogisticQuadraticFit(self):
        #logistic quadratic fit
        points = LogisticQuadraticFit(xVals, yVals, pPrime)
        modelName = "logistic quadratic fit"
        mse = CalculateMSE(points, yVals)
        if mse < minMSE:
            minMSE = mse
            bestModel = modelName
        print("Mean-Square Error for {0}: {1}".format(modelName, mse))
        plt.figure(1)
        plt.plot(xVals, points, 'magenta')


print("====="*5+"\nThe best model for this data is the {0}, with a Mean-Square Error value of {1}".format(bestModel, minMSE))

plt.title("Population vs. Various Models")
plt.ylabel("Population")
plt.xlabel("Time")
plt.legend(["Linear", "Exponential", "Logistic Linear", "Logistic Quadratic", "Population"])
plt.ylim(yMin, yMax)

plot4 = plt.figure(4)
plt.scatter(xVals, yVals)
plt.title("Population of Belgium from 1960 to 2020")
plt.ylabel("Population of Belgium (10 million people)")
plt.xlabel("Time (year since 1960)")
plt.legend(["Population"])

plt.show()
