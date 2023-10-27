from eralegis import thelemicdate


def test_return_str_in_thelemicdate_now():
    td_now = thelemicdate.now()
    assert 'æræ novæ' in td_now


def test_return_td_inday_quinze_janeiro_2020():
    td_inday_quinze_janeiro_2020 = thelemicdate.in_day(2020, 1, 15, 22, 33)
    assert td_inday_quinze_janeiro_2020 == '☉ in 25º ♑ ☽ in 05º ♎ Dies Mercurii Anno VI:v æræ novæ'


def test_return_td_inday_oito_abril_1905():
    td_inday_onze_abril_1905 = thelemicdate.in_day(1905, 4, 8, 12, 30)
    assert td_inday_onze_abril_1905 == '☉ in 18º ♈ ☽ in 28º ♉ Dies Saturnii Anno I:0 æræ novæ'
