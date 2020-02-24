
Bonus = 0;
BonusRateList = [[100,0.010],[60,0.015],[40,0.030],[20,0.050],[10,0.075],[0,0.100]];

Profit =  int(input('请输入当月利润:'));
Profit /= 10000;

for i in range(0, len(BonusRateList)) :
    if (Profit > BonusRateList[i][0]) :
        Bonus += ((Profit - BonusRateList[i][0]) * BonusRateList[i][1]);
        Profit = BonusRateList[i][0];

print (Bonus * 10000);
