from exercises.d_camel_to_kebab import camel_to_kebab

def test_camel_to_kebab_0():
    assert camel_to_kebab('camelCase') == 'camel-case'

def test_camel_to_kebab_1():
    assert camel_to_kebab('CamelCase') == 'camel-case'

def test_camel_to_kebab_2():
    assert camel_to_kebab('camelWithNumber0') == 'camel-with-number-0'

def test_camel_to_kebab_3():
    assert camel_to_kebab('camelWith1AtCenter') == 'camel-with-1-at-center'

def test_camel_to_kebab_4():
    assert camel_to_kebab('camelWithABVT') == 'camel-with-abvt'

def test_camel_to_kebab_5():
    assert camel_to_kebab('camelWithABVTInCenter') == 'camel-with-abvt-in-center'
