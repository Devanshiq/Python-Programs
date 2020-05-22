from matplotlib import pyplot as plt
#        China           India
# 2035	1,433,508,888	1,564,570,223	131,061,335	-0.16	0.61
# 2030	1,441,181,813	1,512,985,207	71,803,394	-0.03	0.77
# 2029	1,441,574,218	1,501,462,374	59,888,156	0.00	0.80
# 2028	1,441,555,143	1,489,564,612	48,009,469	0.03	0.83
# 2027	1,441,105,792	1,477,311,590	36,205,798	0.06	0.86
# 2026	1,440,205,376	1,464,726,099	24,520,723	0.10	0.89
# 2025	1,438,835,697	1,451,829,004	12,993,307	0.13	0.92
# 2024	1,436,995,094	1,438,635,367	1,640,273	0.16	0.95
# 2023	1,434,676,116	1,425,158,481	-9,517,635	0.20	0.97
# 2022	1,431,849,651	1,411,415,296	-20,434,355	0.24	1.00
# 2021	1,428,480,534	1,397,423,009	-31,057,525	0.28	1.03
# 2020	1,424,548,266	1,383,197,753	-41,350,513	0.32	1.06
# 2019	1,420,062,022	1,368,737,513	-51,324,509	0.35	1.08
# 2018	1,415,045,928	1,354,051,854	-60,994,074	0.39	1.11
# 2017	1,409,517,397	1,339,180,127	-70,337,270	0.43	1.13
# 2016	1,403,500,365	1,324,171,354	-79,329,011	0.46	1.15
# 2015	1,397,028,553	1,309,053,980	-87,974,573	0.50	1.17
# 2010	1,359,755,102	1,230,980,691	-128,774,411	0.57	1.38
# 2005	1,321,623,490	1,144,118,674	-177,504,816	0.58	1.6
# 2000	1,283,198,970	1,053,050,912	-230,148,058	0.61	1.79
# 1995	1,239,940,004	960,482,795	    -279,457,209	0.89	1.94
# 1990	1,172,445,200	870,133,480	    -302,311,720	1.64	2.10
# 1985	1,070,863,389	781,666,671	    -289,196,718	1.68	2.28
# 1980	993,877,310	    696,783,517	    -297,093,793	1.43	2.33
# 1975	920,945,083	    621,301,720	    -299,643,363	1.92	2.35
# 1970	824,788,457	    553,578,513	    -271,209,944	2.64	2.23
# 1965	722,562,183	    497,702,365	    -224,859,818	2.28	2.10
# 1960	657,686,143	    449,480,608	    -208,205,535	1.56	1.97
# 1955	610,834,396	    409,269,055	    -201,565,341	1.47	1.79


year=[1955, 1960, 1965 , 1970, 1975,1980,1985,1990,1995,2000,2005,2010,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2035]

indiapopu=[0.409,0.449,0.497,0.553,0.621,0.696,0.781,0.870,0.960,1.053,1.144,1.230,1.309,1.324,1.339,1.354,1.368,1.383,1.397,1.411,1.425,1.438,
           1.451,1.464,1.477,1.489,1.501,1.512,1.564]
chinapopu=[0.610,0.657,0.722,0.824,0.920,0.993,1.070,1.172,1.239,1.283,1.321,1.359,1.397,1.403,1.409,1.415,1.420,1.424,1.428,1.431,1.434,1.436,1.438,
           1.440,1.441,1.441,1.441,1.441,1.443]
print(plt.style.available)
plt.style.use('ggplot')
# plt.xkcd()          #handdrawn
# plt.plot(year,indiapopu,'o--g',marker='o',linestyle='-',color='g',linewidth='3', label='India') #formats are '-'(default that is solid), '--'(dashed), ':'(colon0), '-.'(dashed dotted)
# plt.plot(year,chinapopu, label='China') #color can be written in hex color and teh whole string and in starting letter
# plt.xlabel("year")
# plt.ylabel("Population of India vs China")
# plt.title("Population in billions ")
# #plt.legend(['China','India'])
# plt.legend()
import numpy as np
width=0.25    #default
indices=np.arange(len(year))

plt.grid()
plt.tight_layout()  #padding according to resolutions
# plt.subplot(1,2,1)
# plt.plot(year,indiapopu,'o--g',marker='o',linestyle='-',color='g',linewidth='3', label='India')
# plt.xlabel("year")
# plt.ylabel("Population in billions ")
# plt.title("Subplot 1")
# plt.legend()
#
# plt.subplot(1,2,2)
# plt.plot(year,chinapopu,marker='o',linestyle='--',color='b',linewidth='2', label='China')
# plt.xlabel("year")
# plt.ylabel("Population in billions ")
# plt.title("Subplot 2")
# plt.legend()

plt.bar(indices-width,indiapopu,label='India', color='green',width=width)
plt.bar(indices,chinapopu,label='China', color='blue',width=width)
plt.title("Population comparisons between India and china")
plt.xlabel("Year")
plt.ylabel("Population in billions")
plt.xticks(ticks=indices,labels=year)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()


plt.show()