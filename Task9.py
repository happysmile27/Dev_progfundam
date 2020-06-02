my_dict = {
    'id1': {
        'name': 'Bob',
        'area': 'IT'},
    'id2': {
        'name': 'Bob',
        'area': 'IT'},
    'id3': {
        'name': 'Rob',
        'area': 'Healthacre'},
    'id4': {
        'name': 'Julie',
        'area': 'Marketing'}
}
new_dict = {}
for key, value in my_dict.items():
    if value not in new_dict.values():
        new_dict[key] = value
print(new_dict)