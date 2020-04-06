def decimal_to_binary(num, precision):
    """
    将十进制（含小数）转换为二进制
    :param num: 十进制数 float
    :param precision: 二进制精确位数 int
    :return: 二进制数 str
    """
    binary = ""
    _int = int(num)
    fractional = num - _int
    while _int:
        rem = _int % 2
        binary += str(rem)
        _int //= 2
    binary = binary[:: -1]
    while precision:
        fractional *= 2
        fract_bit = int(fractional)
        if fract_bit == 1:
            fractional -= fract_bit
            binary += '1'
        else:
            binary += '0'
        precision -= 1
    return binary


def binary_to_decimal(binary):
    """
    将二进制转换为十进制
    :param binary: 二进制 str
    :return: 十进制 float
    """
    decimal = 0
    for i in range(0, len(binary)):
        decimal += int(binary[i]) * pow(2, -i-1)
    return decimal
