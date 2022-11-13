import pdb

from models.ascent import Ascent
import repositories.ascent_repository as ascent_repo

from models.climber import Climber
import repositories.climber_repository as climber_repo

from models.hill import Hill
import repositories.hill_repository as hill_repo

ascent_repo.delete_all()
climber_repo.delete_all()
hill_repo.delete_all()

climber_1 = Climber("Fin")
climber_2 = Climber("Kit")
climber_3 = Climber("Sky")

climber_repo.save(climber_1)
climber_repo.save(climber_2)
climber_repo.save(climber_3)

hill_1 = Hill("Beinn a' Chlaidheimh", 913.96, "Highland","/static/images/Beinn a' Chlaidheimh.jpeg")
hill_repo.save(hill_1)
hill_2 = Hill("Beinn Dearg", 913.7, "Highland", "/static/images/Beinn Dearg.jpeg")
hill_repo.save(hill_2)
hill_3 = Hill("Sgùrr nan Ceannaichean", 913.43, "Highland", "/static/images/Sgùrr nan Ceannaichean.jpeg")
hill_repo.save(hill_3)
hill_4 = Hill("Sgùrr a' Choire-bheithe", 913.32, "Highland", "/static/images/Sgùrr a' Choire-bheithe.jpeg")
hill_repo.save(hill_4)
hill_5 = Hill("Beinn Bhreac", 912.44, "Perth and Kinross", "/static/images/Bhreac.jpg")
hill_repo.save(hill_5)
hill_6 = Hill("Leathad an Taobhain", 911.7, "Highland/Perth and Kinross", "/static/images/Leathad an Taobhain.jpeg")
hill_repo.save(hill_6)
hill_7 = Hill("The Fara", 911.4, "Highland", "/static/images/The Fara.jpeg")
hill_repo.save(hill_7)
hill_8 = Hill("Foinaven", 911.05, "Highland", "/static/images/Foinaven.jpeg")
hill_repo.save(hill_8)
hill_9 = Hill("Beinn nan Oighreag", 909.6, "Perth and Kinross/Stirling", "/static/images/beinn-nan-oighreag-1.jpeg")
hill_repo.save(hill_9)
hill_10 = Hill("Streap", 909, "Highland")
hill_repo.save(hill_10)
hill_11 = Hill("Meall Buidhe", 908.2, "Argyll and Bute/Perth and Kinross")
hill_repo.save(hill_11)
hill_12 = Hill("Fuar Tholl", 907, "Highland")
hill_repo.save(hill_12)
hill_13 = Hill("Leum Uilleim", 906.5, "Highland")
hill_repo.save(hill_13)
hill_14 = Hill("Beinn Maol Chaluim", 906.3, "Highland")
hill_repo.save(hill_14)
hill_15 = Hill("Beinn Dearg Mòr", 906.28, "Highland")
hill_repo.save(hill_15)
hill_16 = Hill("Ben Tee", 904, "Highland")
hill_repo.save(hill_16)
hill_17 = Hill("Beinn Damh", 903, "Highland")
hill_repo.save(hill_17)
hill_18 = Hill("Ben Vuirich", 903, "Perth and Kinross")
hill_repo.save(hill_18)
hill_19 = Hill("Beinn an Lochain", 901.7, "Argyll and Bute")
hill_repo.save(hill_19)
hill_20 = Hill("Sgùrr an Fhuarain", 901, "Highland")
hill_repo.save(hill_20)
hill_21 = Hill("Beinn Mheadhonach", 900.9, "Perth and Kinross")
hill_repo.save(hill_21)
hill_22 = Hill("Beinn Odhar", 900.8, "Argyll and Bute/Stirling")
hill_repo.save(hill_22)
hill_23 = Hill("Culardoch", 900, "Aberdeenshire")
hill_repo.save(hill_23)
hill_24 = Hill("Aonach Buidhe", 899, "Highland")
hill_repo.save(hill_24)
hill_25 = Hill("Sgùrr nan Eugallt", 897.5, "Highland")
hill_repo.save(hill_25)
hill_26 = Hill("Beinn a' Bhuiridh", 897, "Argyll and Bute")
hill_repo.save(hill_26)
hill_27 = Hill("Beinn Bhàn", 896, "Highland")
hill_repo.save(hill_27)
hill_28 = Hill("Ben Tirran", 896, "Angus")
hill_repo.save(hill_28)
hill_29 = Hill("Ruadh-stac Beag", 896, "Highland")
hill_repo.save(hill_29)
hill_30 = Hill("Gairbeinn", 895.5, "Highland")
hill_repo.save(hill_30)
hill_31 = Hill("Creag Mhòr", 895, "Moray")
hill_repo.save(hill_31)
hill_32 = Hill("Beinn a' Chuallaich", 892, "Perth and Kinross")
hill_repo.save(hill_32)
hill_33 = Hill("An Ruadh-stac", 890.4, "Highland")
hill_repo.save(hill_33)
hill_34 = Hill("Beinn Enaiglair", 890, "Highland")
hill_repo.save(hill_34)
hill_35 = Hill("Aonach Shasuinn", 888, "Highland")
hill_repo.save(hill_35)
hill_36 = Hill("Creagan na Beinne", 888, "Perth and Kinross")
hill_repo.save(hill_36)
hill_37 = Hill("Sgùrr Dhòmhnuill", 888, "Highland")
hill_repo.save(hill_37)
hill_38 = Hill("Ben Aden", 887, "Highland")
hill_repo.save(hill_38)
hill_39 = Hill("Meall a' Ghiubhais", 887, "Highland")
hill_repo.save(hill_39)
hill_40 = Hill("Beinn a' Chaisteil", 886, "Argyll and Bute/Perth and Kinross")
hill_repo.save(hill_40)
hill_41 = Hill("Buidhe Bheinn", 885.5, "Highland")
hill_repo.save(hill_41)
hill_42 = Hill("Garbh Bheinn", 885, "Highland")
hill_repo.save(hill_42)
hill_43 = Hill("Cam Chreag", 884, "Argyll and Bute/Perth and Kinross/Stirling")
hill_repo.save(hill_43)
hill_44 = Hill("The Cobbler", 884, "Argyll and Bute")
hill_repo.save(hill_44)
hill_45 = Hill("Beinn Odhar Bheag", 883.3, "Highland")
hill_repo.save(hill_45)
hill_46 = Hill("Stob Dubh", 883, "Highland")
hill_repo.save(hill_46)
hill_47 = Hill("Rois-Bheinn", 882, "Highland")
hill_repo.save(hill_47)
hill_48 = Hill("Beinn Chùirn", 880, "Argyll and Bute/Stirling")
hill_repo.save(hill_48)
hill_49 = Hill("Sgurr Mhurlagain", 880, "Highland")
hill_repo.save(hill_49)
hill_50 = Hill("Ben Ledi", 879, "Stirling")
hill_repo.save(hill_50)
hill_51 = Hill("Creag Uchdag", 879, "Perth and Kinross/Stirling")
hill_repo.save(hill_51)
hill_52 = Hill("Fraochaidh", 879, "Argyll and Bute/Highland")
hill_repo.save(hill_52)
hill_53 = Hill("Sguman Coinntich", 879, "Highland")
hill_repo.save(hill_53)
hill_54 = Hill("Sgurr a' Mhuilinn", 878.8, "Highland")
hill_repo.save(hill_54)
hill_55 = Hill("Càrn an Fhreiceadain", 878, "Highland")
hill_repo.save(hill_55)
hill_56 = Hill("A' Chaoirnich", 875, "Highland")
hill_repo.save(hill_56)
hill_57 = Hill("Baosbheinn", 875, "Highland")
hill_repo.save(hill_57)
hill_58 = Hill("Goat Fell", 875, "North Ayrshire")
hill_repo.save(hill_58)
hill_59 = Hill("Sgùrr na Ba Glaise", 874, "Highland")
hill_repo.save(hill_59)
hill_60 = Hill("Ben Hee", 873, "Highland")
hill_repo.save(hill_60)
hill_61 = Hill("Morven", 872, "Aberdeenshire")
hill_repo.save(hill_61)
hill_62 = Hill("Sgorr nan Lochan Uaine", 871, "Highland")
hill_repo.save(hill_62)
hill_63 = Hill("Stob a' Choin", 869, "Stirling")
hill_repo.save(hill_63)
hill_64 = Hill("Faochaig", 868, "Highland")
hill_repo.save(hill_64)
hill_65 = Hill("Bidein a' Chabair", 867.5, "Highland")
hill_repo.save(hill_65)
hill_66 = Hill("Beinn Pharlagain", 867.3, "Perth and Kinross")
hill_repo.save(hill_66)
hill_67 = Hill("Garbh Bheinn", 867, "Highland")
hill_repo.save(hill_67)
hill_68 = Hill("Càrn a' Choire Ghairbh", 865, "Highland")
hill_repo.save(hill_68)
hill_69 = Hill("Conachcraig", 865, "Aberdeenshire")
hill_repo.save(hill_69)
hill_70 = Hill("Beinn Mhic Chasgaig", 864, "Highland")
hill_repo.save(hill_70)
hill_71 = Hill("Beinn Tharsuinn", 863, "Highland")
hill_repo.save(hill_71)
hill_72 = Hill("Creag an Dail Bheag", 863, "Aberdeenshire")
hill_repo.save(hill_72)
hill_73 = Hill("Sgùrr na Feartaig", 863, "Highland")
hill_repo.save(hill_73)
hill_74 = Hill("Beinn a' Bhathaich Àrd", 862, "Highland")
hill_repo.save(hill_74)
hill_75 = Hill("Cam Chreag", 862, "Perth and Kinross")
hill_repo.save(hill_75)
hill_76 = Hill("Meall na h-Aisre", 862, "Highland")
hill_repo.save(hill_76)
hill_77 = Hill("Beinn Luibhean", 859.7, "Argyll and Bute")
hill_repo.save(hill_77)
hill_78 = Hill("Morrone", 859.5, "Aberdeenshire")
hill_repo.save(hill_78)
hill_79 = Hill("Beinn Lair", 859, "Highland")
hill_repo.save(hill_79)
hill_80 = Hill("Caisteal Abhail", 859, "North Ayrshire")
hill_repo.save(hill_80)
hill_81 = Hill("Fraoch Bheinn", 857.3, "Highland")
hill_repo.save(hill_81)
hill_82 = Hill("Beinn a' Chrulaiste", 857, "Highland")
hill_repo.save(hill_82)
hill_83 = Hill("Càrn Dearg Mòr", 857, "Highland")
hill_repo.save(hill_83)
hill_84 = Hill("Cruach Innse", 857, "Highland")
hill_repo.save(hill_84)
hill_85 = Hill("Beinn a' Chaisgein Mòr", 856, "Highland")
hill_repo.save(hill_85)
hill_86 = Hill("Beinn an Eoin", 855, "Highland")
hill_repo.save(hill_86)
hill_87 = Hill("Beinn Bhuidhe", 855, "Highland")
hill_repo.save(hill_87)
hill_88 = Hill("Stob an Aonaich Mhòir", 855, "Perth and Kinross")
hill_repo.save(hill_88)
hill_89 = Hill("Creach Bheinn", 853, "Highland")
hill_repo.save(hill_89)
hill_90 = Hill("Meall an t-Seallaidh", 852, "Stirling")
hill_repo.save(hill_90)
hill_91 = Hill("Bac an Eich", 849, "Highland")
hill_repo.save(hill_91)
hill_92 = Hill("Beinn nan Imirean", 849, "Stirling")
hill_repo.save(hill_92)
hill_93 = Hill("Cùl Mòr", 849, "Highland")
hill_repo.save(hill_93)
hill_94 = Hill("Sgùrr Ghiubhsachain", 849, "Highland")
hill_repo.save(hill_94)
hill_95 = Hill("Ben Donich", 847, "Argyll and Bute")
hill_repo.save(hill_95)
hill_96 = Hill("Canisp", 847, "Highland")
hill_repo.save(hill_96)
hill_97 = Hill("Beinn Resipol", 845, "Highland")
hill_repo.save(hill_97)
hill_98 = Hill("Merrick", 843, "Dumfries and Galloway")
hill_repo.save(hill_98)
hill_99 = Hill("Ben Vrackie", 842, "Perth and Kinross")
hill_repo.save(hill_99)
hill_100 = Hill("Càrn Bàn", 842, "Highland")
hill_repo.save(hill_100)
hill_101 = Hill("Beinn Mholach", 841.7, "Perth and Kinross")
hill_repo.save(hill_101)
hill_102 = Hill("Sgùrr an Airgid", 841.2, "Highland")
hill_repo.save(hill_102)
hill_103 = Hill("Ben Rinnes", 841, "Moray")
hill_repo.save(hill_103)
hill_104 = Hill("Beinn Udlaidh", 840.4, "Argyll and Bute")
hill_repo.save(hill_104)
hill_105 = Hill("Broad Law", 840.1, "Scottish Borders")
hill_repo.save(hill_105)
hill_106 = Hill("Beinn Trilleachan", 840, "Argyll and Bute/Highland")
hill_repo.save(hill_106)
hill_107 = Hill("Càrn Chuinneag", 839, "Highland")
hill_repo.save(hill_107)
hill_108 = Hill("Sgùrr Gaorsaic", 839, "Highland")
hill_repo.save(hill_108)
hill_109 = Hill("Meallan nan Uan", 838.3, "Highland")
hill_repo.save(hill_109)
hill_110 = Hill("Meall na h-Eilde", 837.2, "Highland")
hill_repo.save(hill_110)
hill_111 = Hill("Sgùrr Cos na Breachd-laoidh", 835, "Highland")
hill_repo.save(hill_111)
hill_112 = Hill("Sròn a' Choire Chnapanich", 835, "Perth and Kinross")
hill_repo.save(hill_112)
hill_113 = Hill("Càrn Dearg", 834, "Highland")
hill_repo.save(hill_113)
hill_114 = Hill("Creag nan Gabhar", 834, "Aberdeenshire")
hill_repo.save(hill_114)
hill_115 = Hill("Beinn Dearg", 830, "Perth and Kinross")
hill_repo.save(hill_115)
hill_116 = Hill("Brown Cow Hill", 829, "Aberdeenshire")
hill_repo.save(hill_116)
hill_117 = Hill("Càrn Mòr", 829, "Highland")
hill_repo.save(hill_117)
hill_118 = Hill("An Dùn", 827.4, "Highland/Perth and Kinross")
hill_repo.save(hill_118)
hill_119 = Hill("Beinn Tarsuinn", 826, "North Ayrshire")
hill_repo.save(hill_119)
hill_120 = Hill("Geal-chàrn Mòr", 824, "Highland")
hill_repo.save(hill_120)
hill_121 = Hill("Benvane", 821, "Stirling")
hill_repo.save(hill_121)
hill_122 = Hill("Geal Chàrn", 821, "Highland")
hill_repo.save(hill_122)
hill_123 = Hill("White Coomb", 821, "Dumfries and Galloway")
hill_repo.save(hill_123)
hill_124 = Hill("Beinn Dearg Bheag", 820, "Highland")
hill_repo.save(hill_124)
hill_125 = Hill("Beinn Chaorach", 818, "Argyll and Bute/Stirling")
hill_repo.save(hill_125)
hill_126 = Hill("Càrn na Drochaide", 818, "Aberdeenshire")
hill_repo.save(hill_126)
hill_127 = Hill("Sgorr na Diollaid", 818, "Highland")
hill_repo.save(hill_127)
hill_128 = Hill("Càrn a' Chuilinn", 817, "Highland")
hill_repo.save(hill_128)
hill_129 = Hill("Càrn Dearg", 817, "Highland")
hill_repo.save(hill_129)
hill_130 = Hill("Stob Coire Creagach", 817, "Argyll and Bute")
hill_repo.save(hill_130)
hill_131 = Hill("Breabag", 815, "Highland")
hill_repo.save(hill_131)
hill_132 = Hill("An Sìthean", 814, "Highland")
hill_repo.save(hill_132)
hill_133 = Hill("An Stac", 814, "Highland")
hill_repo.save(hill_133)
hill_134 = Hill("Corserine", 814, "Dumfries and Galloway")
hill_repo.save(hill_134)
hill_135 = Hill("Beinn Each", 813, "Stirling")
hill_repo.save(hill_135)
hill_136 = Hill("Sgor Mòr", 813, "Aberdeenshire")
hill_repo.save(hill_136)
hill_137 = Hill("Askival", 812, "Highland")
hill_repo.save(hill_137)
hill_138 = Hill("Càrn na Saobhaidhe", 811.1, "Highland")
hill_repo.save(hill_138)
hill_139 = Hill("Creach Bheinn", 810, "Argyll and Bute")
hill_repo.save(hill_139)
hill_140 = Hill("Meall a' Bhuachaille", 810, "Highland")
hill_repo.save(hill_140)
hill_141 = Hill("Meall na Fearna", 809, "Perth and Kinross")
hill_repo.save(hill_141)
hill_142 = Hill("Quinag - Sail Gharbh", 809, "Highland")
hill_repo.save(hill_142)
hill_143 = Hill("Sgùrr Innse", 809, "Highland")
hill_repo.save(hill_143)
hill_144 = Hill("Creag Mac Ranaich", 808.6, "Stirling")
hill_repo.save(hill_144)
hill_145 = Hill("Garbh-bheinn", 808, "Highland")
hill_repo.save(hill_145)
hill_146 = Hill("Hart Fell", 808, "Dumfries and Galloway/Scottish Borders")
hill_repo.save(hill_146)
hill_147 = Hill("Creag Rainich", 807, "Highland")
hill_repo.save(hill_147)
hill_148 = Hill("Monamenach", 807, "Angus/Perth and Kinross")
hill_repo.save(hill_148)
hill_149 = Hill("Beinn nam Fuaran", 806, "Argyll and Bute/Perth and Kinross")
hill_repo.save(hill_149)
hill_150 = Hill("Ben Gulabin", 806, "Perth and Kinross")
hill_repo.save(hill_150)
hill_151 = Hill("Meall nan Subh", 806, "Perth and Kinross")
hill_repo.save(hill_151)
hill_152 = Hill("Beinn Iaruinn", 805, "Highland")
hill_repo.save(hill_152)
hill_153 = Hill("Beinn na h-Eaglaise", 805, "Highland")
hill_repo.save(hill_153)
hill_154 = Hill("Càrn Mòr", 804, "Aberdeenshire/Moray")
hill_repo.save(hill_154)
hill_155 = Hill("Geal Chàrn", 804, "Highland")
hill_repo.save(hill_155)
hill_156 = Hill("The Sow of Atholl", 803, "Perth and Kinross")
hill_repo.save(hill_156)
hill_157 = Hill("Beinn Bhreac-liath", 802, "Argyll and Bute")
hill_repo.save(hill_157)
hill_158 = Hill("Cranstackie", 801, "Highland")
hill_repo.save(hill_158)
hill_159 = Hill("Meallan Liath Coire Mhic Dhùghaill", 801, "Highland")
hill_repo.save(hill_159)
hill_160 = Hill("An Cliseam", 799, "Na h-Eileanan Siar")
hill_repo.save(hill_160)
hill_161 = Hill("Am Bàthach", 798.1, "Highland")
hill_repo.save(hill_161)
hill_162 = Hill("Cìr Mhòr", 798.1, "North Ayrshire")
hill_repo.save(hill_162)
hill_163 = Hill("Beinn Dronaig", 797, "Highland")
hill_repo.save(hill_163)
hill_164 = Hill("Cairnsmore of Carsphairn", 797, "Dumfries and Galloway")
hill_repo.save(hill_164)
hill_165 = Hill("Beinn Bhàn", 796, "Highland")
hill_repo.save(hill_165)
hill_166 = Hill("Beinn Mhic-Mhonaidh", 796, "Argyll and Bute")
hill_repo.save(hill_166)
hill_167 = Hill("Mam na Gualainn", 796, "Highland")
hill_repo.save(hill_167)
hill_168 = Hill("Sgùrr an Utha", 796, "Highland")
hill_repo.save(hill_168)
hill_169 = Hill("Sgùrr Coire Choinnichean", 796, "Highland")
hill_repo.save(hill_169)
hill_170 = Hill("Beinn Airigh Charr", 792, "Highland")
hill_repo.save(hill_170)
hill_171 = Hill("Beinn Leoid", 792, "Highland")
hill_repo.save(hill_171)
hill_172 = Hill("Càrn Ealasaid", 792, "Aberdeenshire/Moray")
hill_repo.save(hill_172)
hill_173 = Hill("Glas Bheinn", 792, "Highland")
hill_repo.save(hill_173)
hill_174 = Hill("Sgùrr a' Chaorachain", 792, "Highland")
hill_repo.save(hill_174)
hill_175 = Hill("Auchnafree Hill", 789, "Perth and Kinross")
hill_repo.save(hill_175)
hill_176 = Hill("Beinn Loinne", 789, "Highland")
hill_repo.save(hill_176)
hill_177 = Hill("Meall Dubh", 789, "Highland")
hill_repo.save(hill_177)
hill_178 = Hill("The Brack", 787.5, "Argyll and Bute")
hill_repo.save(hill_178)
hill_179 = Hill("Arkle", 787, "Highland")
hill_repo.save(hill_179)
hill_180 = Hill("Beinn a' Chaisteil", 787, "Highland")
hill_repo.save(hill_180)
hill_181 = Hill("Meall Tàirneachan", 787, "Perth and Kinross")
hill_repo.save(hill_181)
hill_182 = Hill("Càrn na Nathrach", 786, "Highland")
hill_repo.save(hill_182)
hill_183 = Hill("Beinn an Òir", 785, "Argyll and Bute")
hill_repo.save(hill_183)
hill_184 = Hill("Beinn na Caillich", 785, "Highland")
hill_repo.save(hill_184)
hill_185 = Hill("Beinn Mhic Ceididh", 783, "Highland")
hill_repo.save(hill_185)
hill_186 = Hill("Farragon Hill", 782.4, "Perth and Kinross")
hill_repo.save(hill_186)
hill_187 = Hill("Sgùrr Dubh", 782, "Highland")
hill_repo.save(hill_187)
hill_188 = Hill("Ainshval", 781, "Highland")
hill_repo.save(hill_188)
hill_189 = Hill("Corryhabbie Hill", 781, "Moray")
hill_repo.save(hill_189)
hill_190 = Hill("Beinn Bheula", 779, "Argyll and Bute")
hill_repo.save(hill_190)
hill_191 = Hill("Sgùrr Mhic Bharraich", 779, "Highland")
hill_repo.save(hill_191)
hill_192 = Hill("Meall nam Maigheach", 778.9, "Perth and Kinross")
hill_repo.save(hill_192)
hill_193 = Hill("Mount Battock", 778, "Aberdeenshire/Angus")
hill_repo.save(hill_193)
hill_194 = Hill("Meall na Leitreach", 777.1, "Perth and Kinross")
hill_repo.save(hill_194)
hill_195 = Hill("Meall Horn", 777, "Highland")
hill_repo.save(hill_195)
hill_196 = Hill("Glas Bheinn", 776, "Highland")
hill_repo.save(hill_196)
hill_197 = Hill("Quinag - Sàil Gorm", 776, "Highland")
hill_repo.save(hill_197)
hill_198 = Hill("Glamaig - Sgùrr Mhàiri", 775, "Highland")
hill_repo.save(hill_198)
hill_199 = Hill("Sgorr Craobh a' Chaorainn", 775, "Highland")
hill_repo.save(hill_199)
hill_200 = Hill("Shalloch on Minnoch", 774.2, "South Ayrshire")
hill_repo.save(hill_200)
hill_201 = Hill("Beinn nan Caorach", 774, "Highland")
hill_repo.save(hill_201)
hill_202 = Hill("Beinn Spionnaidh", 773, "Highland")
hill_repo.save(hill_202)
hill_203 = Hill("Meall a' Phubuill", 772.7, "Highland")
hill_repo.save(hill_203)
hill_204 = Hill("Meall Lighiche", 772, "Highland")
hill_repo.save(hill_204)
hill_205 = Hill("Beinn Stacach", 771.8, "Stirling")
hill_repo.save(hill_205)
hill_206 = Hill("Stob Coire a' Chearcaill", 771, "Highland")
hill_repo.save(hill_206)
hill_207 = Hill("Druim Tarsuinn", 770, "Highland")
hill_repo.save(hill_207)
hill_208 = Hill("Cùl Beag", 769.4, "Highland")
hill_repo.save(hill_208)
hill_209 = Hill("Meallach Mhòr", 769, "Highland")
hill_repo.save(hill_209)
hill_210 = Hill("Beinn a' Chòin", 768.7, "Argyll and Bute/Stirling")
hill_repo.save(hill_210)
hill_211 = Hill("Càrn Dearg", 768, "Highland")
hill_repo.save(hill_211)
hill_212 = Hill("Sail Mhòr", 767, "Highland")
hill_repo.save(hill_212)
hill_213 = Hill("Beinn Liath Mhòr a' Ghiubhais", 766, "Highland")
hill_repo.save(hill_213)
hill_214 = Hill("Dùn da Ghaoithe", 766, "Argyll and Bute")
hill_repo.save(hill_214)
hill_215 = Hill("Fuar Bheinn", 766, "Highland")
hill_repo.save(hill_215)
hill_216 = Hill("Bràigh nan Uamhachan", 765, "Highland")
hill_repo.save(hill_216)
hill_217 = Hill("Ben Loyal - An Caisteal", 764.2, "Highland")
hill_repo.save(hill_217)
hill_218 = Hill("Meall an Fhudair", 764, "Argyll and Bute")
hill_repo.save(hill_218)
hill_219 = Hill("Quinag - Spidean Coinich", 764, "Highland")
hill_repo.save(hill_219)
hill_220 = Hill("Cnoc Coinnich", 763.5, "Argyll and Bute")
hill_repo.save(hill_220)
hill_221 = Hill("Little Wyvis", 763, "Highland")
hill_repo.save(hill_221)
hill_222 = Hill("Beinn na h-Uamha", 762.4, "Highland")
hill_repo.save(hill_222)

ascent_1 = Ascent('2019-05-31', 'trial ascent desc', climber_1, hill_1)
ascent_repo.save(ascent_1)
ascent_2 = Ascent('2019-05-30', 'trial ascent desc', climber_1, hill_1)
ascent_repo.save(ascent_2)
ascent_3 = Ascent('2019-05-29', 'trial ascent desc', climber_1, hill_1)
ascent_repo.save(ascent_3)
ascent_4 = Ascent('2019-05-28', 'trial ascent desc', climber_1, hill_1)
ascent_repo.save(ascent_4)
ascent_5 = Ascent('2019-05-27', 'trial ascent desc', climber_1, hill_2)
ascent_repo.save(ascent_5)
ascent_6 = Ascent('2019-05-26', 'trial ascent desc', climber_2, hill_1)
ascent_repo.save(ascent_6)
ascent_7 = Ascent('2019-05-25', 'trial ascent desc', climber_2, hill_1)
ascent_repo.save(ascent_7)

print(ascent_repo.climbing_comm_height_alltime())