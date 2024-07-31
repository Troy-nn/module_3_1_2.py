calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


print(string_info('string'))

def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if i == string:
            return True
    return False
print(string_info('Веселое занятие однако'))
print(string_info('Capybara'))
print(is_contains('string', ['string']))
print(is_contains('string', ['zhora_cudejl_He_Tam']))
print(calls)