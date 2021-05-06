# coding: gbk
# ʹ��CRITIC�͹۸�Ȩ�������ʵ������������Ԥ��ֵ
# ���е�����ָ���Ϊ������ָ�꣬ԽСԽ��
# �ο����ӣ�https://blog.csdn.net/stephen_curry300/article/details/106989729
# �ο����ģ����ֿ͹۸�Ȩ��������ȷ�����Ԥ��Ȩ���е�Ӧ��

# ȷ������һԤ��ģ��Ȩ�ز������£�
# 1����ԭʼ���߾���X���б�׼�������õ���׼������R
# 2���ɱ�׼���������������ָ��ĸ���
# 3�����͹۸�Ȩ�����������ָ���Ȩ�أ�������CRITIC���ͱ���ϵ�������֣�
# 4����󣬸���  ������ָ�����  ��  ������ָ���Ȩ��  �����Ԥ�ⷽ����Ȩ�أ�Ȩ��֮��Ϊ1.0

import numpy as np
import pandas as pd
import os
################### �������ϵ��Ȩ�� ###########################
def CvWeight(data,collist):
    '''
    data: dataframe��������
    collist����Ҫ����Ȩ�ص������б�
    '''
    # print('�������ϵ����....')
    statistic = data[collist].describe()                     # ����ͳ��ֵ
    cv = statistic.loc['std'] / abs(statistic.loc['mean'])   # ����CVֵ
    cv_sum = cv.sum()                                        # cv�ܺ�
    # print('����ϵ���ܺͣ�' + str(cv_sum))
    cv_weight = cv / cv_sum                                  # ����Ȩ��
    # print('%s ��Ȩ���ǣ�%s ��' % (collist,[cv_weight[col] for col in collist]))
    # pass
    return cv_weight
# pass
if __name__ == '__main__':
    # ����Ԥ��ģ�͵����ָ��Ϊ
    dir = os.listdir('classes')
    for item in dir:
        df = pd.read_excel('classes/' + item)
        df = df.iloc[:, 3:9]
        print(item[:-5])
        # df = np.array(df)
        w = CvWeight(df, df.columns)
        w = pd.DataFrame(w)
        print(w)
        # critic(df)
        # print(df.columns)
        # w = cal_weight(df)
        # w = w.T
        # w.columns = [df.columns]
        # print(w)
        print('\n\n')

    # X = np.array(
    #     [[0.0197, 199.4, 0.0083,  3.7740,  0.0244],
    #      [0.0545, 1603.6, 0.0619, 10.7023, 0.0665],
    #      [0.0263, 308,    0.0135, 4.6903,  0.0310],
    #      [0.0184, 158.5,  0.0062,  3.3642,  0.0211]]
    # )
    # CRITIC�����������ָ���Ȩ��


