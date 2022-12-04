import csv

class GetChunk:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_chunk(self):
        # a = 1/0
        with open(self.file_name) as f:
            text = f.read()
        text = text.replace(' ', '').replace('　', '')
        semantic_parts = [text]
        
        if '\n' in text:
            tmp_semantic_parts = []
            for semantic_part in semantic_parts:
                tmp_semantic_parts += semantic_part.split('\n')
            semantic_parts = tmp_semantic_parts
        if '.' in text:
            tmp_semantic_parts = []
            for semantic_part in semantic_parts:
                tmp_semantic_parts += semantic_part.split('.')
            semantic_parts = tmp_semantic_parts
        if ',' in text:
            tmp_semantic_parts = []
            for semantic_part in semantic_parts:
                tmp_semantic_parts += semantic_part.split(',')
            semantic_parts = tmp_semantic_parts
        if '。' in text:
            tmp_semantic_parts = []
            for semantic_part in semantic_parts:
                tmp_semantic_parts += semantic_part.split('。')
            semantic_parts = tmp_semantic_parts
        if '、' in text:
            tmp_semantic_parts = []
            for semantic_part in semantic_parts:
                tmp_semantic_parts += semantic_part.split('、')
            semantic_parts = tmp_semantic_parts
        if '，' in text:
            tmp_semantic_parts = []
            for semantic_part in semantic_parts:
                tmp_semantic_parts += semantic_part.split('，')
            semantic_parts = tmp_semantic_parts
        if '．' in text:
            tmp_semantic_parts = []
            for semantic_part in semantic_parts:
                tmp_semantic_parts += semantic_part.split('．')
            semantic_parts = tmp_semantic_parts

        semantic_parts = [semantic_part for semantic_part in semantic_parts if semantic_part != '']
        return semantic_parts