# component-analysis

### 1. processing data
```sh
$ python data_load.py
```
1. Reads from provided .xlsx files
2. Merges data from all the sheets (using participantId)
3. Removes any rows which contain null values
4. Removes columns which have non-numeric values {or map to numeric?}
5. Normalize df using min_max and mean_std
6. Saves the final normalized df under processed_data/ (in csv & pkl formats)

### 2. run PCA

```sh
$ python run_pca.py [mean|mm]
``` 
1. Loads normalized data saved from earlier step and runs PCA
a. mean -> mean normalized; mm -> min_max normalized
2. Runs PCA using sklearn (also by covariance & eigen computation for comparision)
2. results are stored under results/

### 3. Results 

1. Result of running PCA on standard normalized data shown below
2. Datafram size: 97*130 {97 points/participants, 130 questions/features}
3. Plot of variance explained each component & cumulaitve variance {97 components}


![alt text](https://github.com/RevantBabu/component-analysis/blob/master/results/mean.png?raw=true "PCA results")