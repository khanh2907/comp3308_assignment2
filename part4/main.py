from classes.node import Node
from classes.bayes_net import BayesNet
import xml.etree.ElementTree as ET

def main():
	network = ET.parse("Cloudy-Rain-Sprinkler-WetGrass-Network.xml")

	bayes_net = BayesNet(network)

	

	

if __name__ == "__main__":
    main()