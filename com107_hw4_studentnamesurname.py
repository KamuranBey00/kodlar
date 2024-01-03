# Bir ifade ile başlayan kelimeler tespit edilecek (Words starting with a phrase will be detected)
def fn1(cumle, aramaparam):

    fn1TestGirdi=['You can go faster than 150', 'Dikkatli yolculuk yapın']

    fn1TestParam=['fa+', 'dik+']
    
    fn1TestCikti=['faster', 'Dikkatli']

    test_cikti=[]
    kelimeler = [kelime for cumle in fn1TestGirdi for kelime in cumle.split()]
    result = [item.split('+')[0] if '+' in item else item for item in fn1TestParam]
    for kelime in kelimeler:
        if kelime.startswith(tuple(result)):
            test_cikti.append(kelime)
    return test_cikti

# Bir ifade ile biten kelimeler tespit edilecek (Words ending in a phrase will be detected)
# İfade sadece kelimenin sonunda olabilir. Başında olursa listeye dahil edilmeyecek (The phrase can only be at the end of the word. If it is at the beginning, it will not be included in the list.)
def fn2(cumle, aramaparam):
    an_list = []
    er_list = []
    fn2TestGirdi=['The little boy ran farther than his friends . He played the best of any player . ']
    fn2TestParam=['er.', 'an.']
    fn2TestCikti=[['farther', 'player'], ['ran', 'than']]
    test_cikti= []
    kelimeler =[kelime for cumle in fn2TestGirdi for kelime in cumle.split()]
    result=[item.split(".")[0] if '.' in item else item for item in fn2TestParam]
    for kelime in kelimeler:
        if kelime.endswith(tuple(result)):
            test_cikti.append(kelime)
    for i in test_cikti:
        if i.endswith("er"):
            er_list.append(i)
        else:
            an_list.append(i)
    fin_result = [er_list, an_list]
    print(fin_result)
    return fin_result


# Arama yapılacak ifade kelimelerin ortasında olacak (The phrase to be searched will be in the middle of the words)
# İfadenin başında ve sonunda olduğu durumlar sonuçlara dahil edilmeyecek (Cases where the expression is at the beginning and at the end will not be included in the results)
def fn3(cumle, aramaparam):

    return ""

# ? ifadesi arama yapılacak karakterler arasındaki boşluğu ifade eder (? Expression refers to the space between the characters to be searched.)
# ? iki harfin sırasıyla geçtiği ifade veya ifadeler sonuç olarak döndürülecek (? expression or expressions where two letters occur in sequence will be returned as a result)
def fn4(cumle, aramaparam):
    return ""

# - ifadesi arama yapılacak karakterler arasındaki boşluğu ifade eder (Expression refers to the space between the characters to be searched.)
# - Üç harfin sırasıyla geçtiği ifade veya ifadeler sonuç olarak döndürülecek (The expression or phrases in which three letters occur in sequence will be returned as a result)
def fn5(cumle, aramaparam):
    return ""

sinav_notu = 0

fn1TestGirdi=['You can go faster than 150', 'Dikkatli yolculuk yapın']
fn1TestParam=['fa+', 'dik+']
fn1TestCikti=['faster', 'Dikkatli']

sinav_notu = sinav_notu + 20
for i in range(len(fn1TestGirdi)):
    if (fn1(fn1TestGirdi[i],fn1TestParam[i])!=fn1TestCikti[i]):
        sinav_notu = sinav_notu - 10

print("After 1. question:", sinav_notu)

fn2TestGirdi='The little boy ran farther than his friends . He played the best of any player . '
fn2TestParam=['er.', 'an.']
fn2TestCikti=[['farther', 'player'], ['ran', 'than']]


sinav_notu = sinav_notu + 20
for i in range(len(fn2TestParam)):
    sonuc = fn2(fn2TestGirdi,fn2TestParam[i])
    if (sonuc!=fn2TestCikti[i]):
        sinav_notu = sinav_notu - 10

print("After 2. question:", sinav_notu)

fn3TestGirdi=' Python is a programming language that lets you work quickly and integrate systems more effectively .'
fn3TestParam=['a*', 'e*']
fn3TestCikti=[['programming', 'language', 'that', 'integrate'], ['lets', 'systems']]

sinav_notu = sinav_notu + 20
for i in range(len(fn3TestParam)):
    sonuc = fn3(fn3TestGirdi,fn3TestParam[i])
    if (sonuc!=fn3TestCikti[i]):
        sinav_notu = sinav_notu - 10

print("After 3. question:", sinav_notu)

fn4TestGirdi=' Python is a programming language that lets you work quickly and integrate systems more effectively .'
fn4TestParam=['p?g', 'a?e']
fn4TestCikti=[['Python is a prog'], ['a programming language', 'at le', 'and inte', 'ate']]

sinav_notu = sinav_notu + 20
for i in range(len(fn4TestParam)):
    sonuc = fn4(fn4TestGirdi,fn4TestParam[i])
    if (sonuc!=fn4TestCikti[i]):
        sinav_notu = sinav_notu - 10

print("After 4. question:", sinav_notu)

fn5TestGirdi=' Python is a programming language that lets you work quickly and integrate systems more effectively .'
fn5TestParam=['a-r-n', 'y-o-i']
fn5TestCikti=[['a programmin', 'anguage that lets you work quickly an'], ['ython i', 'you work qui', 'y and integrate systems more effecti']]

sinav_notu = sinav_notu + 20
for i in range(len(fn5TestParam)):
    sonuc = fn5(fn5TestGirdi,fn5TestParam[i])
    if (sonuc!=fn5TestCikti[i]):
        sinav_notu = sinav_notu - 10

print("After 5. question:", sinav_notu)