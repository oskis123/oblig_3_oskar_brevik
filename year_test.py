import leap_year


def test_if_divisible_by_4():
    assert leap_year.is_leap_year(4)


def test_if_divisible_by_400():
    assert leap_year.is_leap_year(400)


def test_if_leap_year():
    assert leap_year.is_leap_year(2000)


def test_if_not_leap_year():
    assert not leap_year.is_leap_year(1001)
    assert not leap_year.is_leap_year(1500)
    assert not leap_year.is_leap_year(350)



#test heidaw awdawdadwwdadawadwadwawdwdaawdawd