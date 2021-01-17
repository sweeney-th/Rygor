'''
    This is experimental! The citations are are unfortunately loosely structured and
    this is bound to fail on something. For now, I'm going to just clean everything
    the best I can and log each step of the process carefully so any errors should
    be obvious to any used familiar with the titles in question. Hopefully at some
    point *Arxiv papers will have the citations in the XML 
'''

import logging as log

log = log.getLogger(__name__)

def parseAmpersand(s):
    ### example of parsing ampersand citation
    # Oran, D.P. & Topol, E.J. Prevalence of Asymptomatic SARS-CoV-2 Infection : A Narrative Review. Ann Intern Med 173, 362
    tokens = s.split("&")
    # first, we split on the ampersand:
    #> ['Oran, D.P. ', ' Topol, E.J. Prevalence of Asymptomatic SARS-CoV-2 Infection : A Narrative Review. Ann Intern Med 173, 362']
    # now we can grab the second index to get a title with a stray author, and split it on the first comma to remove part of the name
    tokens = tokens[1].split(",", 1)
    #> [' Topol', ' E.J. Prevalence of Asymptomatic SARS-CoV-2 Infection : A Narrative Review. Ann Intern Med 173, 362']
    print(tokens)
    # we split that one the second space
    #> ['', 'E.J.', 'Prevalence of Asymptomatic SARS-CoV-2 Infection : A Narrative Review. Ann Intern Med 173, 362']
    tokens = tokens[1].split(" ", 2)#[-1]
    # the author-free title is the last element in that list
    return tokens[-1]

    # return tokens[1].split(",", 1)[1].split(" ", 2)[-1]

def parseEtAl(s):
    ### example of parsing et al citation
    # Havers, F.P. et al. Seroprevalence of Antibodies to SARS-CoV-2 in 10 Sites in the United States, March 23-May 12, 2020. JAMA Intern Med (2020). 
    # split on 'et al.'
    tokens = s.split("et al.")#[1]
    #> ['Havers, F.P. ', ' Seroprevalence of Antibodies to SARS-CoV-2 in 10 Sites in the United States, March 23-May 12, 2020. JAMA Intern Med (2020). ']
    # the name-free version is everything on the right 
    return tokens[1]

def parseSingleAuthor(s):
    ### example of parsing single-author or inistitutional author
    # FDA. EUA Authorized Serology Test Performance. United States Food and Drug Administration https://www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/eua-authorized-serology-test-performance (2020).
    # or
    # Looi, M.K. Covid-19: Is a second wave hitting Europe? BMJ 371, m4113 (2020).
    # the first step is the same for both but step is conditional on the comma to deal with author first/last
    tokens = s.split(" ", 1)
    #> ['FDA.', 'EUA Authorized Serology Test Performance. United States Food and Drug Administration https://www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/eua-authorized-serology-test-performance (2020).']
    print(tokens)
    # a comma means we have single author, not institution like FDA
    #> Looi, M.K. Covid-19: Is a second wave hitting Europe? BMJ 371, m4113 (2020).
    # which at this point would be
    #> ['Looi,', 'M.K. Covid-19: Is a second wave hitting Europe? BMJ 371, m4113 (2020).']
    if "," in tokens[0]:
        tokens = tokens[1].split(" ", 1)
        #> ['M.K.', 'Covid-19: Is a second wave hitting Europe? BMJ 371, m4113 (2020).']
        # we just want the right of the split
        return tokens[1]
    else:
        # if there is no comma we probably split it in half (as in FDA example) and author free it to the right of the split
        return tokens[1]

        
def clean(s):

    # the clean function works by removing the authors, then removing the journal information, leaving the paper name
    
    # remove the authors is tricky (read: brittle (hopeless?))
    # I attempt this by breaking the citations into 3 types:
    #   ampersand citations
    #   et. al. citations
    #   single author citations
    def removeAuthors(s):
        if "&" in s:
            return parseAmpersand(s)
        elif "et al." in s:
            return parseEtAl(s)
        else: # What could go wrong? Weeeeee!
            return parseSingleAuthor(s)

    # this is much more straightforward - I just remove "?", split after the "." at the end of the name, and get the left side
    def removeJournal(s):
        s = s.replace("?", ".")
        return s.split(".", 1)[0].strip()
    
    log.info('cleaning: \n\t' + s)
    s = removeAuthors(s)
    log.info('Removing authors ->\n\t' + s)
    # s = removeJournal(s)
    # log.info('Removing Journal (final interpretation) ->\n\t' + s)