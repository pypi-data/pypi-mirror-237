import pandas as pd
from main import Toolkit

test= Toolkit()

test_done = test.whole_quality_control(input_data="exemplar_data/preCARE.csv")
test_done.to_csv ("exemplar_data/CARE_test.csv", index = False, header=True)