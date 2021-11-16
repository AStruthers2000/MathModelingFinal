from DataSetGenerator import DataGenerator

generator = DataGenerator()
generator.GenerateData("TSLA", "1y")
generator.GenerateData("^GSPC", "max")
