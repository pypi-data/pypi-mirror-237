"""
genson:
https://github.com/wolverdude/GenSON
"""
import json
# from genson import SchemaBuilder
# from kuto.utils.log import logger


def formatting(msg):
    """formatted message"""
    if isinstance(msg, dict):
        return json.dumps(msg, indent=2, ensure_ascii=False)
    return msg


# def genSchema(static: dict = None):
#     """
#     return schema static
#     """
#     builder = SchemaBuilder()
#     builder.add_object(static)
#     to_schema = builder.to_schema()
#     to_schema.pop('$schema')
#     logger.debug(f'生成schmea如下:\nschema start-------------->\n{formatting(to_schema)}\nschema end-------------->')
#     return to_schema

