from loguru import logger
import sys

logger.remove()

logger.add(
    sys.stderr,
    format=(
        "{time:YYYY-MM-DD HH:mm:ss.SSS} | "
        "{level:<8} | "
        "{file}:{line} | "
        "{message:<50}"
    ),
    filter=lambda record: "senha" not in record["message"].casefold(),
    level="DEBUG",
)
logger.add(
    "loguru.txt",
    format=(
        "{time:YYYY-MM-DD HH:mm:ss.SSS} | "
        "{level:<8} | "
        "{file}:{line} | "
        "{message:<50}"
    ),
    filter=lambda record: "senha" not in record["message"].casefold(),
    level="DEBUG",
)

logger.debug("Entrei aqui")
logger.info("Pessoa X logou")
logger.error("Erro na solicitação")
logger.warning("Algo deu errado")
logger.critical("Senha parou")
logger.critical("O sitema parou")
