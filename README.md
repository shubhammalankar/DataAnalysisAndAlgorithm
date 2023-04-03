# DataAnalysisAndAlgorithm
Algorithms written in python language

**Part 1 -**
  1. Insertion Sort
  2. Merge Sort
  3. Quick Sort
  
  **Implementation -**
  Dierctly import the file in the python interpreter by creating a new project. It will create additional files after running to store the randomly generated arrays of 20, 100, 1000, 4000 elements respectively.
  
  **Output -** 
  This will sort the arrays and will show the output for each algorithm in the below format- 
Total time to sort 20 elements 0
Total time to sort 100 elements 0
Total time to sort 1000 elements 20
Total time to sort 4000 elements 81

The exact output of the programs are also attached in the QuickSortOutput.txt, MergeSortOutput.txt, InsertionSortOutput.txt

Time taken by three different algorithms to sort different number of arrays are mentioned below -
Files	Insertion sort	Merge sort	Quick sort
Arr20.txt	0	0	0
Arr100.txt	7	0	0
Arr1000.txt	131	20	21
Arr4000.txt	2368	81	60


**Part 2 -**
  1. Longest Common Subsequence Brute Force approach (LCS_BF(X,Y))
  2. Longest Common Subsequence Dynamic Programming approach (LCS_DP(X,Y))
  3. Longest Common Subsequence Dynamic Programming approach with b and c arrays (LCS_DP_CB(X,Y))

  **Implementation -**
  We passed LCS1.txt through LCS_BF and LCS_DP and LCS2.txt through LCS_DP_CB
  
  **Output -**<br>
  LCS_DP<br>
  First String : BillBoard<br>
  Second String : BoardBill<br>
  Length of substring 5<br>
  Time taken in execution : 22<br>
  

  LCS_BF<br>
  1st String:BillBoard<br>
  String two: BoardBill<br>
  Length of LCS: 5<br>
  time taken in execution : 0.097900390625<br>
  
  
  LCS_DP_CB<br>
  X =  Bat<br>
  Y =  Boa<br>
  startmilliseconds 1651177682459970000<br>
  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++<br>
    Y B o a<br>
  X 0 0 0 0<br>
  B 0\1<1<1<br>
  a 0^1^1\2<br>
  t 0^1^1^2<br>
  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++<br>
  endmilliseconds 1651177682472060000<br>
  The length of the longest common subsequence is : 2<br>
  The longest common subsequence of " Bat " and " Boa " is " Ba "<br>

All the codes are developed and executed in Pycharm
