from aoc_2021.code import DaySixteen
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


test_data = None


def test_HexToBin():
    testStr = 'D2FE28'
    expectedStr = '110100101111111000101000'
    resultStr = DaySixteen.HexToBin(testStr)
    assert resultStr == expectedStr


def test_GetNextPacket_id4():
    testStr = '110100101111111000101000'
    expectedVersion = 6
    expectedId = 4
    expectedValue = 2021
    version, id, value, _, _ = DaySixteen.GetNextPacket(testStr)
    assert version == expectedVersion
    assert id == expectedId
    assert value == expectedValue


def test_GetNextPacket_id6Bitlength():
    testStr = '00111000000000000110111101000101001010010001001000000000'
    expectedVersion = 1
    expectedId = 6
    expectedValue = [10, 20]
    value = []
    version, id, _, subPackets, binString = DaySixteen.GetNextPacket(testStr)
    for packet in subPackets:
        (_, _, tValue, _) = packet
        value.append(tValue)
    assert version == expectedVersion
    assert id == expectedId
    assert value == expectedValue


def test_GetNextPacket_id6NumPackets():
    testStr = '11101110000000001101010000001100100000100011000001100000'
    expectedVersion = 7
    expectedId = 3
    expectedValue = [1, 2, 3]
    value = []
    version, id, _, subPackets, binString = DaySixteen.GetNextPacket(testStr)
    for packet in subPackets:
        (_, _, tValue, _) = packet
        value.append(tValue)
    assert version == expectedVersion
    assert id == expectedId
    assert value == expectedValue


def test_part_one_16():
    test_data = '8A004A801A8002F478'
    provided_answer = 16
    assert DaySixteen.part_one(test_data) == provided_answer


def test_part_one_12():
    test_data = '620080001611562C8802118E34'
    provided_answer = 12
    assert DaySixteen.part_one(test_data) == provided_answer


def test_part_one_23():
    test_data = 'C0015000016115A2E0802F182340'
    provided_answer = 23
    assert DaySixteen.part_one(test_data) == provided_answer


def test_part_one_31():
    test_data = 'A0016C880162017C3686B18A3D4780'
    provided_answer = 31
    assert DaySixteen.part_one(test_data) == provided_answer


def test_part_two_Sum():
    # C200B40A82 finds the sum of 1 and 2, resulting in the value 3.
    test_data = 'C200B40A82'
    provided_answer = 3
    assert DaySixteen.part_two(test_data) == provided_answer


def test_part_two_Product():
    # 04005AC33890 finds the product of 6 and 9, resulting in the value 54.
    test_data = '04005AC33890'
    provided_answer = 54
    assert DaySixteen.part_two(test_data) == provided_answer


def test_part_two_Minimum():
    # 880086C3E88112 finds the minimum of 7, 8, and 9, resulting in the value 7.
    test_data = '880086C3E88112'
    provided_answer = 7
    assert DaySixteen.part_two(test_data) == provided_answer


def test_part_two_Maximum():
    # CE00C43D881120 finds the maximum of 7, 8, and 9, resulting in the value 9.
    test_data = 'CE00C43D881120'
    provided_answer = 9
    assert DaySixteen.part_two(test_data) == provided_answer


def test_part_two_LessThan():
    # D8005AC2A8F0 produces 1, because 5 is less than 15.
    test_data = 'D8005AC2A8F0'
    provided_answer = 1
    assert DaySixteen.part_two(test_data) == provided_answer


def test_part_two_GreaterThan():
    # F600BC2D8F produces 0, because 5 is not greater than 15.
    test_data = 'F600BC2D8F'
    provided_answer = 0
    assert DaySixteen.part_two(test_data) == provided_answer


def test_part_two_Equality():
    # 9C005AC2F8F0 produces 0, because 5 is not equal to 15.
    test_data = '9C005AC2F8F0'
    provided_answer = 0
    assert DaySixteen.part_two(test_data) == provided_answer


def test_part_two_ComplexStatement():
    # 9C0141080250320F1802104A08 produces 1, because 1 + 3 = 2 * 2.
    test_data = '9C0141080250320F1802104A08'
    provided_answer = 1
    assert DaySixteen.part_two(test_data) == provided_answer
