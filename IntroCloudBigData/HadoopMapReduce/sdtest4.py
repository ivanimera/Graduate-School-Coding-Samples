from mrjob.job import MRJob

class stdev(MRJob):

    def mapper(self, _, line):
        timestamps, pressure, temperature = line.split(",")
        yield ("pressure", float(pressure))
        yield ("temperature", float(temperature))

    def combiner(self,name, values):
        N = S = S2 = 0
        for v in values:
            N += 1
            S += v
            S2 += v * v
        yield (name, (S, S2, N))

    def reducer(self, name, values):
        SumN = SumS = SumS2 = 0
        for S, S2, N in values:
            SumN += N
            SumS += S
            SumS2 += S2
        SumS2 = float(SumS2) / SumN
        SumS = float(SumS) / SumN
        SumS = SumS * SumS
        result = (SumS2-SumS)**0.5
        yield (name, result)


if __name__ == '__main__':
  stdev.run()