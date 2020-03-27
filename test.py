encode = Encode(['a', 'b', 'c'], [0.7, 0.1, 0.2], 3, 'abc')
print(encode.probability_accumulation)
print(encode.calculate_probability())