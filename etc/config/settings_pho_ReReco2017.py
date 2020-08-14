#############################################################
########## General settings
#############################################################
# flag to be Tested

#cutpassh2aa = '(\
#        ( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||
#        ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) ||
#        ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f )\
#                )' % (0.913286,0.805013,0.358969)
#myMedium94XV2_abseta = '(\
#                   ( ph_abseta < 1.442\
#                     && ph_hoe < 0.02197\
#                     && ph_sieie < 0.01015\
#                     && ph_chIso < 1.141\
#                     && ph_neuIso < ( 1.189-(-ph_et*0.01512)-(-ph_et*ph_et*0.00002259) )\
#                     && ph_phoIso < ( 2.08-(-ph_et*0.004017) )\
#                   ) ||\
#                   ( ph_abseta > 1.566 && ph_abseta < 2.5\
#                     && ph_hoe < 0.0326\
#                     && ph_sieie < 0.0272\
#                     && ph_chIso < 1.051\
#                     && ph_neuIso < ( 2.718-(-ph_et*0.0117)-(-ph_et*ph_et*0.000023) )\
#                     && ph_phoIso < ( 3.867-(-ph_et*0.0037) )\
#                   )\
#                 )'
#myMedium94XV2 = '(\
#                   ( abs(ph_eta) < 1.442\
#                     && ph_hoe < 0.02197\
#                     && ph_sieie < 0.01015\
#                     && ph_chIso < 1.141\
#                     && ph_neuIso < ( 1.189-(-ph_et*0.01512)-(-ph_et*ph_et*0.00002259) )\
#                     && ph_phoIso < ( 2.08-(-ph_et*0.004017) )\
#                   ) ||\
#                   ( abs(ph_eta) > 1.566 && abs(ph_eta) < 2.5\
#                     && ph_hoe < 0.0326\
#                     && ph_sieie < 0.0272\
#                     && ph_chIso < 1.051\
#                     && ph_neuIso < ( 2.718-(-ph_et*0.0117)-(-ph_et*ph_et*0.000023) )\
#                     && ph_phoIso < ( 3.867-(-ph_et*0.0037) )\
#                   )\
#                 )'
#myMedium94XV2_PU0 = '(\
#                   ( abs(ph_eta) < 1.442\
#                     && ph_hoe < 0.02197\
#                     && ph_sieie < 0.01015\
#                     && max(ph_chIso-(event_rho*0.0112), 0.) < 1.141\
#                     && max(ph_neuIso-(event_rho*0.0668), 0.) < ( 1.189-(-ph_et*0.01512)-(-ph_et*ph_et*0.00002259) )\
#                     && max(ph_phoIso-(event_rho*0.1113), 0.) < ( 2.08-(-ph_et*0.004017) )\
#                   ) ||\
#                   ( abs(ph_eta) > 1.566 && abs(ph_eta) < 2.5\
#                     && ph_hoe < 0.0326\
#                     && ph_sieie < 0.0272\
#                     && ph_chIso < 1.051\
#                     && ph_neuIso < ( 2.718-(-ph_et*0.0117)-(-ph_et*ph_et*0.000023) )\
#                     && ph_phoIso < ( 3.867-(-ph_et*0.0037) )\
#                   )\
#                 )'
#myMedium94XV2_PU0 = '(\
#                   ( abs(ph_eta) < 1.442\
#                     && ph_hoe < 0.02197\
#                     && ph_sieie < 0.01015\
#                     && ( (ph_chIso >= event_rho*0.0112 && ph_chIso < 1.141) || (ph_chIso < event_rho*0.0112) )\
#                     && ( (ph_neuIso >= event_rho*0.0668 && ph_neuIso < (1.189-(-ph_et*0.01512)-(-ph_et*ph_et*0.00002259))) || (ph_neuIso < event_rho*0.0668) )\
#                     && ( (ph_phoIso >= event_rho*0.1113 && ph_phoIso < (2.08-(-ph_et*0.004017))) || (ph_phoIso < event_rho*0.1113) )\
#                   ) ||\
#                   ( abs(ph_eta) > 1.566 && abs(ph_eta) < 2.5\
#                     && ph_hoe < 0.0326\
#                     && ph_sieie < 0.0272\
#                     && ph_chIso < 1.051\
#                     && ph_neuIso < ( 2.718-(-ph_et*0.0117)-(-ph_et*ph_et*0.000023) )\
#                     && ph_phoIso < ( 3.867-(-ph_et*0.0037) )\
#                   )\
#                 )'
#myMedium94XV2_PU1 = '(\
#                   ( abs(ph_eta) < 1.\
#                     && ph_hoe < 0.02197\
#                     && ph_sieie < 0.01015\
#                     && ( (ph_chIso >= event_rho*0.0112 && ph_chIso < 1.141) || (ph_chIso < event_rho*0.0112) )\
#                     && ( (ph_neuIso >= event_rho*0.0668 && ph_neuIso < (1.189-(-ph_et*0.01512)-(-ph_et*ph_et*0.00002259))) || (ph_neuIso < event_rho*0.0668) )\
#                     && ( (ph_phoIso >= event_rho*0.1113 && ph_phoIso < (2.08-(-ph_et*0.004017))) || (ph_phoIso < event_rho*0.1113) )\
#                   ) ||\
#                   ( abs(ph_eta) >= 1. && abs(ph_eta) < 1.479\
#                     && ph_hoe < 0.02197\
#                     && ph_sieie < 0.01015\
#                     && ( (ph_chIso >= event_rho*0.0108 && ph_chIso < 1.141) || (ph_chIso < event_rho*0.0108) )\
#                     && ( (ph_neuIso >= event_rho*0.1054 && ph_neuIso < (1.189-(-ph_et*0.01512)-(-ph_et*ph_et*0.00002259))) || (ph_neuIso < event_rho*0.1054) )\
#                     && ( (ph_phoIso >= event_rho*0.0953 && ph_phoIso < (2.08-(-ph_et*0.004017))) || (ph_phoIso < event_rho*0.0953) )\
#                   ) ||\
#                   ( abs(ph_eta) >= 1.479 && abs(ph_eta) < 2.\
#                     && ph_hoe < 0.0326\
#                     && ph_sieie < 0.0272\
#                     && ( (ph_chIso >= event_rho*0.0106 && ph_chIso < 1.051) || (ph_chIso < event_rho*0.0106) )\
#                     && ( (ph_neuIso >= event_rho*0.0786 && ph_neuIso < (2.718-(-ph_et*0.0117)-(-ph_et*ph_et*0.000023))) || (ph_neuIso < event_rho*0.0786) )\
#                     && ( (ph_phoIso >= event_rho*0.0619 && ph_phoIso < (3.867-(-ph_et*0.0037))) || (ph_phoIso < event_rho*0.0619) )\
#                   ) ||\
#                   ( abs(ph_eta) >= 2. && abs(ph_eta) < 2.2\
#                     && ph_hoe < 0.0326\
#                     && ph_sieie < 0.0272\
#                     && ( (ph_chIso >= event_rho*0.01002 && ph_chIso < 1.051) || (ph_chIso < event_rho*0.01002) )\
#                     && ( (ph_neuIso >= event_rho*0.0233 && ph_neuIso < (2.718-(-ph_et*0.0117)-(-ph_et*ph_et*0.000023))) || (ph_neuIso < event_rho*0.0233) )\
#                     && ( (ph_phoIso >= event_rho*0.0837 && ph_phoIso < (3.867-(-ph_et*0.0037))) || (ph_phoIso < event_rho*0.0837) )\
#                   ) ||\
#                   ( abs(ph_eta) >= 2.2 && abs(ph_eta) < 2.3\
#                     && ph_hoe < 0.0326\
#                     && ph_sieie < 0.0272\
#                     && ( (ph_chIso >= event_rho*0.0098 && ph_chIso < 1.051) || (ph_chIso < event_rho*0.0098) )\
#                     && ( (ph_neuIso >= event_rho*0.0078 && ph_neuIso < (2.718-(-ph_et*0.0117)-(-ph_et*ph_et*0.000023))) || (ph_neuIso < event_rho*0.0078) )\
#                     && ( (ph_phoIso >= event_rho*0.1070 && ph_phoIso < (3.867-(-ph_et*0.0037))) || (ph_phoIso < event_rho*0.1070) )\
#                   ) ||\
#                   ( abs(ph_eta) >= 2.3 && abs(ph_eta) < 2.4\
#                     && ph_hoe < 0.0326\
#                     && ph_sieie < 0.0272\
#                     && ( (ph_chIso >= event_rho*0.0089 && ph_chIso < 1.051) || (ph_chIso < event_rho*0.0089) )\
#                     && ( (ph_neuIso >= event_rho*0.0028 && ph_neuIso < (2.718-(-ph_et*0.0117)-(-ph_et*ph_et*0.000023))) || (ph_neuIso < event_rho*0.0028) )\
#                     && ( (ph_phoIso >= event_rho*0.1212 && ph_phoIso < (3.867-(-ph_et*0.0037))) || (ph_phoIso < event_rho*0.1212) )\
#                   ) ||\
#                   ( abs(ph_eta) >= 2.4\
#                     && ph_hoe < 0.0326\
#                     && ph_sieie < 0.0272\
#                     && ( (ph_chIso >= event_rho*0.0089 && ph_chIso < 1.051) || (ph_chIso < event_rho*0.0089) )\
#                     && ( (ph_neuIso >= event_rho*0.0137 && ph_neuIso < (2.718-(-ph_et*0.0117)-(-ph_et*ph_et*0.000023))) || (ph_neuIso < event_rho*0.0137) )\
#                     && ( (ph_phoIso >= event_rho*0.1466 && ph_phoIso < (3.867-(-ph_et*0.0037))) || (ph_phoIso < event_rho*0.1466) )\
#                   )\
#                 )'


def chgIsoStr(EAchg, chgIso_C1):
    return '( (ph_chIso >= event_rho*%f && ph_chIso < %f) || (ph_chIso < event_rho*%f) )'\
            %(EAchg, chgIso_C1, EAchg)
    #return 'passingCutBasedLoose94XV2PhoAnyPFIsoWithEACut == 1'

def neuIsoStr(EAneu, neuIso_C1, neuIso_C2, neuIso_C3):
    return '( (ph_neuIso >= event_rho*%f && ph_neuIso < (%f-(-ph_et*%f)-(-ph_et*ph_et*%f))) || (ph_neuIso < event_rho*%f) )'\
           %(EAneu, neuIso_C1, neuIso_C2, neuIso_C3, EAneu)
    #return 'passingCutBasedLoose94XV2PhoAnyPFIsoWithEACut1 == 1'

def phoIsoStr(EApho, phoIso_C1, phoIso_C2):
    return '( (ph_phoIso >= event_rho*%f && ph_phoIso < (%f-(-ph_et*%f))) || (ph_phoIso < event_rho*%f) )'\
           %(EApho, phoIso_C1, phoIso_C2, EApho)
    #return 'passingCutBasedLoose94XV2PhoAnyPFIsoWithEAAndQuadScalingCut == 1'

# EB
#hoeCut = 'ph_hoe < 0.04596'
#sieieCut = 'ph_sieie < 0.0106'
hoeCut = 'passingCutBasedLoose94XV2PhoSingleTowerHadOverEmCut == 1'
sieieCut = 'passingCutBasedLoose94XV2PhoFull5x5SigmaIEtaIEtaCut == 1'
chgIso_C1 = 1.694 # absPFChaHadIsoWithEACut_C1
chgIso_C2 = 0. # absPFChaHadIsoWithEACut_C2
neuIso_C1 = 24.032 # absPFNeuHadIsoWithEACut_C1
neuIso_C2 = 0.01512 # absPFNeuHadIsoWithEACut_C2
neuIso_C3 = 0.00002259 # absPFNeuHadIsowithEACut_C3
phoIso_C1 = 2.876 # absPFPhoIsoWithEACut_C1
phoIso_C2 = 0.004017 # absPFPhoIsoWithEACut_C2
neuIsoCut = 'passingCutBasedLoose94XV2PhoAnyPFIsoWithEAAndQuadScalingCut == 1'
phoIsoCut = 'passingCutBasedLoose94XV2PhoAnyPFIsoWithEACut1 == 1'
chgIsoCut = 'passingCutBasedLoose94XV2PhoAnyPFIsoWithEACut == 1'

# 0. <= eta < 1.
etaLow, etaHigh = 0., 1.
EAchg, EAneu, EApho = 0.0112, 0.0668, 0.1113
eta0To1p0 =  '( ph_abseta >= %f && ph_abseta < %f'%(etaLow, etaHigh)\
             +' && '+hoeCut\
             +' && '+sieieCut\
             +' && '+phoIsoCut\
             +' && '+chgIsoStr(EAchg, chgIso_C1)\
             +' && '+neuIsoStr(EAneu, neuIso_C1, neuIso_C2, neuIso_C3)\
             +' && '+phoIsoStr(EApho, phoIso_C1, phoIso_C2)\
             +' )'
             #+' && '+chgIsoCut\
             #+' && '+phoIsoStr(EApho, phoIso_C1, phoIso_C2)

# 1. <= eta < 1.479
etaLow, etaHigh = 1., 1.479
EAchg, EAneu, EApho = 0.0108, 0.1054, 0.0953
eta1p0To1p4 = '( ph_abseta >= %f && ph_abseta < %f'%(etaLow, etaHigh)\
              +' && '+hoeCut\
              +' && '+sieieCut\
              +' && '+phoIsoCut\
              +' && '+chgIsoStr(EAchg, chgIso_C1)\
              +' && '+neuIsoStr(EAneu, neuIso_C1, neuIso_C2, neuIso_C3)\
              +' && '+phoIsoStr(EApho, phoIso_C1, phoIso_C2)\
              +' )'
              #+' && '+chgIsoCut\
              #+' && '+phoIsoStr(EApho, phoIso_C1, phoIso_C2)

# EE
#hoeCut = 'ph_hoe < 0.0590'
#sieieCut = 'ph_sieie < 0.0272'
#hoeCut = 'passingCutBasedLoose94XV2PhoSingleTowerHadOverEmCut == 1'
#sieieCut = 'passingCutBasedLoose94XV2PhoFull5x5SigmaIEtaIEtaCut == 1'
chgIso_C1 = 2.089 # absPFChaHadIsoWithEACut_C1
chgIso_C2 = 0. # absPFChaHadIsoWithEACut_C2
neuIso_C1 = 19.722 # absPFNeuHadIsoWithEACut_C1
neuIso_C2 = 0.0117 # absPFNeuHadIsoWithEACut_C2
neuIso_C3 = 0.000023 # absPFNeuHadIsowithEACut_C3
phoIso_C1 = 4.162 # absPFPhoIsoWithEACut_C1
phoIso_C2 = 0.0037 # absPFPhoIsoWithEACut_C2

# 1.479 <= eta < 2.
etaLow, etaHigh = 1.479, 2.
EAchg, EAneu, EApho = 0.0106, 0.0786, 0.0619
eta1p4To2p0 = '( ph_abseta >= %f && ph_abseta < %f'%(etaLow, etaHigh)\
              +' && '+hoeCut\
              +' && '+sieieCut\
              +' && '+phoIsoCut\
              +' && '+chgIsoStr(EAchg, chgIso_C1)\
              +' && '+neuIsoStr(EAneu, neuIso_C1, neuIso_C2, neuIso_C3)\
              +' && '+phoIsoStr(EApho, phoIso_C1, phoIso_C2)\
              +' )'
              #+' && '+chgIsoCut\
              #+' && '+phoIsoStr(EApho, phoIso_C1, phoIso_C2)

# 2. <= eta < 2.2
etaLow, etaHigh = 2., 2.2
EAchg, EAneu, EApho = 0.01002, 0.0233, 0.0837
eta2p0To2p2 = '( ph_abseta >= %f && ph_abseta < %f'%(etaLow, etaHigh)\
              +' && '+hoeCut\
              +' && '+sieieCut\
              +' && '+phoIsoCut\
              +' && '+chgIsoStr(EAchg, chgIso_C1)\
              +' && '+neuIsoStr(EAneu, neuIso_C1, neuIso_C2, neuIso_C3)\
              +' && '+phoIsoStr(EApho, phoIso_C1, phoIso_C2)\
              +' )'
              #+' && '+chgIsoCut\
              #+' && '+phoIsoStr(EApho, phoIso_C1, phoIso_C2)

# 2.2 <= eta < 2.3
etaLow, etaHigh = 2.2, 2.3
EAchg, EAneu, EApho = 0.0098, 0.0078, 0.1070
eta2p2To2p3 = '( ph_abseta >= %f && ph_abseta < %f'%(etaLow, etaHigh)\
              +' && '+hoeCut\
              +' && '+sieieCut\
              +' && '+phoIsoCut\
              +' && '+chgIsoStr(EAchg, chgIso_C1)\
              +' && '+neuIsoStr(EAneu, neuIso_C1, neuIso_C2, neuIso_C3)\
              +' && '+phoIsoStr(EApho, phoIso_C1, phoIso_C2)\
              +' )'
              #+' && '+chgIsoCut\
              #+' && '+phoIsoStr(EApho, phoIso_C1, phoIso_C2)

# 2.3 <= eta < 2.4
etaLow, etaHigh = 2.3, 2.4
EAchg, EAneu, EApho = 0.0089, 0.0028, 0.1212
eta2p3To2p4 = '( ph_abseta >= %f && ph_abseta < %f'%(etaLow, etaHigh)\
              +' && '+hoeCut\
              +' && '+sieieCut\
              +' && '+phoIsoCut\
              +' && '+chgIsoStr(EAchg, chgIso_C1)\
              +' && '+neuIsoStr(EAneu, neuIso_C1, neuIso_C2, neuIso_C3)\
              +' && '+phoIsoStr(EApho, phoIso_C1, phoIso_C2)\
              +' )'
              #+' && '+chgIsoCut\
              #+' && '+phoIsoStr(EApho, phoIso_C1, phoIso_C2)

# 2.4 <= eta
etaLow = 2.4
EAchg, EAneu, EApho = 0.0087, 0.0137, 0.1466
eta2p4ToInf = '( ph_abseta >= %f'%(etaLow)\
              +' && '+hoeCut\
              +' && '+sieieCut\
              +' && '+phoIsoCut\
              +' && '+chgIsoStr(EAchg, chgIso_C1)\
              +' && '+neuIsoStr(EAneu, neuIso_C1, neuIso_C2, neuIso_C3)\
              +' && '+phoIsoStr(EApho, phoIso_C1, phoIso_C2)\
              +' )'
              #+' && '+chgIsoCut\
              #+' && '+neuIsoCut\

#myMedium94XV2_PU2 = '( '+eta0To1p0\
myLoose94XV2_PU4 = '( '+eta0To1p0\
                    +' || '+eta1p0To1p4\
                    +' || '+eta1p4To2p0\
                    +' || '+eta2p0To2p2\
                    +' || '+eta2p2To2p3\
                    +' || '+eta2p3To2p4\
                    +' || '+eta2p4ToInf+' )'
#cutpassh2aa = '(\
#                   ( ph_hoe < 0.08 ) &&\
#                   ( ph_eta < 1.4 ) &&\
#                   ( ( ph_full5x5x_r9 > 0.5 ) ||\
#                       ( ( ph_full5x5x_r9 > 0.85 ) &&\
#                         ( ph_sieie < 0.015 ) &&\
#                         ( ph_phoIso < 4. ) &&\
#                         ( ph_chIso < 6. )\
#                       )\
#                   )\
#               )'
#cutpassh2aaV1 = '( ph_hoe < 0.08 && ph_full5x5x_r9 > 0.5 )'
#cutpassh2aaV2 = '(\
#cutpassh2aaV3 = '(\
#                     ( ph_chIso/ph_et < 0.05 && ph_mva94XV2 > -0.98 && ph_hoe < 0.08 ) &&\
#                     (\
#                        ( abs(ph_eta) < 1.44 && ph_full5x5x_r9 > 0.5\
#                           && ( ph_full5x5x_r9 > 0.85 || ( ph_sieie < 0.015 && ph_phoIso < 4. && ph_chIso < 6.))) ||\
#                        ( abs(ph_eta) > 1.57 && abs(ph_eta) < 2.5 && ph_full5x5x_r9 > 0.8\
#                           && ( ph_full5x5x_r9 > 0.90 || ( ph_sieie < 0.035 && ph_phoIso < 4. && ph_chIso < 6.)))\
#                     )\
#                 )'
#cutpassh2aaV4 = '(\
#                     ( ph_chIso/ph_et < 0.05 && ph_mva94XV2 > -0.98 && ph_hoe < 0.08 ) &&\
#                     (\
#                        ( abs(ph_eta) < 1.442 && ph_full5x5x_r9 >= 0.5\
#                           && ( ph_full5x5x_r9 > 0.85 || ( ph_full5x5x_r9 <= 0.85 && ph_sieie < 0.015 && ph_phoIso < 4. && ph_chIso < 6.))) ||\
#                        ( abs(ph_eta) >= 1.566 && abs(ph_eta) < 2.5 && ph_full5x5x_r9 >= 0.8\
#                           && ( ph_full5x5x_r9 > 0.90 || ( ph_full5x5x_r9 <= 0.90 && ph_sieie < 0.035 && ph_phoIso < 4. && ph_chIso < 6.)))\
#                     )\
#                 )'
cutpassh2aaV5 = '(\
                     ( ph_chIso/ph_et < 0.05 && ph_mva94XV2 > -0.98 && passingCutBasedLoose94XV2PhoSingleTowerHadOverEmCut == 1 ) &&\
                     (\
                        ( ph_abseta < 1.442 && ph_full5x5x_r9 >= 0.5\
                           && ( ph_full5x5x_r9 > 0.85 || ( ph_full5x5x_r9 <= 0.85 && ph_sieie < 0.015 && ph_phoIso < 4. && ph_chIso < 6.))) ||\
                        ( ph_abseta >= 1.566 && ph_abseta < 2.5 && ph_full5x5x_r9 >= 0.8\
                           && ( ph_full5x5x_r9 > 0.90 || ( ph_full5x5x_r9 <= 0.90 && ph_sieie < 0.035 && ph_phoIso < 4. && ph_chIso < 6.)))\
                     )\
                 )'
# failed:
#cutpassh2aaV3 = '(\
#                   ( abs(ph_eta) < 1.442\
#                     && ph_hoe < 0.08\
#                     && ph_chIso/ph_et < 0.05\
#                     && ph_mva94XV2 > -0.98\
#                     && ph_full5x5x_r9 >= 0.5\
#                     && ( ph_full5x5x_r9 > 0.85 || (ph_sieie < 0.015 && ph_phoIso < 4. && ph_chIso < 6.) )\
#                   ) ||\
#                   ( abs(ph_eta) > 1.566 && abs(ph_eta) < 2.5\
#                     && ph_hoe < 0.08\
#                     && ph_chIso/ph_et < 0.05\
#                     && ph_mva94XV2 > -0.98\
#                     && ph_full5x5x_r9 >= 0.8\
#                     && ( ph_full5x5x_r9 > 0.90 || (ph_sieie < 0.035 && ph_phoIso < 4. && ph_chIso < 6.) )\
#                   )\
#                 )'
#cutpassh2aaV3 = '(\
#                   ( ph_chIso/ph_et < 0.05 && ph_mva94XV2 > -0.98 && ph_hoe < 0.08 )\
#                   && (\
#                        ( abs(ph_eta) < 1.442 && ph_full5x5x_r9 >= 0.5\
#                          && ( ph_full5x5x_r9 > 0.85 || (ph_sieie < 0.015 && ph_phoIso < 4. && ph_chIso < 6.) )\
#                        ) ||\
#                        ( abs(ph_eta) > 1.566 && abs(ph_eta) < 2.5 && ph_full5x5x_r9 >= 0.8\
#                          && ( ph_full5x5x_r9 > 0.90 || (ph_sieie < 0.035 && ph_phoIso < 4. && ph_chIso < 6.) )\
#                        )\
#                      )\
#                 )'

flags = {
#    'passingLoose100XV2'   : '(passingLoose100XV2  == 1)',
#    'passingMedium100XV2'  : '(passingMedium100XV2 == 1)',
#    'passingTight100XV2'   : '(passingTight100XV2  == 1)',
#    'passingMVA94XV2wp80' : '(passingMVA94XV2wp80 == 1)',
#    'passingMVA94XV2wp90' : '(passingMVA94XV2wp90 == 1)',
#    'passingCutBasedLoose94XV2'  : '(passingCutBasedLoose94XV2 == 1)',
#    'passingCutBasedMedium94XV2'  : '(passingCutBasedMedium94XV2 == 1)',
#    'myMedium94XV2'  : myMedium94XV2
#    'myMedium94XV2_abseta_esc'  : myMedium94XV2_abseta_esc
#    'myMedium94XV2_PU2'  : myMedium94XV2_PU2
#    'myLoose94XV2_PU2'  : myLoose94XV2_PU2
#    'myLoose94XV2_PU4'  : myLoose94XV2_PU4
#    'myLoose94XV2_hoe_sieie_c0_c1'  : myLoose94XV2_PU4
#    'myLoose94XV2_chg_neu_pho_cutBased_hoe_sieie'  : myLoose94XV2_PU4
#    'passingh2aa'  : cutpassh2aa
#    'passingh2aaV2'  : cutpassh2aaV2
#    'passingh2aaV3'  : cutpassh2aaV3
    'passingh2aaV5'  : cutpassh2aaV5
    }

baseOutDir = 'results/ReReco2017/tnpPhoID/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'tnpPhoIDs'

samplesDef = {
    'data'   : tnpSamples.ReReco2017['data_Run2017B'].clone(),
    'mcNom'  : tnpSamples.ReReco2017['DY_madgraph'].clone(),
    'mcAlt'  : tnpSamples.ReReco2017['DY_amcatnloext'].clone(),
    'tagSel' : tnpSamples.ReReco2017['DY_madgraph'].clone(),
}
## can add data sample easily
samplesDef['data'].add_sample( tnpSamples.ReReco2017['data_Run2017C'] )
samplesDef['data'].add_sample( tnpSamples.ReReco2017['data_Run2017D'] )
samplesDef['data'].add_sample( tnpSamples.ReReco2017['data_Run2017E'] )
samplesDef['data'].add_sample( tnpSamples.ReReco2017['data_Run2017F'] )

## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
samplesDef['data' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_tnpTree(tnpTreeDir)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_tnpTree(tnpTreeDir)

if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
if not samplesDef['tagSel'] is None:
    samplesDef['tagSel'].rename('mcAltSel_DY_madgraph')
    samplesDef['tagSel'].set_cut('tag_Ele_pt > 37')

## set MC weight, simple way (use tree weight) 
#weightName = 'totWeight'
#if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)

## set MC weight, can use several pileup rw for different data taking 

weightName = 'weights_2017_runBCDEF.totWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree('/eos/cms/store/group/phys_egamma/swmukher/ntuple_2017_v2/PU/DY_madgraph_pho.pu.puTree.root')
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree('/eos/cms/store/group/phys_egamma/swmukher/ntuple_2017_v2/PU/DY_amcatnloext_pho.pu.puTree.root')
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_puTree('/eos/cms/store/group/phys_egamma/swmukher/ntuple_2017_v2/PU/DY_madgraph_pho.pu.puTree.root')



#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
   { 'var' : 'ph_sc_eta' , 'type': 'float', 'bins': [-2.5,-2.0,-1.566,-1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5] },
#   { 'var' : 'ph_sc_eta' , 'type': 'float', 'bins': [-1.4442, -0.8, 0.0, 0.8, 1.4442] },
   { 'var' : 'ph_et' , 'type': 'float', 'bins': [20,35,50,100,200,500] },
]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
#cutBase   = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.17'
cutBase   = '(tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.17)'

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
#additionalCuts = { 
#   0 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#   1 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#   2 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#   3 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#   4 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#   5 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#   6 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#   7 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#   8 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#   9 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#}

#### or remove any additional cut (default)
additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",
    ]

tnpParAltSigFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    ]
     
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "alphaP[0.,-5.,5.]",
    "alphaF[0.,-5.,5.]",
    ]
        
