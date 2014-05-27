Use JavaBayes (available at http://www.cs.cmu.edu/~javabayes/) to construct a small Bayes net modelling the relationship between metastatic cancer, brain tumor, increased total serum calcium, coma and severe headaches. 

Metastatic cancer is a possible cause of a brain tumor and is also an explanation for increased total serum calcium. 

In turn, either of these could explain a patient falling into a coma. Severe headache is also possibly associated with a brain tumor. 

The prior probability of metastatic cancer P(m) is 0.2. 

The conditional probability of increased total serum calcium P(I | M) is: P(i | m) = 0.8 and P(i | ¬m) = 0.2. 

The conditional probability of brain tumor P(B | M) is: P(b | m) = 0.2 and P(b | ¬m) = 0.05. 

The conditional probability of coma P(C | I, B) is: P(c | i, b) = 0.8, P(c | ¬i, b) = 0.8, P(c | i, ¬b) = 0.8 and P(c | ¬i, ¬b) = 0.05. 

The conditional probability of severe headache P(S | B) is P(s | b) = 0.8 and P(s | ¬b) = 0.6.

a) Construct and show the equivalent graphical model.

b) What is the prior probability of coma P(C)?

Posterior distribution:

	probability (  "Coma" ) { //1 variable(s) and 2 values
		table 
			0.47435035514892876	// p(true | evidence )
			0.5256496448510712; 	// p(false | evidence );
	}

c) What is the probability of metastatic cancer given the patient has severe headaches and has not fallen into coma? 

  - Set Coma to observed false.
  - Set Severe_Headache to observed true.
  - Query Metastatic_Cancer.

Posterior distribution:

	probability (  "Metastatic_Cancer" ) { //1 variable(s) and 2 values
		table 
			0.0757614259265982	// p(true | evidence )
			0.9242385740734018; 	// p(false | evidence );
	}


d) What is the Markov blanket of coma? 

In a Bayesian network, the Markov blanket of node A includes its parents, children and the other parents of all of its children.

http://en.wikipedia.org/wiki/Markov_blanket

Brain Tumor and Increased Total Serum Calcium

e) Are increased total serum calcium and brain tumor independent given coma? Explain. 
No. Explaining away. See lecture 11, slide 10

f) What is the probability of fallen into coma given the patient has metastatic cancer? 

  - Set Metastatic_Cancer to observed true.
  - Query Coma.

Posterior distribution:

	probability (  "Coma" ) { //1 variable(s) and 2 values
		table 
			0.5040679804736937	// p(true | evidence )
			0.4959320195263062; 	// p(false | evidence );
	}
