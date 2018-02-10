from common import configs, constants
from common.datahandler import create_train_test_files
from common.filehandler import read_csv_from_file
from common.experiment import repeat_experiment, analyze_output


def __main__():
    df = read_csv_from_file(configs.INPUT_FOLDER + constants.DATA_FILE_NAME)
    create_train_test_files(df,configs.STAGING_FOLDER,configs.TEST_SET_SIZE,configs.NUMBER_OF_CROSS_VALIDATION_SETS)
    repeat_experiment(configs.STAGING_FOLDER, configs.OUTPUT_FOLDER, configs.NUMBER_OF_CROSS_VALIDATION_SETS)
    analyze_output(configs.OUTPUT_FOLDER, configs.NUMBER_OF_CROSS_VALIDATION_SETS)

__main__()
