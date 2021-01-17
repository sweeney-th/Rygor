from CitationParser import CitationParser
import logging as log

# configure logger
log.basicConfig(
  filename ='rygor.log',
  filemode ='w',
  level=log.INFO,
  format ='%(name)s - %(levelname)s - %(message)s'
)

a = 'Oran, D.P. & Topol, E.J. Prevalence of Asymptomatic SARS-CoV-2 Infection : A Narrative Review. Ann Intern Med 173, 362'
e = 'Havers, F.P. et al. Seroprevalence of Antibodies to SARS-CoV-2 in 10 Sites in the United States, March 23-May 12, 2020. JAMA Intern Med (2020). '
m = 'FDA. EUA Authorized Serology Test Performance. United States Food and Drug Administration https://www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/eua-authorized-serology-test-performance (2020).'
CitationParser.clean('Looi, M.K. Covid-19: Is a second wave hitting Europe? BMJ 371, m4113 (2020).')