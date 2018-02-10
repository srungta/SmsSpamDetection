from common.filehandler import ensure_path_exists, read_csv_from_file, write_to_csv, get_file_name
from common import configs, constants
from numpy import random

def create_train_test_files(df,staging_folder, test_set_size=configs.DEFAULT_TEST_SET_SIZE, no_of_validation_sets=configs.DEFAULT_NUMBER_OF_CROSS_VALIDATION_SETS):
    for setindex in range(1,no_of_validation_sets + 1):
        trainset , testset = split_into_train_test(df, test_set_size)
        staging_folder_name = staging_folder + str(setindex)
        ensure_path_exists(staging_folder_name)
        write_to_csv(trainset, get_file_name(staging_folder_name , constants.TRAINING_FILE_NAME))
        write_to_csv(testset, get_file_name(staging_folder_name , constants.TEST_FILE_NAME))

def split_into_train_test(dataframe , percentage=configs.DEFAULT_TEST_SET_SIZE):
    mask = random.rand(len(dataframe)) > percentage
    train = dataframe[mask]
    test = dataframe[~mask]
    return train, test

