import Lab2.Lab2 as Lab2

def test_calc_average():
    input = [1 ,2, 3 ]
    result = Lab2.calc_average(input)
    assert result == 2

def test_find_min_max():
    input = [1, 2, 3]
    result = Lab2.find_min_max(input)
    assert result == (1, 3)

def test_calc_median_temperature():
    input = [1, 2, 3]
    result = Lab2.calc_median_temperature(input)
    assert result == 2
