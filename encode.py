class Encode:
    def __init__(self, input_alphabet: list, input_probability: list, input_length: int, input_to_be_encoded: str):
        """
        初始化加密程序参数
        :param input_alphabet: 字符表
        :param input_probability: 每个字符出现的概率
        :param input_length: 信息字符长度
        """
        self.alphabet = input_alphabet
        self.probability = input_probability
        self.length = input_length
        self.to_be_encoded = input_to_be_encoded
        self.probability_map = {}
        self.probability_accumulation = [0]
        self.generate_probability_dict()
        self.generate_probability_accumulation_map()

    def generate_probability_dict(self):
        """
        将字符表中的每个字符与其概率对应，生成一个 dict
        """
        for i in range(0, len(self.probability)):
            self.probability_map[self.alphabet[i]] = self.probability[i]

    def generate_probability_accumulation_map(self):
        """
        将字符表中的每个字符与其累积概率对应，生成一个 list
        """
        f = 0
        for i in range(0, len(self.probability)):
            f += self.probability[i]
            self.probability_accumulation.append(f)

    def calculate_probability(self):
        """
        计算输入信息最终的概率区间
        :return: 左区间、右区间
        """
        left = 0
        right = 1
        for i in range(0, len(self.to_be_encoded)):
            k = self.alphabet.index(self.to_be_encoded[i]) + 1
            l_update = left + (right - left) * self.probability_accumulation[k - 1]
            r_update = left + (right - left) * self.probability_accumulation[k]
            left = l_update
            right = r_update
        return left, right
