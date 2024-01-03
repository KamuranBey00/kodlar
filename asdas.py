#def fn2(cumle, aramaparam):
#    fn2TestGirdi=['The little boy ran farther than his friends . He played the best of any player . ']
#    fn2TestParam=['er.', 'an.']
#    fn2TestCikti=[['farther', 'player'], ['ran', 'than']]
#
#    test_cikti= []
#    kelimeler =[kelime for cumle in fn2TestGirdi for kelime in cumle.split()]
#    result=[item.split(".")[0] if '.' in item else item for item in fn2TestParam]
#    for kelime in kelimeler:
#        if kelime.endswith(tuple(result)):
#            test_cikti.append(kelime)    
#    return test_cikti 


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
    return fin_result
print(fn2('The little boy ran farther than his friends . He played the best of any player . ','s.'))