from common import constants 
from common.filehandler import ensure_path_exists, read_csv_from_file, write_to_csv, get_file_name

def analyze_output(OUTPUT_FOLDER, NUMBER_OF_CROSS_VALIDATION_SETS):
    for setindex in range(1,NUMBER_OF_CROSS_VALIDATION_SETS + 1):
        output_folder_name = OUTPUT_FOLDER + str(setindex)
        resultset = read_csv_from_file(get_file_name(output_folder_name , constants.OUTPUT_FILE_NAME))
        do_analysis(resultset)

def do_experiment(train_set, test_set):
    result_set = test_set
    return result_set

def do_analysis(result_set):
    None

def repeat_experiment(STAGING_FOLDER, OUTPUT_FOLDER, NUMBER_OF_CROSS_VALIDATION_SETS):
    for setindex in range(1,NUMBER_OF_CROSS_VALIDATION_SETS + 1):
        staging_folder_name = STAGING_FOLDER + str(setindex)
        output_folder_name = OUTPUT_FOLDER + str(setindex)
        ensure_path_exists(output_folder_name)
        trainset = read_csv_from_file(get_file_name(staging_folder_name , constants.TRAINING_FILE_NAME))
        testset = read_csv_from_file(get_file_name(staging_folder_name , constants.TEST_FILE_NAME)) 
        result = do_experiment(trainset,testset)
        write_to_csv(result, get_file_name(output_folder_name , constants.OUTPUT_FILE_NAME))