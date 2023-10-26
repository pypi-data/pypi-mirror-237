import shortuuid


def generate_string(length: int = 20) -> str:
    generated: str = shortuuid.ShortUUID().random(length=length)
    return generated
