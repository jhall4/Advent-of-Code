# make tests think they're running in code module
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent / "Code"
sys.path[0] = str(codeModulePath)

import DaySixteen

testData = None


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
    expectedValue = [10,20]
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
    expectedValue = [1,2,3]
    value = []
    version, id, _, subPackets, binString = DaySixteen.GetNextPacket(testStr)
    for packet in subPackets:
        (_, _, tValue, _) = packet
        value.append(tValue)
    assert version == expectedVersion
    assert id == expectedId
    assert value == expectedValue


def test_PartOne_16():
    testData = '8A004A801A8002F478'
    providedAnswer = 16
    assert DaySixteen.PartOne(testData) == providedAnswer


def test_PartOne_12():
    testData = '620080001611562C8802118E34'
    providedAnswer = 12
    assert DaySixteen.PartOne(testData) == providedAnswer


def test_PartOne_23():
    testData = 'C0015000016115A2E0802F182340'
    providedAnswer = 23
    assert DaySixteen.PartOne(testData) == providedAnswer


def test_PartOne_31():
    testData = 'A0016C880162017C3686B18A3D4780'
    providedAnswer = 31
    assert DaySixteen.PartOne(testData) == providedAnswer


def test_PartTwo_Sum():
# C200B40A82 finds the sum of 1 and 2, resulting in the value 3.
    testData = 'C200B40A82'
    providedAnswer = 3 
    assert DaySixteen.PartTwo(testData) == providedAnswer


def test_PartTwo_Product():
# 04005AC33890 finds the product of 6 and 9, resulting in the value 54.
    testData = '04005AC33890'
    providedAnswer = 54
    assert DaySixteen.PartTwo(testData) == providedAnswer


def test_PartTwo_Minimum():
# 880086C3E88112 finds the minimum of 7, 8, and 9, resulting in the value 7.
    testData = '880086C3E88112'
    providedAnswer = 7
    assert DaySixteen.PartTwo(testData) == providedAnswer


def test_PartTwo_Maximum():
# CE00C43D881120 finds the maximum of 7, 8, and 9, resulting in the value 9.
    testData = 'CE00C43D881120'
    providedAnswer = 9 
    assert DaySixteen.PartTwo(testData) == providedAnswer


def test_PartTwo_LessThan():
# D8005AC2A8F0 produces 1, because 5 is less than 15.
    testData = 'D8005AC2A8F0'
    providedAnswer = 1
    assert DaySixteen.PartTwo(testData) == providedAnswer


def test_PartTwo_GreaterThan():
# F600BC2D8F produces 0, because 5 is not greater than 15.
    testData = 'F600BC2D8F'
    providedAnswer = 0
    assert DaySixteen.PartTwo(testData) == providedAnswer


def test_PartTwo_Equality():
# 9C005AC2F8F0 produces 0, because 5 is not equal to 15.
    testData = '9C005AC2F8F0'
    providedAnswer = 0
    assert DaySixteen.PartTwo(testData) == providedAnswer


def test_PartTwo_ComplexStatement():
# 9C0141080250320F1802104A08 produces 1, because 1 + 3 = 2 * 2.
    testData = '9C0141080250320F1802104A08'
    providedAnswer = 1
    assert DaySixteen.PartTwo(testData) == providedAnswer





