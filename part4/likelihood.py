import sys
import os.path
from classes.node import Node
from classes.bayes_net import BayesNet
import xml.etree.ElementTree as ET
import numpy, time, sys

def main():
	if (len(sys.argv) > 1):
		N = int(sys.argv[1])

		network = ET.parse("Cloudy-Rain-Sprinkler-WetGrass-Network.xml")

		bayes_net = BayesNet(network)

		# Find P(C|S,W)
		X = 'C'
		e = ['S', 'W']

		p = []

		M = 1000
		# python main.py  211.93s user 81.52s system 99% cpu 4:53.51 total

		print "----------- Likelihood Weighting Sampling ---------------"
		print "Estimating the probability of P(Cloudy | Sprinkler, Wetgrass)"

		for i in range(0, M):
			p.append(bayes_net.likelihood_weighting(X, e, N))

		arr = numpy.array(p)

		# find the mean
		mean = numpy.mean(arr)

		# find the variance
		variance = numpy.var(arr)

		# find the standard deviation
		std = numpy.std(arr)

		print "---- Summary ----"
		print "N:", N
		print "M:", M
		print "Mean:", mean
		print "Variance:", variance
		print "Standard Deviation:", std
		print ""
	else:
		print "Please provide N."



if __name__ == "__main__":
    main()