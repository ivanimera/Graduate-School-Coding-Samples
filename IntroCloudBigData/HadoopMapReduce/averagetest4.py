from mrjob.job import MRJob


class Avg(MRJob):
    def mapper(self, _, line):
        timestamps, pressure, temperature = line.split(",")
        if temperature != "" and pressure != "" and pressure != "0.0":
            # Filter NA or if pressure is 0 (sure outlier)
            yield ("temperature", (float(temperature), 1))
            yield ("pressure", (float(pressure), 1))

    def reducer_combiner(self, data, temp_pres):
        avg, count = 0, 0
        for tp, c in temp_pres:
            avg = (avg * count + tp * c) / (count + c)
            count += c
        return data, (avg, count)

    def combiner(self, data, temp_pres):
        yield self.reducer_combiner(data, temp_pres)

    def reducer(self, data, temp_pres):
        data, (avg, count) = self.reducer_combiner(data, temp_pres)
        yield (data, avg)


if __name__ == '__main__':
    Avg.run()


