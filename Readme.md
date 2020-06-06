# MRR (Mean Reciprocal Rank)
(1) Based the current item, generate the next item candidate list. The number of the items on the list is determined by X, which is a parameter of MRR, expressed as MRR(X) or MRR@X. Candidate items are ranked according to probability from high to low.  
(2) Find the location of the next item (i) on the list of candidate items. Calculate the reciprocal of the position, and record as ri.  
(3) The result of MRR@X is (r1+r2+...+rn)/n  

# HR (Hit Rate)
(1) Similar to the first step of MRR. But it does not require the candidate list to be sorted.  
(2) Find whether the next item (i) is on the list. If it is on the list, score, hi, is recorded as 1, otherwise it is 0.  
(3) The result of HR@X is (h1+h2+...+hn)/n  

# P (Precision)
(1) Firstly, we need to be clear about the purpose of the recommendation.  
(2) Secondly, I think we should have a set of next items (Tset) based on the current one to test the algorithm, which is different from the MRR and HR.  
(3) Then, using the algorithm to generate the candidate list (Cset). The length of the list can also determined by the parameter of Precision, expressed as P(X), P@X or Precision@X.  
(4) Finally, the result of P@X is len(Tset&Cset)/X, which means that how many of the recommendations we make are relevant to the customers.  

# R (Recall)
(1) Similar to Precision, the purpose of the recommendation should be built first.  
(2) Then, for session-based recommendation, the set of next items from the test dataset is all of the relevant items for Recall calculation. The number of it can be recorded as Nr.  
(3) Based on the analysis of Precision, the result of R@X is len(Tset&Cset)/Nr  
(4) For other recommendation applications, it may be difficult to know the number of the whole relevant items, which is important for calculating R@X.  

# MAP (Mean Average Precision)
(1) Firstly, AP stands for average precision. Based on the current items, the target next items can be regarded as a set (Tset). The prediction results can be regarded as another set (Cset), which is sorted based on probability from high to low. Then we can find the location of the matched items in the prediction results. The score of ith matched items, located as the lith elements of the prediction results, can be i/li.  
(2) According to the above analysis, if the number of matched items is N, the result of AP is (1/l1 + 2/l2 + ... + N/lN)/N  
(3) MAP is the mean of different users' AP. For the session-based recommendation, MAP can be calculated by averaging each prediction results.  
