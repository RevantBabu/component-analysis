# component-analysis

> python data_load.py
1. Reads from provided .xlsx files
2. Merges data from all the sheets (using participantId)
3. Removes any rows which contain null values
4. Removes columns which have non-numeric values {or map to numeric?}
5. Normalize df using min_max and mean_std
6. Saves the final normalized df under processed_data/ (in csv & pkl formats)

> python run_pca.py 
1. Loads data saved from earlier step and runs PCA
2. results are stored under results/