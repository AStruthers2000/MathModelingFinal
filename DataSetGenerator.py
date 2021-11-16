import yfinance as yf
import datetime as dt
import csv

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

        with open("{0}-Data.csv".format(ticker), 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            
            startDate = -1
            for index, row in hist.iterrows():
                if startDate == -1:
                    startDate = self.ConvertDayToNumber(index)
                    writer.writerow(["Days since {0}".format(index), "Price at Closing (USD)"])
                writer.writerow([self.DaysSinceBeginning(startDate, self.ConvertDayToNumber(index)), row["Close"]])
            
if __name__ == "__main__":
    generator = DataGenerator()
    generator.GenerateData("^GSPC", "max")
