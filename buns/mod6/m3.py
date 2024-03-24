import logging
import json


class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        msg = msg.replace('"', '\"')
        return msg, kwargs


class JsonFormatter(logging.Formatter):
    def format(self, record):
        data = {
            "time": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage()
        }
        return json.dumps(data)


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('skillbox_json_messages.log')
handler.setFormatter(JsonFormatter())
logger.addHandler(handler)
json_logger = JsonAdapter(logger, {})

json_logger.info("Message")
json_logger.info(input())