from loguru import logger
import sys

logger.remove()

logger.add(
    sys.stderr,
    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "{level:<8} | "
        "{file}:{line} | "
        "{message:<50}"
    ),
    filter=lambda record: "senha" not in record["message"].lower(),
    level="WARNING",
)
logger.add(
    "loguru.txt",
    format="{time:YYYY-MM-DD HH:mm:ss} <r>{level}</r> <g>{message}</g> {file}:{line}",
    filter=lambda record: "senha" not in record["message"].lower(),
    level="WARNING",
)

logger.debug("Entrei aqui")
logger.info("Pessoa X logou")
logger.error("Erro na solicitação")
logger.warning("Algo deu errado")
logger.critical("Senha parou")
