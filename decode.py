import binary_process


class Decode:
    def __init__(self, input_alphabet: list, input_probability: list, input_length: int, binary_tag):
        """
        初始化解密程序
        :param input_alphabet: 字符表
        :param input_probability: 每个字符出现的概率
        :param input_length: 原信息长度
        :param binary_tag: 二进制加密后的信息
        """
        self.alphabet = input_alphabet
        self.probability = input_probability
        self.length = input_length
        self.tag = binary_process.binary_to_decimal(binary_tag)
        self.probability_accumulation = [0]
        self.generate_probability_accumulation_map()

    def generate_probability_accumulation_map(self):
        """
        将字符表中的每个字符与其累积概率对应，生成一个 list
        """
        f = 0
        for i in range(0, len(self.probability)):
            f += self.probability[i]
            self.probability_accumulation.append(f)

    def interval(self, board):
        for i in range(0, len(self.probability_accumulation) - 1):
            if self.probability_accumulation[i] <= board < self.probability_accumulation[i + 1]:
                return i + 1

    def decode(self):
        tmp_tag = self.tag
        output = ''
        length_remained = self.length
        while length_remained > 0:
            i = self.interval(tmp_tag)
            output = output + self.alphabet[i - 1]
            tmp_tag = (tmp_tag - self.probability_accumulation[i - 1]) / (self.probability_accumulation[i] - self.probability_accumulation[i - 1])
            length_remained -= 1
        return output

