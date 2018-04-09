import os
import sys

os.system("python averagetest4.py " + sys.argv[1] + " -r hadoop > average.txt")

f = open("average.txt", "r+")

lines = f.readlines()
avg_temp = lines[0].split("\t")[1].strip()
avg_pres = lines[1].split("\t")[1].strip()

os.system("python sdtest4.py " + sys.argv[1] + " -r hadoop > sd.txt")

f = open("sd.txt", "r+")
lines = f.readlines()
sd_temp = lines[0].split("\t")[1].strip()
sd_pres = lines[1].split("\t")[1].strip()

os.system("python avgwo.py " + sys.argv[1] + " --avg-temp " + avg_temp + " --sd-pres " + sd_pres + " --sd-temp " +
          sd_temp + " --avg-pres " + avg_pres + " -r hadoop > avgwo.txt")

os.system("python sdwo.py " + sys.argv[1] + " --avg-pres " + avg_pres + " --avg-temp " + avg_temp +
          " --sd-pres " + sd_pres + " --sd-temp " + sd_temp + " -r hadoop > sdwo.txt")



