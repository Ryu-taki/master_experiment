# Introduction to Data Analysis and Modeling of Biological and Social Systems

## 250606
### Done
* Preserved simulation values in Exercise 1
  * Output:
    * `output/exercise1/simulation_values/[d,i,r,s]_values_baseline.npy`
* Defined common functions in `common_func.py` and modified each file to import and use the necessary functions from it.
* Completed Exercise2
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
* First mtg
* Environment setup
* Completed Exercise 1
  * `experiment1.py`
  * Output:
    * `output/exercise1/four_compartments.png`
    * `output/exercise1/result.txt`

### Todo
* Complete Exercise 2
* Since Exercise 2 uses the results from Exercise 1, I need to modify `experiment1.py` to preserve the values of `i_values`.