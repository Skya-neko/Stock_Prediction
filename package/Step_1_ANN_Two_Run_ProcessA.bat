SET "today=%date:~0,10%"
python   .\package\Step_1_ANN_Two.py Step_0_ANN_Two_Result_ProcessA.csv Double >>   .\log\Log-ANN_Two_Result_ProcessA_%today:/=-%.txt  2>&1
pause :: Keep the window open
@REM %today:/=-% Means replace "/" with "-"