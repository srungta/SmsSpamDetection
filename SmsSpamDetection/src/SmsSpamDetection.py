from common import datahandler, filehandler, experiment 

INPUT_FOLDER = './input/'
NUMBER_OF_CROSS_VALIDATION_SETS = 10
STAGING_FOLDER = './staging/'
OUTPUT_FOLDER = './output/'
TEST_SET_SIZE = 0.2

def __main__():
    df = filehandler.read_csv_from_file(INPUT_FOLDER + 'main.csv')
    datahandler.create_train_test_files(df,STAGING_FOLDER,TEST_SET_SIZE,NUMBER_OF_CROSS_VALIDATION_SETS)
    experiment.repeat_experiment(STAGING_FOLDER, OUTPUT_FOLDER, NUMBER_OF_CROSS_VALIDATION_SETS)
    experiment.analyze_output(OUTPUT_FOLDER, NUMBER_OF_CROSS_VALIDATION_SETS)


__main__()
