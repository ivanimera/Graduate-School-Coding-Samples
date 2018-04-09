from mrjob.job import MRJob


class AVGWO(MRJob):
    def configure_args(self):
        super(AVGWO, self).configure_args()
        self.add_passthru_arg('--avg-pres', dest='avg_pres', default=4, type=float)
        self.add_passthru_arg('--avg-temp', dest='avg_temp', default=4, type=float)
        self.add_passthru_arg('--sd-temp', dest='sd_temp', default=4, type=float)
        self.add_passthru_arg('--sd-pres', dest='sd_pres', default=4, type=float)

    def mapper(self, _, line):
        timestamps, pressure, temperature = line.split(",")
        sigma = 1
        if temperature != "" and pressure != "" and pressure != "0.0":

            # Filter NA or if pressure is 0 (sure outlier)
            if float(temperature) < (self.options.avg_temp - sigma * self.options.sd_temp) or \
                            float(temperature) > (self.options.avg_temp + sigma * self.options.sd_temp) or \
                            float(pressure) < (self.options.avg_pres - sigma * self.options.sd_pres) or \
                            float(pressure) > (self.options.avg_pres + sigma * self.options.sd_pres):
                yield ("outliers-temperature", (float(temperature), 1))
                yield ("outliers-pressure", (float(pressure), 1))
            else:
                yield ("temperature", (float(temperature), 1))
                yield ("pressure", (float(pressure), 1))

    def reducer_combiner(self, data, temp_pres):
        avg, count = 0.0, 0
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
    AVGWO.run()
