"""
******************************************************************
***  File Name		: MainMeasurement.py
***  Version		: V1.0
***  Designer		: 池戸 陸
***  Date			: 2022.06.02
***  Purpose        : 計測処理
***
*******************************************************************
*** Revision :
*** V1.0 : 池戸陸, 2022.06.02
"""

"""
*******************************************************************
***  Class Name		: MainMeasurement
***  Designer		    : 池戸 陸
***  Date		        : 2022.06.02
***  Function			: 計測時にダウンロード情報管理にファイルを要求する
                          瞬間速度、平均速度、安定性を求める
***  Return      	    : -1 エラー
                          0以上 計測結果
***
*******************************************************************
"""
#speedtestをimportしてやるならダウンロード情報管理がいらない話どうする?
class MainMeasurement:
    def get_speed_test():
        #計測DBSからファイルサイズを受け取る処理

        #計算する
        InstantSpeed = InstantSpeed()
        AverageSpeed = AverageSpeed()
        Stability = StabilityCalculation()
        return InstantSpeed,AverageSpeed,Stability
