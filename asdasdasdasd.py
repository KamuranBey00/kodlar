import re

fn3TestGirdi = 'Python is a programming language that lets you work quickly and integrate systems more effectively.'
fn3TestParam = ['a*', 'e*']
fn3TestCikti = [['programming', 'language', 'that', 'integrate'], ['lets', 'systems']]

def extract_words(text, patterns):
    result = []
    for pattern in patterns:
        regex_pattern = re.compile(rf'\b\w*{pattern}\w*\b')
        matches = regex_pattern.findall(text)
        matches = [match for match in matches if text.find(match) + len(match) != len(text) and text.find(match) != 0]
        result.append(matches)
    return result

output = extract_words(fn3TestGirdi, fn3TestParam)

print(output)
