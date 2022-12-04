import csv

class GetChunk:
    def __init__(self, file_name):
        self.file_name = file_name

    def check_symbol(self, symbol, text, semantic_parts):
        if symbol in text:
            tmp_semantic_parts = []
            for semantic_part in semantic_parts:
                tmp_semantic_parts += semantic_part.split(symbol)
            semantic_parts = tmp_semantic_parts
        return semantic_parts

    def get_chunk(self):
        with open(self.file_name) as f:
            text = f.read()
        text = text.replace(' ', '').replace('　', '')
        semantic_parts = [text]
        symbols = ['\n', '.', ',', '。', '、', '，', '．']
        
        for symbol in symbols:
            semantic_parts = self.check_symbol(symbol, text, semantic_parts)
        semantic_parts = [semantic_part for semantic_part in semantic_parts if semantic_part != '']
        
        return semantic_parts