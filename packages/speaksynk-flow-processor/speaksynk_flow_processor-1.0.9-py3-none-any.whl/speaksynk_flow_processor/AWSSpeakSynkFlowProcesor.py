import boto3
import os
from speaksynk_flow_processor.SpeakSynkFlowProcessor import SpeakSynkFlowProcessor
from speaksynk_flow_processor.utils.utils import createFolder, get_file_path
from speaksynk_flow_processor.constants.constants import (
    WORKING_DIR,
    VIDEO_FILE_NAME,
    S3_BUCKET_NAME,
)


class AWSSpeakSynkFlowProcesor(SpeakSynkFlowProcessor):
    def __init__(self):
        super().__init__()
        self.s3 = boto3.client("s3")
        self.bucket_name = os.environ[S3_BUCKET_NAME]

    def download(self, filekey):
        super().download(filekey)
        filePath = os.path.join(WORKING_DIR, filekey)
        createFolder(os.path.dirname(filePath))
        self._logger.info("Video path: %s, Video Key: %s" % (filePath, filekey))
        self.s3.download_file(self.bucket_name, filekey, filePath)
        self._logger.info("File created")

    def upload(self, filekey, fileName):
        super().upload(filekey, fileName)
        filePath = get_file_path(fileName)
        self._logger.info("Uploading video: %s" % filePath)
        with open(filePath, "rb") as out_handle:
            self._logger.info("Uploading video to: %s" % filekey)
            self.s3.upload_fileobj(out_handle, self.bucket_name, filekey)
            self._logger.info("Finished uploaded video")
