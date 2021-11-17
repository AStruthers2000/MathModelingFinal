import yfinance as yf
import datetime as dt
import csv
import os
import shutil

class DataGenerator:
    def ConvertDayToNumber(self, date):
        temp = dt.datetime(1899, 12, 30)
        delta = date - temp
        return float(delta.days)+(float(delta.seconds)/86400)

    def DaysSinceBeginning(self, start, current):
        return int(current - start)

    def GenerateData(self, ticker, period):
        stock = yf.Ticker(ticker)

        hist = stock.history(period=period)

        filename = "{0}-Data.csv".format(ticker)
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            
            startDate = -1
            for index, row in hist.iterrows():
                if startDate == -1:
                    startDate = self.ConvertDayToNumber(index)
                    writer.writerow(["Days since {0}".format(index), "Price at Closing (USD)"])
                writer.writerow([self.DaysSinceBeginning(startDate, self.ConvertDayToNumber(index)), row["Close"]])

        cwd = os.path.abspath(os.getcwd())
        path = cwd + "/Data/"
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
        shutil.move('{0}'.format(filename), path + '{0}'.format(filename))
        
            
if __name__ == "__main__":
    generator = DataGenerator()
    generator.GenerateData("AAPL", "max")
