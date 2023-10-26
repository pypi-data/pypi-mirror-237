from dqt.utils.log import logger
from dqt.utils.meta import ResultCode


def alert(data) -> ResultCode:
    logger.info("✅ Done > JIRA")
    return ResultCode.SUCCEEDED
