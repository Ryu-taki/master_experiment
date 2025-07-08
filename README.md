# Introduction to Data Analysis and Modeling of Biological and Social Systems

## 250708
### Done
* Changed the way of saving and loading simulation values.
  * Implemented `save_values_as_pickle` and `load_values_from_pickle` in `common_func.py`
  * Output:
    * `output/exercise1/simulation_values/simulation_values.pkl`
    * `output/exercise2/simulation_values/simulation_values_b[5,6,8].pkl`

* Implemented Exercise 3
  * `exercise3.py`
  * Output:
    * `output/exercise3/result.txt` (edited manually)
  
* Implemented Exercise 4
  * `exercise4.py`
  * Output:
    * `output/exercise4/simulation_values/simulation_values_b[5,6,8,10]_[25,50,100]weeks.pkl`
    * `output/exercise4/utility_values.csv`

### Todo
* Discuss the results of Exercises 2, 3 and 4.
* Complete Exercise 5

## 250606
### Done
* Preserved simulation values in Exercise 1
  * Output:
    * `output/exercise1/simulation_values/[d,i,r,s]_values_baseline.npy`
* Defined common functions in `common_func.py` and modified each file to import and use the necessary functions from it.
* Implemented Exercise 2
  * `exercise2.py`
  * Output:
    * `output/exercise2/four_infection_curves.png`
    * `output/exercise2/total_number_of_[cases,dead].png`
    * `output/exercise2/total_number_of_[cases,dead]_log.png`

### Todo
* Describe the results of Exercise 2 with respect to changes in the b value.
* Complete Exercise 3

## 250605
### Done
* First meeting
* Environment setup
* Completed Exercise 1
  * `experiment1.py`
  * Output:
    * `output/exercise1/four_compartments.png`
    * `output/exercise1/result.txt`

### Todo
* Complete Exercise 2
* Since Exercise 2 uses the results from Exercise 1, I need to modify `experiment1.py` to preserve the values of `i_values`.