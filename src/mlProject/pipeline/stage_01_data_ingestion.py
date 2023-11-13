from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager() #create instance of ConfigurationManager class
        data_ingestion_config = config.get_data_ingestion_config() #get data from config.yaml
        data_ingestion = DataIngestion(config=data_ingestion_config) #create instance and passing data
        data_ingestion.download_file() #use method to download
        data_ingestion.extract_zip_file() #use method to unzip

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e