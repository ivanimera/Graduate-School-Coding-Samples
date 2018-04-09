from mrjob.job import MRJob


class SDWO(MRJob):
    def configure_args(self):
        super(SDWO, self).configure_args()
        self.add_passthru_arg('--avg-pres', dest='avg_pres', default=4, type=float)
        self.add_passthru_arg('--avg-temp', dest='avg_temp', default=4, type=float)
        self.add_passthru_arg('--sd-temp', dest='sd_temp', default=4, type=float)
        self.add_passthru_arg('--sd-pres', dest='sd_pres', default=4, type=float)

    def mapper(self, _, line):
        timestamps, pressure, temperature = line.split(",")
        sigma = 3
        if temperature != "" and pressure != "" and pressure != "0.0":

            # Filter NA or if pressure is 0 (sure outlier)
            if float(temperature) < (self.options.avg_temp - sigma * self.options.sd_temp) or \
                            float(temperature) > (self.options.avg_temp + sigma * self.options.sd_temp) or \
                            float(pressure) < (self.options.avg_pres - sigma * self.options.sd_pres) or \
                            float(pressure) > (self.options.avg_pres + sigma * self.options.sd_pres):
                yield ("outliers-temperature", (float(temperature),1))
                yield ("outliers-pressure", (float(pressure),1))
            else:
                yield ("temperature", (float(temperature), 1))
                yield ("pressure", (float(pressure), 1))

    def combiner(self, name, temp_pres):
        n, s, s2, max_tp, min_tp = 0, 0.0, 0.0, 0.0, float('inf')
        for tp, c in temp_pres:
            s += tp
            s2 += tp * tp
            n += c
            max_tp = max(max_tp, tp)
            min_tp = min(min_tp, tp)

        yield (name, [s, s2, n, max_tp, min_tp])

    def reducer(self, name, temp_pres):
        sum_n, sum_s, sum_s2, max_max_tp, min_min_tp = 0, 0.0, 0.0, 0.0, float('inf')
        for s, s2, n, max_tp, min_tp in temp_pres:
            sum_n += n
            sum_s += s
            sum_s2 += s2
            max_max_tp = max(max_max_tp, max_tp)
            min_min_tp = min(min_min_tp, min_tp)

        sum_s2 = sum_s2 / sum_n
        sum_s = sum_s / sum_n
        sum_s = sum_s * sum_s
        sd = (sum_s2-sum_s)**0.5
        yield (name, [sd, max_max_tp, min_min_tp, sum_n])


if __name__ == '__main__':
     SDWO.run()
