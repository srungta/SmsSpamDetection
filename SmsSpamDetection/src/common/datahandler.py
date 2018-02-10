from common.filehandler import ensure_path_exists, read_csv_from_file, write_to_csv
from numpy import random

def create_train_test_files(df,STAGING_FOLDER, TEST_SET_SIZE=0.2, NUMBER_OF_CROSS_VALIDATION_SETS=1):
    for setindex in range(1,NUMBER_OF_CROSS_VALIDATION_SETS + 1):
        trainset , testset = create_train_test_sets(df, TEST_SET_SIZE)
        staging_folder_name = STAGING_FOLDER + str(setindex)
        ensure_path_exists(staging_folder_name)
        write_to_csv(trainset, staging_folder_name + '/train.csv')
        write_to_csv(testset, staging_folder_name + '/test.csv')

def create_train_test_sets(dataframe , percentage=0.2):
    mask = random.rand(len(dataframe)) > percentage
    train = dataframe[mask]
    test = dataframe[~mask]
    return train, test

