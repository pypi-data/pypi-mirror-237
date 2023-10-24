import pytest

from alphabet_thief import replace


TEST_TEXTS = [
    '',  # empty case
    'I Have a Dream!',  # English
    'Trời mưa thì phải ở nhà.',  # Vietnamese
    'українська мова',  # Ukrainian
    'ちいさい秋みつけた。',  # Japanese
]

TEST_RESULTS_REPLACED_WITH_EMPTY = [
    '',
    '   !',
    '̛̀ ̛ ̀ ̉ ̛̉ ̀.',
    '̈ ',
    '。',
]

TEST_RESULTS_REPLACED_WITH_SPACE = [
    '',
    '              !',
    '   ̛̀    ̛     ̀    ̉   ̛̉    ̀.',
    '     ̈          ',
    '         。',
]

TEST_RESULTS_REPLACED_WITH_A = [
    '',
    'a aaaa a aaaaa!',
    'aaà̛a aa̛a aaà aaảa ả̛ aaà.',
    'aaaaäaaaaa aaaa',
    'aaaaaaaaa。',
]


@pytest.mark.parametrize(
    'test_text, test_result',
    zip(TEST_TEXTS, TEST_RESULTS_REPLACED_WITH_EMPTY),
)
def test_replaced_with_empty(test_text, test_result):
    result = replace(test_text, '')
    assert result == test_result


@pytest.mark.parametrize(
    'test_text, test_result',
    zip(TEST_TEXTS, TEST_RESULTS_REPLACED_WITH_SPACE),
)
def test_replaced_with_space(test_text, test_result):
    result = replace(test_text, ' ')
    assert result == test_result


@pytest.mark.parametrize(
    'test_text, test_result',
    zip(TEST_TEXTS, TEST_RESULTS_REPLACED_WITH_A),
)
def test_replaced_with_a(test_text, test_result):
    result = replace(test_text, 'a')
    assert result == test_result
