def compare_seg(file_name1, file_name2, file_name3):
    with open(file_name1) as f1:
        result14 = f1.readlines()
    with open(file_name2) as f2:
        result15 = f2.readlines()
    assert len(result14) == len(result15)
    diff = []
    for i in range(len(result14)):
        if result14[i] != result15[i]:
            diff.append('14:' + result14[i] + '15:' + result15[i])
    print(len(diff), len(result14))
    with open(file_name3) as f3:
        f3.write(''.join(diff))

compare_seg('test_output_11_14.txt', 'test_output_11-15.txt', 'compare_result.txt')
