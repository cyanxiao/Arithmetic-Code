import binary_process


class Encode:
    def __init__(self, input_alphabet: list, input_probability: list, input_to_be_encoded: str):
        """
        初始化加密程序参数
        :param input_alphabet: 字符表
        :param input_probability: 每个字符出现的概率
        :param input_to_be_encoded: 需要加密的信息 str
        """
        self.alphabet = input_alphabet
        self.probability = input_probability
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

    def binary_output(self):
        """
        将十进制小数输出转换为二进制输出
        :return: 二进制 str
        """
        left, right = self.calculate_probability()
        length = 1
        current_outcome = binary_process.binary_to_decimal(binary_process.decimal_to_binary((left + right) / 2, length))
        while not left <= current_outcome < right:
            length += 1
            current_outcome = binary_process.binary_to_decimal(
                binary_process.decimal_to_binary((left + right) / 2, length))
        return binary_process.decimal_to_binary((left + right) / 2, length)
