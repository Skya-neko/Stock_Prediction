set  project_root=D:\StockPrediction\StockPrediction\
cd /d %project_root%
echo Project root: %project_root%
SET "today=%date:~0,10%"
python   %project_root%\package\Step-1_CombineCSV.py   >>  %project_root%\log\Log-ANN_Two_CombineCSV_%today:/=-%.txt  2>&1
@REM pause :: schtask will make job run in backgroun, so don't pause because the window keep show up is annoying.
@REM %today:/=-% Means replace "/" with "-"
rem // Allow a key-press to abort the wait; `/T` can be omitted:
timeout /T 3